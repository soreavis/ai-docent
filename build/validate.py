#!/usr/bin/env python3
"""Validate every skill against the Agent Skills spec and this repo's conventions.

Run locally with `python3 build/validate.py`; CI runs the same script.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "claude-docent"
NAME_RE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
DESC_MAX = 200  # claude.ai upload cap; the open spec allows 1024

failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)


for manifest in (ROOT / ".claude-plugin/marketplace.json", PLUGIN / ".claude-plugin/plugin.json"):
    try:
        json.loads(manifest.read_text())
    except Exception as exc:
        failures.append(f"{manifest.name}: invalid JSON — {exc}")

skills = sorted(p for p in (PLUGIN / "skills").iterdir() if p.is_dir())
check(skills, "no skills found")

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
    # docs.claude.com is stale; it may only appear as an explicit warning.
    for line in text.splitlines():
        if "docs.claude.com" in line and not re.search(r"never|stale", line, re.I):
            failures.append(f"{skill.name}: cites the stale docs.claude.com domain")
    check(
        "copy everything below" not in text and "don't paste this part" not in text,
        f"{skill.name}: leftover paste-in scaffolding",
    )

if failures:
    print(f"✘ {len(failures)} failure(s):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)

print(f"✔ {len(skills)} skills pass: {', '.join(s.name for s in skills)}")
