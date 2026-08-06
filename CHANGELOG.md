# Changelog

All notable changes to this project are documented here.

This project follows [Keep a Changelog](https://keepachangelog.com/) and [Semantic Versioning](https://semver.org/). Releases are managed by [Release Please](https://github.com/googleapis/release-please) from Conventional Commits — see [CONTRIBUTING.md](CONTRIBUTING.md#releasing).

## [0.2.0](https://github.com/soreavis/ai-docent/compare/v0.1.0...v0.2.0) (2026-08-05)


### Features

* add long-haul 4.4, the practice retrospective ([32a7b0e](https://github.com/soreavis/ai-docent/commit/32a7b0edb50dce001bc8598da089e49d3febe26e))
* add the companion, a revision skill across every course ([0b75f29](https://github.com/soreavis/ai-docent/commit/0b75f2960270b97e21b75995cb57834f62468587))
* add the start launcher, learner-chosen tone, and user docs ([2226b01](https://github.com/soreavis/ai-docent/commit/2226b019f9f2f77ebe9e54d7f489e7d69a42f1f9))
* make Progress Cards recognisable and self-describing ([9cd7ab2](https://github.com/soreavis/ai-docent/commit/9cd7ab2ca579e98871d695eeb3f6c5d2ccf0b659))
* seed the companion from courses, and make the wizards precise ([df8c481](https://github.com/soreavis/ai-docent/commit/df8c481ee18986c87c1e7af25a57a00925ac32ff))
* set a contribution policy before the repo goes public ([ba144a8](https://github.com/soreavis/ai-docent/commit/ba144a86b04eb40fd1ed97c7039c3c38797838f7))
* validate Progress Cards instead of trusting them ([cc1b399](https://github.com/soreavis/ai-docent/commit/cc1b3995ba5458c04bad12191f3b78713cd1aed6))


### Bug Fixes

* **ci:** derive current version in the README-badge negative test ([#10](https://github.com/soreavis/ai-docent/issues/10)) ([82251ec](https://github.com/soreavis/ai-docent/commit/82251ecefcbf26d1ce9544af1f71b3055a8c70b5))
* close a fabrication gap in the reliability planted-error rule ([6e4e51e](https://github.com/soreavis/ai-docent/commit/6e4e51ee40e4b40a26e296640c50793ccb6c78b9))
* correct the stale course count in every manifest ([cb0d5f8](https://github.com/soreavis/ai-docent/commit/cb0d5f8637f8c0b9e4801eb89f0c6bb850467103))
* correct what a deep audit of every Markdown file found ([8c433f4](https://github.com/soreavis/ai-docent/commit/8c433f4e1e098b5abd20060175f9f7f14c54c708))
* credit the lethal trifecta, and correct a stale validator comment ([dc97228](https://github.com/soreavis/ai-docent/commit/dc972286723b4639a49470034eac29f2686ca095))
* drop an unsourced trend claim and de-collide the card marker ([e1f499b](https://github.com/soreavis/ai-docent/commit/e1f499b63e52ff9de2633e8aa2f1327365601ae4))
* harden CI supply chain, manifests, and the build validator ([fb87596](https://github.com/soreavis/ai-docent/commit/fb875967857024670a273af9380773a3f71458e9))
* harden frontmatter validation against silent YAML hazards ([dc53d5c](https://github.com/soreavis/ai-docent/commit/dc53d5cc0c8f2fa5726fe050c20f00e32e06a9cb))
* keep the README version badge in lockstep ([f6b9bac](https://github.com/soreavis/ai-docent/commit/f6b9bac84916620a339b3b14e932cadb843ff760))
* load companion's game-mode.md, and gate orphaned references ([16916b9](https://github.com/soreavis/ai-docent/commit/16916b909d0e0d4b08e692061a41c71372fcc58c))
* make the courses survive a year change ([63f7089](https://github.com/soreavis/ai-docent/commit/63f7089f04128a533f411f7c8b553e837ef58bde))
* **readme:** use object form for enabledPlugins ([#9](https://github.com/soreavis/ai-docent/issues/9)) ([6b919c0](https://github.com/soreavis/ai-docent/commit/6b919c0f2b6be75d4ed69f2a867dac932d1dbc67))
* six skills had frontmatter that did not parse as YAML ([4c9cd87](https://github.com/soreavis/ai-docent/commit/4c9cd87c9b528961c51852393a21b16041ba6119))
* use the shields static/v1 form for the version badge ([0ddc2a3](https://github.com/soreavis/ai-docent/commit/0ddc2a3f8f66448d9bcbe8bb1ad480f2756a93b7))
* validate the plugin, not just the marketplace manifest ([71266da](https://github.com/soreavis/ai-docent/commit/71266daeab165ae315c0bb0134afd0d455653723))

## [Unreleased]

### Fixed

- **The validator had 75 assertions and nothing testing any of them.** `build/test_validate.py` now copies the repo, breaks one thing, and asserts the gate fires with the message that names it — 13 cases, run in CI. Writing it immediately caught two mistakes in its own fixtures, one of which (a link replaced once where the file mentions it twice) would have made a passing test prove nothing.
- **`companion` never loaded its own `game-mode.md`.** The file exists and is written for revision — XP for items held and retired, a ladder counted by items retired rather than by lessons cleared — but no line of the skill ever read it, while the Progress Card still asked for `Rank: [rank] ([xp] XP · next at [n])`. With the bands unreachable the only options were to invent a rank or borrow the courses' ladder, which counts something else; either way the made-up number persisted to the save file. `build/validate.py` now checks the reference contract in both directions, so a file nothing loads fails the build.
- The README's level column is recounted against the `## LEVEL n` headings in each curriculum. Nothing previously held the two together, so adding a level would have quietly left the table wrong.
- The **lethal trifecta** is now credited to Simon Willison where `security` teaches it. Teaching a coined framing without attribution is the habit this project spends a whole course arguing against.
- `CLAUDE.md` moved to `.claude/CLAUDE.md` and now uses the documented `@AGENTS.md` import rather than a prose link, which only suggested the file. At the repo root it also sat at the plugin root, where installed plugins never load it — `claude plugin validate --strict` flagged it.
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
