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
IGNORE = shutil.ignore_patterns(".git", "dist", "__pycache__", "*.pyc")


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


CASES = [
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
]


def run(root):
    return subprocess.run(
        [sys.executable, str(root / "build/validate.py")],
        capture_output=True,
        text=True,
    )


def main():
    failures = []

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

    if failures:
        print(f"\n✘ {len(failures)} gate(s) not proven:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)

    print(f"\n✔ {len(CASES)} gates fire on the defect they were written for")


if __name__ == "__main__":
    main()
