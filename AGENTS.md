# AGENTS.md

Guidance for AI agents working **on this repository**. (If you are looking for the courses themselves, they are the skills in `skills/` — this file is about maintaining them.)

## What this repo is

`ai-docent` packages six multi-session tutor courses as [Agent Skills](https://agentskills.io), distributed to every agent platform that can install a skill or plugin. One skill tree, many thin manifests.

```
skills/<course>/SKILL.md        the course; loads in full when invoked
skills/<course>/references/     curriculum + game mode; load on demand
version.txt                     single source of truth for the version
.claude-plugin/  .codex-plugin/  .cursor-plugin/  .grok-plugin/
.agents/plugins/  gemini-extension.json
```

## Rules

- **Never edit a version by hand.** `version.txt` is the source of truth and Release Please rewrites every manifest and every SKILL.md frontmatter from it. Editing one manifest alone breaks lockstep and CI fails.
- **Run `python3 build/validate.py` before you commit.** It checks the Agent Skills spec, this repo's course conventions, and version lockstep across all eight manifests.
- **`description` must stay ≤200 characters.** The open spec allows 1024, but the claude.ai uploader is stricter, and the same file ships to both.
- **Keep `SKILL.md` under 500 lines.** Detail belongs in `references/`, which loads only when read.
- **A skill's folder name must equal its frontmatter `name`.** Uploads are rejected otherwise.

## Course conventions — these are deliberate, keep them

- **No hardcoded prices, usage limits, or model IDs.** Route every changeable number to live docs. A well-formed but stale figure is a hallucination.
- **Doc domains:** `code.claude.com/docs`, `platform.claude.com/docs`, `support.claude.com`, `claude.com/pricing`. Never `docs.claude.com` — it redirects and is stale.
- **Game Mode scoring stays honest.** XP is recomputed from logged events each session, never carried as a remembered total.
- **`reliability` keeps its planted-error protocol.** Every deliberately planted fabrication is tracked in an explicit list and revealed before the session ends. Unrevealed items carry into the Progress Card.
- **`security` keeps its describe-don't-perform protocol.** Attacks are inert, fenced, labeled, and neutralized before the exercise closes. Never executed.
- **No personal, employer, or client names** anywhere in the courses.

## Cross-references

Courses point at each other with `/ai-docent:<course>`. If you rename a course, update every sibling that references it — `grep -rn "/ai-docent:" skills/`.

## Adding a platform lane

Add a manifest under the platform's convention, register its version path in both `release-please-config.json` (`extra-files`) and `MANIFESTS` in `build/validate.py`, then document the install command in the README table. The manifest is thin: name, version, description, and a `"skills": "./skills"` pointer where the platform supports one.
