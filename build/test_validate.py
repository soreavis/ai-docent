#!/usr/bin/env python3
"""Prove each gate in validate.py actually fires.

A gate that has never failed has not been shown to work. This repo learned that
the hard way: the frontmatter check read YAML with a regex, passed on all ten
skills, and hid six whose metadata did not parse — every one of which would have
installed nameless and undiscoverable.

Each case copies the repo to a temp dir, breaks exactly one thing, and asserts
validate.py exits non-zero with the message that names it. Adding a gate without
adding a case here leaves the same hole open.

Run with `python3 build/test_validate.py`; CI runs the same script.
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parent.parent
IGNORE = shutil.ignore_patterns(".git", "dist", "__pycache__", "*.pyc", "results")


def edit(root, rel, old, new):
    p = root / rel
    text = p.read_text()
    if old not in text:
        raise AssertionError(f"fixture is stale: {old!r} not found in {rel}")
    p.write_text(text.replace(old, new, 1))


def edit_all(root, rel, old, new):
    p = root / rel
    text = p.read_text()
    if old not in text:
        raise AssertionError(f"fixture is stale: {old!r} not found in {rel}")
    p.write_text(text.replace(old, new))


def append(root, rel, text):
    (root / rel).write_text((root / rel).read_text() + text)


def unquoted_description(root):
    p = root / "skills/builder/SKILL.md"
    text = p.read_text()
    desc = re.search(r"^description: .+$", text, re.M).group(0)
    p.write_text(text.replace(desc, "description: Teach them: the API, tools, and agents.", 1))


def duplicate_key(root):
    edit(root, "skills/builder/SKILL.md", "\nlicense:", "\nname: builder\nlicense:")


def drift_manifest(root):
    p = root / ".claude-plugin/plugin.json"
    data = json.loads(p.read_text())
    data["version"] = "9.9.9"
    p.write_text(json.dumps(data, indent=2) + "\n")


def unregister_skill(root):
    p = root / "release-please-config.json"
    data = json.loads(p.read_text())
    files = data["packages"]["."]["extra-files"]
    data["packages"]["."]["extra-files"] = [f for f in files if f.get("path") != "skills/companion/SKILL.md"]
    p.write_text(json.dumps(data, indent=2) + "\n")


def orphan_reference(root):
    """The bug this file was written after: a reference nothing loads.

    Every link must go — one surviving mention still satisfies the gate, which
    is exactly what this fixture got wrong the first time it ran.
    """
    edit_all(
        root,
        "skills/companion/SKILL.md",
        "[references/game-mode.md](references/game-mode.md)",
        "the game mode rules",
    )


def strip_rank_bands(root):
    """Each course names its ranks differently, so strip the bands structurally."""
    p = root / "skills/builder/references/game-mode.md"
    text = p.read_text()
    ladder = re.search(r"^## Ranks[^\n]*\n\n(.+)$", text, re.M)
    if not ladder:
        raise AssertionError("fixture is stale: no rank ladder in builder/game-mode.md")
    p.write_text(text.replace(ladder.group(1), re.sub(r"\s*\([^)]*\d[^)]*\)", "", ladder.group(1)), 1))


# Built at runtime so this file never contains an address-shaped string itself.
PLANTED = "ada" + "@" + "mailbox" + "." + "net"
ESCAPED = PLANTED.replace(".", "\\.")


def allowlist_grouped_address(root):
    """The same leak written as the validator's own regex idiom, host\.(a|b)."""
    p = root / "build/validate.py"
    text = p.read_text()
    marker = 'EMAIL_OK = re.compile(\n    r"'
    if marker not in text:
        raise AssertionError("fixture is stale: EMAIL_OK definition moved")
    grouped = "ada" + "@" + "mailbox\\.(net|org)|"
    p.write_text(text.replace(marker, marker + grouped, 1))


def allowlist_planted_address(root):
    """The original leak: an address added to the validator's own allowlist."""
    p = root / "build/validate.py"
    text = p.read_text()
    marker = 'EMAIL_OK = re.compile(\n    r"'
    if marker not in text:
        raise AssertionError("fixture is stale: EMAIL_OK definition moved")
    p.write_text(text.replace(marker, marker + ESCAPED + "|", 1))


CASES = [
    ("an escaped address in a doc", lambda r: append(r, "docs/troubleshooting.md", f"\nWrite to {ESCAPED} instead.\n"), "unexpected email"),
    ("an address allow-listed inside the validator", allowlist_planted_address, "build/validate.py"),
    ("a grouped regex address allow-listed inside the validator", allowlist_grouped_address, "build/validate.py"),
    (
        "runtime note dropped from a skill",
        lambda r: edit(r, "skills/companion/SKILL.md", "give the form it uses", "use the right form"),
        "no note for other runtimes",
    ),
    (
        "Codex invocation policy removed",
        lambda r: (r / "skills/builder/agents/openai.yaml").write_text("policy: {}\n"),
        "no agents/openai.yaml",
    ),
    ("frontmatter with an unquoted ': '", unquoted_description, "not valid YAML"),
    ("duplicate frontmatter key", duplicate_key, "duplicate frontmatter key"),
    ("manifest version drift", drift_manifest, "version 9.9.9"),
    ("skill missing from release-please", unregister_skill, "not in release-please extra-files"),
    ("reference file nothing loads", orphan_reference, "never loaded by SKILL.md"),
    ("rank ladder without numeric bands", strip_rank_bands, "no numeric bands"),
    (
        "README badge out of lockstep",
        lambda r: edit(r, "README.md", f"message={(r / 'version.txt').read_text().strip()}", "message=9.9.9"),
        "README",
    ),
    (
        "README level column drift",
        lambda r: append(r, "skills/builder/references/curriculum.md", "\n## LEVEL 6 — extra\n"),
        "curriculum has 6",
    ),
    (
        "angle bracket in a description",
        lambda r: edit(r, "skills/start/SKILL.md", "Entry point for the ai-docent courses.", "Entry point for the <ai-docent> courses."),
        "description contains < or >",
    ),
    (
        "progress-file exception dropped from GROUND RULES",
        lambda r: edit(r, "skills/shipping/SKILL.md", "The one standing exception is this skill's own progress file", "One exception is the progress file"),
        "GROUND RULES forbid the progress file",
    ),
    (
        "README course size gone stale",
        lambda r: edit(r, "README.md", "runs roughly 21–23 KB", "runs roughly 15–20 KB"),
        "says 15–20 KB",
    ),
    (
        "a truncated-card check removed",
        lambda r: edit(r, "skills/long-haul/SKILL.md", "**Complete?**", "**Whole?**"),
        "no truncated-card check",
    ),
    (
        "cheat-sheet citing a lesson inside a list of citations",
        lambda r: edit(r, "docs/cheatsheets/builder.md", "(5.1, 5.3)", "(5.1, 9.9)"),
        "cites lesson 9.9",
    ),
    (
        "an unlisted file inside docs/cheatsheets",
        lambda r: (r / "docs/cheatsheets/zzz-notes.md").write_text("# stray\n"),
        "docs/cheatsheets/zzz-notes.md is not listed",
    ),
    (
        "cheat-sheet citing a lesson that does not exist",
        lambda r: edit(r, "docs/cheatsheets/reliability.md", "(2.3)", "(9.9)"),
        "cites lesson 9.9",
    ),
    (
        "a skill with no eval case",
        lambda r: edit(r, "evals/language-follows-learner/prompt.md", "/ai-docent:prompt-craft", "/ai-docent:promptcraft"),
        "no eval case opens with /ai-docent:prompt-craft",
    ),
    (
        "placement check dropped from a course wizard",
        lambda r: edit(r, "skills/prompt-craft/SKILL.md", "**Placement check.**", "**Level claim.**"),
        "without a placement check",
    ),
    (
        "never-narrate-the-unseen rule removed",
        lambda r: edit(r, "skills/security/SKILL.md", "Never invent what you did not read or run", "Never invent what you did not read"),
        "no 'Never invent what you did not read or run' rule",
    ),
    (
        "learner-language rule removed",
        lambda r: edit(r, "skills/mechanics/SKILL.md", "Teach in the learner's language", "Teach in English"),
        "no learner-language rule",
    ),
    (
        "guardrail moved out of GROUND RULES",
        lambda r: edit(r, "skills/builder/SKILL.md", "No search tool", "No lookup tool"),
        "no tool guard in GROUND RULES",
    ),
    (
        "a calendar year pinned in course content",
        lambda r: append(r, "skills/builder/references/curriculum.md", "\nAs of 2026, this holds.\n"),
        "pins a year",
    ),
    (
        "docs.claude.com cited rather than warned about",
        lambda r: append(r, "skills/builder/SKILL.md", "\nSee https://docs.claude.com/en/docs for more.\n"),
        "cites docs.claude.com",
    ),
    (
        "prose course count drift",
        lambda r: edit(r, "README.md", "Eight multi-session", "Nine multi-session"),
        "courses",
    ),
    (
        "one skill's tone.md forked from the rest",
        lambda r: append(r, "skills/security/references/tone.md", "\n- **Swashbuckler** — piratical.\n"),
        "tone.md has drifted in: security",
    ),
    (
        "a guide missing from the docs index",
        lambda r: (r / "docs/orphan.md").write_text("# Orphan\n"),
        "not listed in docs/README.md",
    ),
    (
        "dependency pinned inline in a workflow",
        lambda r: edit(r, ".github/workflows/ci.yml", "-r build/requirements.txt", "pyyaml==6.0.3"),
        "pins a dependency inline",
    ),
    (
        "issue template missing a skill",
        lambda r: edit(r, ".github/ISSUE_TEMPLATE/course_correction.yml", "companion", "compangion"),
        "does not offer companion",
    ),
    (
        "private key committed",
        lambda r: append(r, "docs/troubleshooting.md", "\n-----BEGIN RSA PRIVATE KEY-----\n"),
        "private key block",
    ),
    (
        "connection string carrying credentials",
        lambda r: append(r, "docs/troubleshooting.md", "\npostgres://admin:hunter2islong@db:5432/app\n"),
        "credentialed connection string",
    ),
    (
        "auth header carrying a credential",
        lambda r: append(r, "docs/troubleshooting.md", "\nAuthorization: Bearer abcdef0123456789ghijkl\n"),
        "auth header carrying a credential",
    ),
    (
        "credential assigned to a literal",
        lambda r: append(r, "docs/troubleshooting.md", '\napi_key = "AKIAIOSFODNN7EXAMPLEKEY"\n'),
        "assigned credential literal",
    ),
    (
        "an address that is not the maintainer's",
        lambda r: append(r, "docs/troubleshooting.md", "\nMail someone@some-employer.invalid instead.\n"),
        "unexpected email",
    ),
    (
        "a path with a real username in it",
        lambda r: append(r, "docs/troubleshooting.md", "\nRun it from /Users/ada/code/ai-docent.\n"),
        "user-specific absolute path",
    ),
]


def run(root):
    return subprocess.run(
        [sys.executable, str(root / "build/validate.py")],
        capture_output=True,
        text=True,
    )


# Both address rules are pinned verbatim. Widening either one is the change that
# let a real address into the public history, so it must fail here as well as
# in review.
PINNED = (
    'r"(git|noreply|support)@github\\.com|[^@]+@users\\.noreply\\.github\\.com|[^@]+@example\\.(com|org)",',
    'r"(git|noreply|support)@github\\.com|[^@]+@users\\.noreply\\.github\\.com|[^@]+@example\\.(com|org)|[^@]+@[\\w.-]+\\.invalid",',
)


def main():
    failures = []
    source = (REPO / "build/validate.py").read_text()
    for rule in PINNED:
        if rule not in source:
            failures.append(f"pinned address rule changed or missing: {rule}")
    print("  ok   address rules match their pins" if not failures else "  FAIL address rules differ from their pins")

    with tempfile.TemporaryDirectory() as tmp:
        clean = pathlib.Path(tmp) / "clean"
        shutil.copytree(REPO, clean, ignore=IGNORE)
        result = run(clean)
        if result.returncode != 0:
            failures.append(f"baseline: an unmodified repo must pass, got:\n{result.stdout}")
        else:
            print("  ok   baseline — unmodified repo passes")

    for name, mutate, expected in CASES:
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp) / "repo"
            shutil.copytree(REPO, root, ignore=IGNORE)
            try:
                mutate(root)
            except AssertionError as exc:
                failures.append(f"{name}: {exc}")
                print(f"  FAIL {name} — {exc}")
                continue
            result = run(root)
            if result.returncode == 0:
                failures.append(f"{name}: validate.py passed a repo that should fail")
                print(f"  FAIL {name} — gate did not fire")
            elif expected not in result.stdout:
                failures.append(f"{name}: expected {expected!r} in output, got:\n{result.stdout}")
                print(f"  FAIL {name} — fired with the wrong message")
            else:
                print(f"  ok   {name}")

    # --history runs on a real git repo, so it gets its own case: an address
    # committed and then removed must still fail, which a tree scan cannot see.
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp) / "repo"
        shutil.copytree(REPO, root, ignore=IGNORE)
        git = lambda *a: subprocess.run(["git", "-C", str(root), *a], capture_output=True, text=True)
        git("init", "-q")
        git("config", "user.email", "ci@users.noreply.github.com")
        git("config", "user.name", "ci")
        git("add", "-A")
        git("commit", "-qm", "base")
        clean = subprocess.run([sys.executable, str(root / "build/validate.py"), "--history"], capture_output=True, text=True)
        (root / "docs/note.md").write_text(f"Write to {ESCAPED}.\n")
        git("add", "-A")
        git("commit", "-qm", "add")
        (root / "docs/wide.md").write_bytes(f"Mail {PLANTED}.".encode("utf-16"))
        git("add", "-A")
        git("commit", "-qm", "wide")
        (root / "docs/note.md").unlink()
        (root / "docs/wide.md").unlink()
        git("add", "-A")
        git("commit", "-qm", "remove")
        git("tag", "-a", "v9.9.9", "-m", f"contact {PLANTED}")
        tree = run(root)
        dirty = subprocess.run([sys.executable, str(root / "build/validate.py"), "--history"], capture_output=True, text=True)
        shallow = pathlib.Path(tmp) / "shallow"
        subprocess.run(["git", "clone", "-q", "--depth", "1", f"file://{root}", str(shallow)], capture_output=True)
        thin = subprocess.run([sys.executable, str(shallow / "build/validate.py"), "--history"], capture_output=True, text=True)
        if clean.returncode != 0:
            failures.append(f"history baseline: a clean history must pass, got:\n{clean.stdout}")
        elif tree.returncode != 0:
            failures.append(f"history: the tree is clean again, so a plain run must pass, got:\n{tree.stdout}")
        elif dirty.returncode == 0 or "docs/note.md" not in dirty.stdout:
            failures.append(f"history: an address added then removed was not caught:\n{dirty.stdout}")
        elif "docs/wide.md" not in dirty.stdout:
            failures.append(f"history: an address in a UTF-16 file was not caught:\n{dirty.stdout}")
        elif "tag " not in dirty.stdout:
            failures.append(f"history: an address in an annotated tag message was not caught:\n{dirty.stdout}")
        elif thin.returncode == 0 or "shallow clone" not in thin.stdout:
            failures.append(f"history: a shallow clone passed instead of being refused:\n{thin.stdout}")
        else:
            print("  ok   history: removed, UTF-16 and tag-message addresses caught, shallow clone refused")

    if failures:
        print(f"\n✘ {len(failures)} gate(s) not proven:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)

    print(f"\n✔ {len(CASES)} gates fire on the defect they were written for")


if __name__ == "__main__":
    main()
