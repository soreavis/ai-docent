# Changelog

All notable changes to this project are documented here.

This project follows [Keep a Changelog](https://keepachangelog.com/) and [Semantic Versioning](https://semver.org/). Releases are managed by Release Please from Conventional Commits — see [CONTRIBUTING.md](CONTRIBUTING.md#releasing).

## [Unreleased]

### Fixed

- Frontmatter is now checked for the hazards a YAML parser accepts silently: duplicate keys (only the last survives), tabs in indentation, and a missing opening `---`.
- **Six of ten skills had frontmatter that did not parse as YAML.** An unquoted `": "` inside the `description` field broke the mapping, and the runtime drops *all* metadata when that happens — those skills would have installed with no name and no description, undiscoverable and uninvocable. Found by `claude plugin validate --strict`; `build/validate.py` missed it because it read the frontmatter with a regex. It now parses the YAML properly, and CI installs PyYAML so the strong check always runs.
- The guardrail block told every course that `docs.claude.com` is stale. It isn't — it 301s to the current documentation. The rule (cite the canonical domain) stands; the false reason is gone.
- Two invented statistics removed: `shipping` claimed a technique "prevents half of all review round-trips", and `mechanics` asserted "most learners finish in 5–8 sessions" and instructed the tutor to say so — a population figure this project cannot have.
- Every course rank ladder now carries XP bands. The Progress Card asks for `next at [n]`, and without bands that number was underivable, so it was invented and then persisted to the save file each session.
- `mechanics` had no retro, yet instructed the tutor to mention the companion "at the ~5-session retro". Both the retro and a gate for it now exist.
- The enumerated-doc-domains guardrail was checked against the whole file rather than the GROUND RULES block, so `SECURITY.md`'s claim that relocating a guardrail is caught was false for that one rule.
- Corrected counts: seven guardrails not six (`AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`), two support skills not three (`docs/README.md`), eight branch questions not seven (`long-haul`), skill files 15–20 KB not 12–15 KB (`README.md`).

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
- Every skill now guards against acting on the learner's system unasked. All of them are gated by `build/validate.py`.
- Course content is now year-free and gated: `build/validate.py` fails if any file under `skills/` pins a calendar year, and Progress Cards take the date from the environment or the learner rather than from the model's memory.
- Progress Cards now carry `<!-- ai-docent:card v1 course=… -->` markers, a `Storage:` line recording which lane saved them, and an instruction to print them fenced so chat surfaces offer one-click copy. All three are gated.

## [0.1.0] - 2026-07-24

### Added

- Eight multi-session tutor courses as Agent Skills: `foundations`, `prompt-craft`, `reliability`, `shipping`, `long-haul`, `security`, `mechanics`, `builder`.
- Install lanes for Claude Code, Codex, Cursor, Gemini CLI, Copilot/GitHub CLI, Grok, Claude web/Desktop/Cowork, and the generic `.agents/` convention, plus standalone skill zips for runtimes without a marketplace.
- File-based Progress Cards at `~/.ai-docent/progress-<course>.md`, with a pasted-card fallback where there is no filesystem.
- `version.txt` as the single source of truth, kept in lockstep across every manifest by Release Please and enforced by CI.
- Anti-hallucination guardrails in every course — a tool guard, an uncertainty rule, a never-construct-a-URL rule, and enumerated documentation domains, all inside the truncation-resilient GROUND RULES block and gated by `build/validate.py`.
