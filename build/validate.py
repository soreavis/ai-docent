#!/usr/bin/env python3
"""Validate every skill against the Agent Skills spec, and every platform
manifest against version.txt.

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

skills = sorted(p for p in SKILLS.iterdir() if p.is_dir())
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

if failures:
    print(f"✘ {len(failures)} failure(s):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)

print(f"✔ v{version} — {len(skills)} skills, {len(MANIFESTS)} manifests in lockstep")
print(f"  skills: {', '.join(s.name for s in skills)}")
