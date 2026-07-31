# Changelog

All notable changes to this project are documented here.

This project follows [Keep a Changelog](https://keepachangelog.com/) and [Semantic Versioning](https://semver.org/). Releases are managed by Release Please from Conventional Commits — see [CONTRIBUTING.md](CONTRIBUTING.md#releasing).

## [Unreleased]

### Added

- `start`, a launcher skill: it asks what's going wrong, recommends one course, and can run all eight in order as a single tracked program. It teaches nothing itself and carries `role: launcher`, so it is excluded from the course count.
- Learner-selected tone of voice in every skill — Coach, Blunt, Socratic, Peer, Patient, Formal, or a described custom voice. The choice is recorded on the Progress Card and survives between sessions.
- Two further anti-hallucination guardrails in every GROUND RULES block: never state a figure you did not look up, and tone never changes what is true. Both are gated by `build/validate.py`, as is the tone reference's delivery-not-content floor.
- A CI gate on prose counts, so a manifest or the README claiming "eight courses" fails if the number of courses changes.
- A new `long-haul` lesson, 4.4 The practice retrospective: reviewing your own habits rather than the work, using the running logs the courses already keep as the evidence. It names the distinction that matters — a ritual genuinely no longer needed versus one abandoned because it was tedious.
- A contribution policy: what lands fast (corrections with a source, platform lanes, validator gates), what needs an issue first (courses, levels, anything touching a guardrail), and what will be declined. AI-assisted contributions are welcome with disclosure and the same standard the `shipping` course teaches; fully automated pull requests are closed unreviewed.
- A Course Correction issue template that requires a source, and a pull-request template with an AI-disclosure section. CI now fails if the templates don't offer every skill.
- Every skill handles the card edge cases explicitly — several cards pasted at once, an unrecognised card version, a lesson the curriculum doesn't have, a future date, a disputed judgement, skipping ahead, two courses in one conversation — rather than guessing.
- Wizard question counts are now precise and enforced: each states its core questions, how many branch questions exist, and a hard ceiling, and CI fails if any of those disagree with the questions actually written.
- Courses now seed the companion as they go: each Progress Card carries a `Review seeds` line written at the end of a lesson, and courses point at `/ai-docent:companion` at the five-session retro and on completion — not after every lesson. The companion inherits name, tone and Game Mode from the newest card rather than re-asking what a course already established.
- `companion`, a support skill that keeps learned material from fading: it builds a review queue from every course card it can read, drills what's due on a widening 1-day/3-day/1-week/3-week ladder, spots which habits have gone quiet across courses, and has a five-minute mode. It never teaches new material — a drill that exposes a gap routes to the course that owns it.
- Cards are now validated on read instead of trusted on sight: the course checks the marker's `course=`, refuses to resume from another course's card, names missing fields rather than inferring them, and asks which to use when a file is further along than a pasted card.
- A cold-start rebuild path — three questions reconstruct a card instead of restarting onboarding — plus a mid-session `save` on request, so an interrupted session doesn't lose everything.
- Every skill now guards against acting on the learner's system unasked. All five are gated by `build/validate.py`.
- Course content is now year-free and gated: `build/validate.py` fails if any file under `skills/` pins a calendar year, and Progress Cards take the date from the environment or the learner rather than from the model's memory.
- Progress Cards now carry `<!-- ai-docent:card v1 course=… -->` markers, a `Storage:` line recording which lane saved them, and an instruction to print them fenced so chat surfaces offer one-click copy. All three are gated.

## [0.1.0] - 2026-07-24

### Added

- Eight multi-session tutor courses as Agent Skills: `foundations`, `prompt-craft`, `reliability`, `shipping`, `long-haul`, `security`, `mechanics`, `builder`.
- Install lanes for Claude Code, Codex, Cursor, Gemini CLI, Copilot/GitHub CLI, Grok, Claude web/Desktop/Cowork, and the generic `.agents/` convention, plus standalone skill zips for runtimes without a marketplace.
- File-based Progress Cards at `~/.ai-docent/progress-<course>.md`, with a pasted-card fallback where there is no filesystem.
- `version.txt` as the single source of truth, kept in lockstep across every manifest by Release Please and enforced by CI.
- Anti-hallucination guardrails in every course — a tool guard, an uncertainty rule, a never-construct-a-URL rule, and enumerated documentation domains, all inside the truncation-resilient GROUND RULES block and gated by `build/validate.py`.
