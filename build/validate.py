#!/usr/bin/env python3
"""Validate every skill against the Agent Skills spec, and every platform
manifest against version.txt.

Release Please bumps version.txt, every SKILL.md, and every platform manifest
together. This script fails loudly if any of them drift apart — most likely
because a version was edited by hand.

Run locally with `python3 build/validate.py`; CI runs the same script.
"""
import json
import pathlib
import re
import sys

try:
    import yaml
except ImportError:  # CI installs it; local runs fall back to the targeted check below
    yaml = None

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
DESC_MAX = 200  # claude.ai upload cap; the open spec allows 1024

# Every manifest that must carry the release version, and where it lives.
MANIFESTS = {
    ".claude-plugin/plugin.json": ("version",),
    ".claude-plugin/marketplace.json": ("plugins", 0, "version"),
    ".codex-plugin/plugin.json": ("version",),
    ".cursor-plugin/plugin.json": ("version",),
    ".grok-plugin/plugin.json": ("version",),
    ".grok-plugin/marketplace.json": ("plugins", 0, "version"),
    ".agents/plugins/marketplace.json": ("plugins", 0, "version"),
    "gemini-extension.json": ("version",),
}

failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)


def dig(obj, path):
    for key in path:
        obj = obj[key]
    return obj


version = (ROOT / "version.txt").read_text().strip()
check(re.fullmatch(r"\d+\.\d+\.\d+", version), f"version.txt: '{version}' is not semver")

for rel, path in MANIFESTS.items():
    f = ROOT / rel
    if not f.exists():
        failures.append(f"{rel}: missing")
        continue
    try:
        data = json.loads(f.read_text())
    except Exception as exc:
        failures.append(f"{rel}: invalid JSON — {exc}")
        continue
    try:
        found = dig(data, path)
    except (KeyError, IndexError, TypeError):
        failures.append(f"{rel}: no version at {'.'.join(map(str, path))}")
        continue
    check(found == version, f"{rel}: version {found} != version.txt {version}")

# The Claude marketplace carries an optional container version in metadata.version
# that release-please does not manage; the other two marketplaces omit it. If it
# ever reappears here it must still match the lockstep, or it drifts silently.
mkt_meta_version = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text()).get("metadata", {}).get("version")
check(
    mkt_meta_version in (None, version),
    f".claude-plugin/marketplace.json: metadata.version {mkt_meta_version} != version.txt {version}",
)

# The README badge is the version most people actually read, so it is held to the
# same lockstep as the manifests. It uses shields' static/v1 query form rather
# than /badge/version-X-colour: in the path form the trailing colour parses as a
# semver prerelease, so release-please rewrote "0.1.0-blue" to "0.1.1" and
# produced a badge that rendered "404: badge not found".
badge_line = next(
    (l for l in (ROOT / "README.md").read_text().splitlines() if "label=version" in l), ""
)
found = re.search(r"message=(\d+\.\d+\.\d+)&", badge_line)
check(found, "README.md: no version badge found")
if found:
    check(found.group(1) == version, f"README.md: badge {found.group(1)} != version.txt {version}")
check(
    "x-release-please-version" in badge_line,
    "README.md: version badge missing the release-please marker",
)

skills = sorted(p for p in SKILLS.iterdir() if p.is_dir())
check(skills, "no skills found")

# A skill Release Please doesn't know about keeps its old version while everything
# else moves, and lockstep fails on the *next* release rather than this commit.
registered = {
    e.get("path")
    for e in json.loads((ROOT / "release-please-config.json").read_text())["packages"]["."]["extra-files"]
}
for skill in skills:
    rel = f"skills/{skill.name}/SKILL.md"
    check(rel in registered, f"{skill.name}: not in release-please extra-files — its version will not bump")

# Skills carrying a `role:` are support skills, not courses — `start` routes,
# `companion` drills — and neither teaches new material. Prose counts ("eight
# courses") must not include them.
courses = []

for skill in skills:
    md = skill / "SKILL.md"
    if not md.exists():
        failures.append(f"{skill.name}: missing SKILL.md")
        continue
    text = md.read_text()
    if not text.startswith("---"):
        failures.append(f"{skill.name}: SKILL.md has no YAML frontmatter")
        continue
    parts = text.split("---", 2)
    if len(parts) < 3:
        failures.append(f"{skill.name}: SKILL.md frontmatter has no closing '---'")
        continue
    fm = parts[1]
    # Regex-reading the frontmatter is how an unquoted ": " in six descriptions
    # went unnoticed: the runtime drops ALL metadata when the YAML fails, so the
    # skill installs nameless and undiscoverable. Parse it properly.
    if yaml is not None:
        try:
            yaml.safe_load(fm)
        except Exception as exc:
            failures.append(f"{skill.name}: frontmatter is not valid YAML — {str(exc).splitlines()[0]}")
    else:
        raw = re.search(r"^description: (.+)$", fm, re.M)
        if raw and ": " in raw.group(1) and not raw.group(1).strip().startswith(('"', "'")):
            failures.append(f"{skill.name}: description contains ': ' and is unquoted — breaks YAML")

    # Hazards a YAML parser accepts silently, or that break the split above.
    check(text.startswith("---\n"), f"{skill.name}: SKILL.md must open with '---'")
    check("\t" not in fm, f"{skill.name}: tab in frontmatter — illegal YAML indentation")
    fm_keys = re.findall(r"^(\w[\w-]*):", fm, re.M)
    check(
        len(fm_keys) == len(set(fm_keys)),
        f"{skill.name}: duplicate frontmatter key — YAML keeps only the last silently",
    )

    if not re.search(r"^  role: ", fm, re.M):
        courses.append(skill)

    name = re.search(r"^name: (.+)$", fm, re.M)
    desc = re.search(r"^description: (.+)$", fm, re.M)
    check(name, f"{skill.name}: no name field")
    check(desc, f"{skill.name}: no description field")
    if name:
        value = name.group(1).strip()
        check(value == skill.name, f"{skill.name}: name '{value}' != folder name")
        check(NAME_RE.fullmatch(value), f"{skill.name}: name '{value}' breaks the charset rule")
        check(len(value) <= 64, f"{skill.name}: name longer than 64 chars")
    if desc:
        n = len(desc.group(1).strip().strip('"'))
        check(n <= DESC_MAX, f"{skill.name}: description {n} chars, max {DESC_MAX}")

    skill_version = re.search(r"^  version: (.+)$", fm, re.M)
    check(skill_version, f"{skill.name}: no metadata.version")
    if skill_version:
        found = skill_version.group(1).strip().strip('"')
        check(found == version, f"{skill.name}: version {found} != version.txt {version}")
    check(
        "x-release-please-start-version" in fm,
        f"{skill.name}: missing the release-please version marker",
    )

    check(text.count("\n") < 500, f"{skill.name}: SKILL.md over 500 lines")

    linked = set()
    for ref in re.findall(r"\]\((references/[^)]+)\)", text):
        check((skill / ref).exists(), f"{skill.name}: broken reference {ref}")
        linked.add(ref.split("/")[-1].split("#")[0])

    # The other direction. A reference file nothing loads is not merely dead
    # weight: companion shipped a game-mode.md defining its own XP events and
    # rank ladder, no line of its SKILL.md ever read it, and the Progress Card
    # still demanded "next at [n]" — so the model had to invent a rank, or
    # borrow the courses' ladder, which scores something else entirely.
    for ref in sorted((skill / "references").glob("*.md")):
        check(
            ref.name in linked,
            f"{skill.name}: references/{ref.name} is never loaded by SKILL.md",
        )

    # Conventions shared by every course in this family.
    check("What should I call you" in text, f"{skill.name}: missing the name-first wizard question")
    check("disable-model-invocation: true" in fm, f"{skill.name}: courses must be user-invoked")
    check(f"progress-{skill.name}.md" in text, f"{skill.name}: no file-based progress card")
    game = (skill / "references/game-mode.md").read_text()
    check(
        "unearned point is a fabrication" in game,
        f"{skill.name}: game-mode.md missing the scoring-honesty rule",
    )
    # The card asks for "next at [n]". Without numeric bands on the rank ladder
    # that number cannot be derived, so the model invents one and persists it.
    ladder = re.search(r"^## Ranks[^\n]*\n\n(.+)$", game, re.M)
    check(ladder, f"{skill.name}: game-mode.md has no rank ladder")
    if ladder:
        check(
            re.search(r"\(\d", ladder.group(1)),
            f"{skill.name}: rank ladder has no numeric bands, so 'next at' is underivable",
        )
    # Anti-hallucination guardrails, from the 2026-07-24 audit. These must sit
    # inside the GROUND RULES block so a truncated paste still carries them.
    ground = text.split("## GROUND RULES", 1)[-1].split("\n## ", 1)[0]
    check("No search tool" in ground, f"{skill.name}: no tool guard in GROUND RULES")
    check("When unsure, say so" in ground, f"{skill.name}: no uncertainty rule in GROUND RULES")
    check("Never construct a URL" in ground, f"{skill.name}: no URL-fabrication rule in GROUND RULES")
    check(
        "Never state a figure you did not look up" in ground,
        f"{skill.name}: no unlooked-up-figure rule in GROUND RULES",
    )
    # Tone is the one feature that can quietly undo the rest: a voice the learner
    # picked must never license a claim the evidence doesn't.
    check(
        "Tone never changes what is true" in ground,
        f"{skill.name}: tone must not be allowed to override the guardrails",
    )
    # Two later additions, same placement rule: a truncated paste must still carry
    # them. The first closes the gap between "never state a figure" and the
    # broader habit of narrating files, outputs and sessions never seen; the
    # second keeps every guardrail in force when the learner writes in another
    # language, which is where a hedge is most likely to be dropped in translation.
    check(
        "Never invent what you did not read or run" in ground,
        f"{skill.name}: no 'Never invent what you did not read or run' rule in GROUND RULES",
    )
    check(
        "Teach in the learner's language" in ground,
        f"{skill.name}: no learner-language rule in GROUND RULES",
    )
    check("Tone of voice?" in text, f"{skill.name}: wizard never offers a tone")
    check("Tone: [chosen voice" in text, f"{skill.name}: Progress Card does not carry the tone")
    # A pasted card is the only save file on chat surfaces, so it has to be
    # recognisable on sight and say which lane it came from.
    check(
        f"<!-- ai-docent:card v1 course={skill.name} -->" in text,
        f"{skill.name}: Progress Card missing its opening marker",
    )
    check("<!-- ai-docent:card-end -->" in text, f"{skill.name}: Progress Card missing its closing marker")
    check(
        f"Storage: [file: ~/.ai-docent/progress-{skill.name}.md" in text,
        f"{skill.name}: Progress Card does not record which storage lane was used",
    )
    check(
        "Date: [today's date" in text,
        f"{skill.name}: Progress Card date is not grounded against a guessed year",
    )
    # A card is the entire state of the course, so it cannot be trusted on sight:
    # wrong-course, stale and truncated cards all corrupt progress silently.
    check(
        "Checking a card before you trust it" in text,
        f"{skill.name}: cards are trusted without validation",
    )
    check(f"The marker reads `course={skill.name}`" in text, f"{skill.name}: no wrong-card check")
    check("**Complete?**" in text, f"{skill.name}: no truncated-card check")
    check("Silently resuming from an older card" in text, f"{skill.name}: no stale-card check")
    check("`reconstructed`" in text, f"{skill.name}: no cold-start rebuild path")
    check(
        "When something doesn't fit" in text,
        f"{skill.name}: no edge-case handling for malformed or conflicting cards",
    )
    # The wizard's stated counts are checked against the questions actually
    # written, so adding a branch question can't silently make the cap a lie.
    check(
        re.search(r"Hard ceiling of \d+|(?:maximum|max|more than) \w+ questions", text),
        f"{skill.name}: wizard states no question ceiling",
    )
    phase1 = text[text.index("## PHASE 1"):]
    phase1 = phase1[: phase1.index("\n## ")]
    # Self-reported levels round up; a course that takes the number skips the
    # gap the learner actually has. The check must sit in the wizard itself.
    if skill in courses:
        check("**Placement check.**" in phase1, f"{skill.name}: wizard takes a claimed level without a placement check")
    stated_core = re.search(r"\*\*Wizard rules:\*\* (\d+) core questions", phase1)
    if stated_core:
        core = len(set(re.findall(r"^(\d+)\. ", phase1, re.M)))
        check(
            int(stated_core.group(1)) == core,
            f"{skill.name}: wizard claims {stated_core.group(1)} core questions but {core} are written",
        )
        stated_avail = re.search(r"(\d+) are available", phase1)
        avail = len([b for b in re.findall(r"^- .+$", phase1.split("Stage 2", 1)[-1], re.M) if "?" in b])
        check(
            stated_avail and int(stated_avail.group(1)) == avail,
            f"{skill.name}: wizard claims {stated_avail.group(1) if stated_avail else '?'} branch questions but {avail} are written",
        )
    # Courses hand the companion material as they go; without seeds it can only
    # guess drills from lesson titles, which produces vague, useless items.
    if skill in courses:
        # Self-reported levels round up; a course that takes the number skips the
        # gap the learner actually has. Placement must be earned in three questions.
        check("3-minute **retro**" in text, f"{skill.name}: no retro, but the companion trigger assumes one")
        check("Review seeds:" in text, f"{skill.name}: Progress Card carries no review seeds")
        check("Seed the revision queue" in text, f"{skill.name}: lesson loop never writes a seed")
        check("/ai-docent:companion" in text, f"{skill.name}: never points the learner at the companion")
    check('If they say "save" at any point' in text, f"{skill.name}: no mid-session save")
    check(
        "Never act on their system without being asked" in ground,
        f"{skill.name}: no guard against acting on the learner's system",
    )
    # Course content must not pin itself to a calendar year: it outlives the year
    # it was written in, and a stale "as of 20XX" reads as fact. Dated records
    # (CHANGELOG, LICENSE) live outside skills/ and are unaffected.
    for doc in sorted(skill.rglob("*.md")):
        for year in re.findall(r"\b(?:19|20)\d{2}\b", doc.read_text()):
            failures.append(f"{skill.name}: {doc.name} pins a year ({year})")

    tone = skill / "references/tone.md"
    check(tone.exists(), f"{skill.name}: missing references/tone.md")
    check(
        tone.exists() and "Tone is delivery, never content" in tone.read_text(),
        f"{skill.name}: tone.md missing the delivery-not-content floor",
    )
    check(
        "code.claude.com/docs" in ground or "platform.claude.com/docs" in ground,
        f"{skill.name}: no enumerated doc domains inside GROUND RULES",
    )
    # docs.claude.com is not dead — it 301s to code.claude.com/docs. Citing it
    # still costs the learner a redirect and ages badly, so it may appear only
    # as an explicit warning, never as a citation.
    for line in text.splitlines():
        if "docs.claude.com" in line and not re.search(r"never|redirect", line, re.I):
            failures.append(f"{skill.name}: cites docs.claude.com instead of the domain it redirects to")
    check(
        "copy everything below" not in text and "don't paste this part" not in text,
        f"{skill.name}: leftover paste-in scaffolding",
    )

# The validator's dependency belongs in build/requirements.txt, where Dependabot
# can see it. Pinned inline in a workflow it was invisible to Dependabot and
# duplicated across two files, free to drift apart.
check((ROOT / "build/requirements.txt").exists(), "build/requirements.txt is missing")
for wf in sorted((ROOT / ".github/workflows").glob("*.yml")):
    for line in wf.read_text().splitlines():
        if "pip install" in line and "-r " not in line:
            failures.append(f"{wf.name}: pins a dependency inline — install from build/requirements.txt instead")

# tone.md is the one reference file that is deliberately identical everywhere:
# it is the floor a chosen voice may never lower. Ten copies with nothing
# holding them together means editing one forks the other nine silently, and
# the voice menu a learner sees would depend on which course they opened.
by_content = {}
for skill in skills:
    tone_file = skill / "references/tone.md"
    if tone_file.exists():
        by_content.setdefault(tone_file.read_bytes(), []).append(skill.name)
if len(by_content) > 1:
    shared = max(by_content.values(), key=len)
    drifted = sorted(n for group in by_content.values() if group is not shared for n in group)
    failures.append(
        f"references/tone.md has drifted in: {', '.join(drifted)} — every skill carries the identical floor"
    )

# The validator proves the files are well-formed; the eval suite checks the
# skills behave. A skill with no case is a skill nothing has ever watched refuse
# to fabricate. Every skill must be the opening command of at least one prompt —
# a mention inside a pasted card or a sentence does not count.
invoked = set()
for p in (ROOT / "evals").rglob("prompt.md"):
    body = p.read_text().split("---", 2)[-1].strip()
    first = body.split("\n", 1)[0].strip()
    m = re.fullmatch(r"/ai-docent:([a-z-]+)", first)
    if m:
        invoked.add(m.group(1))
for skill in skills:
    check(skill.name in invoked, f"{skill.name}: no eval case opens with /ai-docent:{skill.name} — nothing checks it behaves")

# A cheat-sheet is the course with the practice removed, so it is the easiest
# place for an invented habit to hide. Every sheet must exist, be indexed, and
# cite only lesson numbers its curriculum actually has — in "(2.6)" and
# "(5.1, 5.3)" form alike.
docs_index = (ROOT / "docs/README.md").read_text()
for skill in courses:
    sheet = ROOT / f"docs/cheatsheets/{skill.name}.md"
    if not sheet.exists():
        failures.append(f"{skill.name}: no docs/cheatsheets/{skill.name}.md")
        continue
    check(f"cheatsheets/{skill.name}.md" in docs_index, f"{skill.name}: cheat-sheet not listed in docs/README.md")
    lessons = set(re.findall(r"^- \*\*(\d+\.\d+)", (skill / "references/curriculum.md").read_text(), re.M))
    for group in re.findall(r"\((\d+\.\d+(?:,\s*\d+\.\d+)*)\)", sheet.read_text()):
        for ref in re.split(r",\s*", group):
            check(ref in lessons, f"{skill.name}: cheat-sheet cites lesson {ref}, which the curriculum does not have")

# docs/README.md is the only way into docs/. A guide missing from it is a guide
# nobody finds, at any depth.
linked_docs = set(re.findall(r"\]\(([\w/-]+\.md)\)", docs_index))
for doc in sorted((ROOT / "docs").rglob("*.md")):
    rel_doc = doc.relative_to(ROOT / "docs").as_posix()
    if rel_doc != "README.md":
        check(rel_doc in linked_docs, f"docs/{rel_doc} is not listed in docs/README.md")

# The issue templates enumerate the skills. A skill missing from them is one
# nobody can file a report against, which is exactly the report worth having.
for tmpl in (".github/ISSUE_TEMPLATE/course_correction.yml", ".github/ISSUE_TEMPLATE/bug_report.yml"):
    body = (ROOT / tmpl).read_text()
    for skill in skills:
        check(
            re.search(rf"^\s*-?\s*{re.escape(skill.name)}\b", body, re.M),
            f"{tmpl}: does not offer {skill.name}",
        )

# The README's level column is the only place the shape of each course is
# advertised, and nothing about adding a LEVEL heading to a curriculum forces
# the table to move with it.
readme = (ROOT / "README.md").read_text()
for name, claim in re.findall(r"^\| `([a-z-]+)` \| ([0-9]+(?:–[0-9]+)?) \|", readme, re.M):
    curriculum = SKILLS / name / "references/curriculum.md"
    if not curriculum.exists():
        failures.append(f"README.md: table row `{name}` has no curriculum.md")
        continue
    levels = sorted({int(n) for n in re.findall(r"^##\s*LEVEL\s+(\d+)", curriculum.read_text(), re.M | re.I)})
    if not levels:
        failures.append(f"{name}: curriculum.md has no '## LEVEL n' headings")
        continue
    expected = f"{levels[0]}–{levels[-1]}" if levels[0] == 0 else str(levels[-1])
    check(claim == expected, f"README.md: `{name}` shows levels {claim}, curriculum has {expected}")

# Marketplace descriptions state the course count in prose, so adding a course
# silently strands every listing on the old number. Catch that.
WORDS = "one two three four five six seven eight nine ten".split()
for rel in [*MANIFESTS, "README.md"]:
    text = (ROOT / rel).read_text()
    for n, word in enumerate(WORDS, 1):
        if n != len(courses) and re.search(rf"\b{word}\b[^.]{{0,40}}\bcourses\b", text, re.I):
            failures.append(f"{rel}: claims '{word} courses' but there are {len(courses)}")

# A wrong version ships and gets fixed next release. A committed credential is
# burned the moment it is pushed, and a scraped address stays scraped — neither
# is undone by a later commit, so they are worth a gate that runs before the
# push. GitHub scans provider tokens on public repos for free, but the generic
# shapes below (private keys, credentialed URLs, auth headers, assigned
# literals) need an organization-owned repo on Team or higher with Secret
# Protection. This one is user-owned, so that scanning will never apply to it.
SECRET_SHAPES = [
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key block"),
    (r"[a-z][a-z0-9+.\-]*://[^/\s:@]+:[^/\s:@]+@", "credentialed connection string"),
    (r"(?i)authorization\s*:\s*(bearer|basic)\s+[A-Za-z0-9._~+/=\-]{16,}",
     "auth header carrying a credential"),
    (r"(?i)\b(api[_-]?key|secret|token|password|passwd|credential)s?\b\W{0,3}[:=]\s*"
     r"[\"'][A-Za-z0-9/+_.\-]{16,}[\"']", "assigned credential literal"),
]

# This repo publishes no contact address at all. Conduct reports route through
# GitHub's report-abuse form and security reports through private advisories,
# so both private channels exist without an inbox to scrape. Any address that
# appears here now arrived by accident — which is exactly what to catch, since
# a published address cannot be unpublished once it has been crawled.
EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}")
EMAIL_OK = re.compile(
    r"git@github\.com|[^@]+@example\.(com|org)|[^@]+@users\.noreply\.github\.com"
)

HYGIENE_SKIP = {".git", "dist", "__pycache__", "node_modules", ".venv", "venv"}
HYGIENE_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".sh", ".txt", ".py"}
for f in sorted(ROOT.rglob("*")):
    # validate.py holds the patterns and test_validate.py holds the probes that
    # must match them; scanning either would make this gate fail on itself.
    if not f.is_file() or HYGIENE_SKIP & set(f.parts):
        continue
    # Eval runs write transcripts and judge output under evals/results/, which is
    # gitignored and full of tool-call artefacts that look like addresses.
    if "evals/results/" in f.relative_to(ROOT).as_posix():
        continue
    if f.suffix not in HYGIENE_SUFFIXES or f.name in ("validate.py", "test_validate.py"):
        continue
    rel = f.relative_to(ROOT)
    for i, line in enumerate(f.read_text(errors="ignore").splitlines(), 1):
        if "/Users/" in line:
            failures.append(f"{rel}:{i}: user-specific absolute path — write ~/ instead")
        for pattern, what in SECRET_SHAPES:
            if re.search(pattern, line):
                failures.append(f"{rel}:{i}: {what} — never commit a live credential")
        for m in EMAIL_RE.finditer(line):
            if not EMAIL_OK.fullmatch(m.group(0)):
                failures.append(f"{rel}:{i}: unexpected email {m.group(0)}")

if failures:
    print(f"✘ {len(failures)} failure(s):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)

support = [s.name for s in skills if s not in courses]
print(f"✔ v{version} — {len(courses)} courses, {len(MANIFESTS)} manifests in lockstep")
print(f"  courses: {', '.join(s.name for s in courses)}")
print(f"  support: {', '.join(support) or 'none'}")
