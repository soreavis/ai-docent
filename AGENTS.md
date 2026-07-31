# AGENTS.md

Guidance for AI agents working **on this repository**. (If you are looking for the courses themselves, they are the skills in `skills/` — this file is about maintaining them.)

## What this repo is

`ai-docent` packages eight multi-session tutor courses as [Agent Skills](https://agentskills.io), distributed to every agent platform that can install a skill or plugin. One skill tree, many thin manifests.

The courses run in any agent. The curriculum currently uses Claude as its worked platform, so lesson text names Claude surfaces and doc domains — that is subject matter, not a packaging constraint.

```
skills/<course>/SKILL.md        the course; loads in full when invoked
skills/<course>/references/     curriculum + game mode; load on demand
version.txt                     single source of truth for the version
.claude-plugin/  .codex-plugin/  .cursor-plugin/  .grok-plugin/
.agents/plugins/  gemini-extension.json
```

## Rules

- **Never edit a version by hand.** `version.txt` is the source of truth and Release Please rewrites every manifest and every SKILL.md frontmatter from it. Editing one manifest alone breaks lockstep and CI fails.
- **Run `python3 build/validate.py` before you commit.** It checks the Agent Skills spec, this repo's course conventions, and version lockstep across all eight manifests and the README badge.
- **`description` must stay ≤200 characters.** The open spec allows 1024, but the strictest uploader (claude.ai) is stricter, and the same file ships to both.
- **Keep `SKILL.md` under 500 lines.** Detail belongs in `references/`, which loads only when read.
- **A skill's folder name must equal its frontmatter `name`.** Uploads are rejected otherwise.
- **`allowed-tools` is deliberately omitted.** Not an oversight. The field is marked experimental in the Agent Skills spec and its support varies by runtime, while every course's accuracy rule depends on web search — a wrong or incomplete allowlist would silently disable the primary anti-hallucination guardrail on some hosts. Revisit only when the field is stable across the runtimes in the README install table, and if you add it, name the web-search tool for every one of them.

## Course conventions — these are deliberate, keep them

- **No hardcoded prices, usage limits, or model IDs.** Route every changeable number to live docs. A well-formed but stale figure is a hallucination.
- **Doc domains:** `code.claude.com/docs`, `platform.claude.com/docs`, `support.claude.com`, `claude.com/pricing`. Never `docs.claude.com` — it redirects and is stale.
- **Game Mode scoring stays honest.** XP is recomputed from logged events each session, never carried as a remembered total.
- **`reliability` keeps its planted-error protocol.** Every deliberately planted fabrication is tracked in an explicit list and revealed before the session ends. Unrevealed items carry into the Progress Card.
- **`security` keeps its describe-don't-perform protocol.** Attacks are inert, fenced, labeled, and neutralized before the exercise closes. Never executed.
- **No personal, employer, or client names** anywhere in the courses.
- **Six guardrails must live inside the GROUND RULES block of every skill** — the tool guard, the uncertainty rule, the never-construct-a-URL rule, enumerated doc domains, the never-state-an-unlooked-up-figure rule, and the rule that tone never changes what is true. They sit there rather than lower down so a truncated paste still carries them. `build/validate.py` fails the build if any is missing; see the 2026-07-24 hallucination audit for why each exists.
- **Tone is delivery, never content.** Every skill offers the learner a voice and carries `references/tone.md`. The voice may change register, warmth and length; it may never change a fact, a hedge, or whether something got verified. If you add a voice, it inherits that floor — and the Progress Card must keep carrying the choice, or it silently resets each session.
- **Support skills are not courses.** Any skill carrying a `role:` in its metadata is excluded from the course count by `validate.py`, so prose saying "eight courses" stays true. There are two: `start` (`role: launcher`) routes people and sequences the full track, and `companion` (`role: companion`) drills material back from the other cards. Neither teaches new material — if you find yourself writing a lesson into one, it belongs in a course.

## Cross-references

Courses point at each other with `/ai-docent:<course>`. If you rename a course, update every sibling that references it — `grep -rn "/ai-docent:" skills/`.

## Adding a platform lane

Add a manifest under the platform's convention, register its version path in both `release-please-config.json` (`extra-files`) and `MANIFESTS` in `build/validate.py`, then document the install command in the README table. The manifest is thin: name, version, description, and a `"skills": "./skills"` pointer where the platform supports one.
