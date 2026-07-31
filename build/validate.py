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
    except (KeyError, IndexError):
        failures.append(f"{rel}: no version at {'.'.join(map(str, path))}")
        continue
    check(found == version, f"{rel}: version {found} != version.txt {version}")

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

# `start` is a launcher, not a course: it routes and sequences but teaches
# nothing. Prose counts ("eight courses") must not include it.
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
    fm = text.split("---")[1]
    if "role: launcher" not in fm:
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
        n = len(desc.group(1).strip())
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

    for ref in re.findall(r"\]\((references/[^)]+)\)", text):
        check((skill / ref).exists(), f"{skill.name}: broken reference {ref}")

    # Conventions shared by every course in this family.
    check("What should I call you" in text, f"{skill.name}: missing the name-first wizard question")
    check("disable-model-invocation: true" in fm, f"{skill.name}: courses must be user-invoked")
    check(f"progress-{skill.name}.md" in text, f"{skill.name}: no file-based progress card")
    check(
        "unearned point is a fabrication" in (skill / "references/game-mode.md").read_text(),
        f"{skill.name}: game-mode.md missing the scoring-honesty rule",
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
    tone = skill / "references/tone.md"
    check(tone.exists(), f"{skill.name}: missing references/tone.md")
    check(
        tone.exists() and "Tone is delivery, never content" in tone.read_text(),
        f"{skill.name}: tone.md missing the delivery-not-content floor",
    )
    check(
        "code.claude.com/docs" in text or "platform.claude.com/docs" in text,
        f"{skill.name}: no enumerated doc domains to ground links against",
    )
    # docs.claude.com is stale; it may only appear as an explicit warning.
    for line in text.splitlines():
        if "docs.claude.com" in line and not re.search(r"never|stale", line, re.I):
            failures.append(f"{skill.name}: cites the stale docs.claude.com domain")
    check(
        "copy everything below" not in text and "don't paste this part" not in text,
        f"{skill.name}: leftover paste-in scaffolding",
    )

# Marketplace descriptions state the course count in prose, so adding a course
# silently strands every listing on the old number. Catch that.
WORDS = "one two three four five six seven eight nine ten".split()
for rel in [*MANIFESTS, "README.md"]:
    text = (ROOT / rel).read_text()
    for n, word in enumerate(WORDS, 1):
        if n != len(courses) and re.search(rf"\b{word}\b[^.]{{0,40}}\bcourses\b", text, re.I):
            failures.append(f"{rel}: claims '{word} courses' but there are {len(courses)}")

if failures:
    print(f"✘ {len(failures)} failure(s):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)

launchers = [s.name for s in skills if s not in courses]
print(f"✔ v{version} — {len(courses)} courses, {len(MANIFESTS)} manifests in lockstep")
print(f"  courses: {', '.join(s.name for s in courses)}")
print(f"  launcher: {', '.join(launchers) or 'none'}")
