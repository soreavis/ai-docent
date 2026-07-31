# Changelog

All notable changes to this project are documented here.

This project follows [Keep a Changelog](https://keepachangelog.com/) and [Semantic Versioning](https://semver.org/). Releases are managed by Release Please from Conventional Commits — see [CONTRIBUTING.md](CONTRIBUTING.md#releasing).

## [Unreleased]

### Added

- `start`, a launcher skill: it asks what's going wrong, recommends one course, and can run all eight in order as a single tracked program. It teaches nothing itself and carries `role: launcher`, so it is excluded from the course count.
- Learner-selected tone of voice in every skill — Coach, Blunt, Socratic, Peer, Patient, Formal, or a described custom voice. The choice is recorded on the Progress Card and survives between sessions.
- Two further anti-hallucination guardrails in every GROUND RULES block: never state a figure you did not look up, and tone never changes what is true. Both are gated by `build/validate.py`, as is the tone reference's delivery-not-content floor.
- A CI gate on prose counts, so a manifest or the README claiming "eight courses" fails if the number of courses changes.
- Course content is now year-free and gated: `build/validate.py` fails if any file under `skills/` pins a calendar year, and Progress Cards take the date from the environment or the learner rather than from the model's memory.
- Progress Cards now carry `<!-- ai-docent:card v1 course=… -->` markers, a `Storage:` line recording which lane saved them, and an instruction to print them fenced so chat surfaces offer one-click copy. All three are gated.

## [0.1.0] - 2026-07-24

### Added

- Eight multi-session tutor courses as Agent Skills: `foundations`, `prompt-craft`, `reliability`, `shipping`, `long-haul`, `security`, `mechanics`, `builder`.
- Install lanes for Claude Code, Codex, Cursor, Gemini CLI, Copilot/GitHub CLI, Grok, Claude web/Desktop/Cowork, and the generic `.agents/` convention, plus standalone skill zips for runtimes without a marketplace.
- File-based Progress Cards at `~/.ai-docent/progress-<course>.md`, with a pasted-card fallback where there is no filesystem.
- `version.txt` as the single source of truth, kept in lockstep across every manifest by Release Please and enforced by CI.
- Anti-hallucination guardrails in every course — a tool guard, an uncertainty rule, a never-construct-a-URL rule, and enumerated documentation domains, all inside the truncation-resilient GROUND RULES block and gated by `build/validate.py`.
