# Changelog

All notable changes to this project are documented here.

This project follows [Keep a Changelog](https://keepachangelog.com/) and [Semantic Versioning](https://semver.org/). Releases are managed by [Release Please](https://github.com/googleapis/release-please) from Conventional Commits — see [CONTRIBUTING.md](CONTRIBUTING.md#releasing).

## [0.2.2](https://github.com/soreavis/ai-docent/compare/v0.2.1...v0.2.2) (2026-09-15)


### Bug Fixes

* correct stale versions, counts and dead links across the docs ([42689d2](https://github.com/soreavis/ai-docent/commit/42689d2cd8d224d1b396ae5390884f07820709c3))
* skip local venvs in the hygiene scan and document gemini --consent ([c5d65b9](https://github.com/soreavis/ai-docent/commit/c5d65b9233f5fd3a406e9993977dad134ab740a2))

## [0.2.1](https://github.com/soreavis/ai-docent/compare/v0.2.0...v0.2.1) (2026-08-08)


### Bug Fixes

* hold the ten copies of tone.md identical ([e3e250a](https://github.com/soreavis/ai-docent/commit/e3e250ad8a3266397ddc1abf161604cb2533960a))


### Documentation

* `docs/example-prompts.md` — copyable starting points for people who have just started: the four parts most beginner prompts leave out, the ask-me-questions-first opener, everyday prompts by task, the ones that make an answer checkable, and how to steer a bad answer instead of restarting. It teaches nothing `prompt-craft` doesn't cover in full; it exists so day one doesn't require a course. Listed in `docs/README.md`, and a gate now fails the build if any guide is missing from that index. ([8cf7adb](https://github.com/soreavis/ai-docent/commit/8cf7adb46524a2026c80272db06303d41a31594e))
* every conduct and security report now routes through GitHub rather than a published address ([cdbabe5](https://github.com/soreavis/ai-docent/commit/cdbabe54dfe73d6e0cf6eed3286ab9fa95abaf22)), and the validator gates secrets and personal data before they can be pushed ([67c964b](https://github.com/soreavis/ai-docent/commit/67c964b98c8093cfbc86c8d529920571f13c235e))

## [0.2.0](https://github.com/soreavis/ai-docent/compare/v0.1.0...v0.2.0) (2026-08-05)


### Features

* add long-haul 4.4, the practice retrospective ([150f15d](https://github.com/soreavis/ai-docent/commit/150f15d3e73b5cd020100612e4e1bf63898da190))
* add the companion, a revision skill across every course ([a1514f9](https://github.com/soreavis/ai-docent/commit/a1514f98c7d4fb15f08a4f193dc6200697048d24))
* add the start launcher, learner-chosen tone, and user docs ([a16cd41](https://github.com/soreavis/ai-docent/commit/a16cd41fe99b3761d88b0b2429fb951ce8f77940))
* make Progress Cards recognisable and self-describing ([fd0c616](https://github.com/soreavis/ai-docent/commit/fd0c6167a11eeaa7570c2ff562b1ca65689f89bb))
* seed the companion from courses, and make the wizards precise ([6963ea8](https://github.com/soreavis/ai-docent/commit/6963ea879862a193657da8f6623cc928f9336c54))
* set a contribution policy before the repo goes public ([ca4f2fc](https://github.com/soreavis/ai-docent/commit/ca4f2fcef0afff0464c7d21bbe7b19000f21e294))
* validate Progress Cards instead of trusting them ([fe51ca9](https://github.com/soreavis/ai-docent/commit/fe51ca95675fa9252040fdbbeee0b79e00700074))

In detail:

* `start`, a launcher skill: it asks what's going wrong, recommends one course, and can run all eight in order as a single tracked program. It teaches nothing itself and carries `role: launcher`, so it is excluded from the course count.
* Learner-selected tone of voice in every skill — Coach, Blunt, Socratic, Peer, Patient, Formal, or a described custom voice. The choice is recorded on the Progress Card and survives between sessions.
* Two further anti-hallucination guardrails in every GROUND RULES block: never state a figure you did not look up, and tone never changes what is true. Both are gated by `build/validate.py`, as is the tone reference's delivery-not-content floor.
* A CI gate on prose counts, so a manifest or the README claiming "eight courses" fails if the number of courses changes.
* A new `long-haul` lesson, 4.4 The practice retrospective: reviewing your own habits rather than the work, using the running logs the courses already keep as the evidence. It names the distinction that matters — a ritual genuinely no longer needed versus one abandoned because it was tedious.
* A contribution policy: what lands fast (corrections with a source, platform lanes, validator gates), what needs an issue first (courses, levels, anything touching a guardrail), and what will be declined. AI-assisted contributions are welcome with disclosure and the same standard the `shipping` course teaches; fully automated pull requests are closed unreviewed.
* A Course Correction issue template that requires a source, and a pull-request template with an AI-disclosure section. CI now fails if the templates don't offer every skill.
* Every skill handles the card edge cases explicitly — several cards pasted at once, an unrecognised card version, a lesson the curriculum doesn't have, a future date, a disputed judgement, skipping ahead, two courses in one conversation — rather than guessing.
* Wizard question counts are now precise and enforced: each states its core questions, how many branch questions exist, and a hard ceiling, and CI fails if any of those disagree with the questions actually written.
* Courses now seed the companion as they go: each Progress Card carries a `Review seeds` line written at the end of a lesson, and courses point at `/ai-docent:companion` at the five-session retro and on completion — not after every lesson. The companion inherits name, tone and Game Mode from the newest card rather than re-asking what a course already established.
* `companion`, a support skill that keeps learned material from fading: it builds a review queue from every course card it can read, drills what's due on a widening 1-day/3-day/1-week/3-week ladder, spots which habits have gone quiet across courses, and has a five-minute mode. It never teaches new material — a drill that exposes a gap routes to the course that owns it.
* Cards are now validated on read instead of trusted on sight: the course checks the marker's `course=`, refuses to resume from another course's card, names missing fields rather than inferring them, and asks which to use when a file is further along than a pasted card.
* A cold-start rebuild path — three questions reconstruct a card instead of restarting onboarding — plus a mid-session `save` on request, so an interrupted session doesn't lose everything.
* Every skill now guards against acting on the learner's system unasked. All of them are gated by `build/validate.py`.
* Course content is now year-free and gated: `build/validate.py` fails if any file under `skills/` pins a calendar year, and Progress Cards take the date from the environment or the learner rather than from the model's memory.
* Progress Cards now carry `<!-- ai-docent:card v1 course=… -->` markers, a `Storage:` line recording which lane saved them, and an instruction to print them fenced so chat surfaces offer one-click copy. All three are gated.


### Bug Fixes

* **ci:** derive current version in the README-badge negative test ([82550d7](https://github.com/soreavis/ai-docent/commit/82550d75755f5ca7ce448fa0aced2acc9da78588))
* close a fabrication gap in the reliability planted-error rule ([dfa9bb8](https://github.com/soreavis/ai-docent/commit/dfa9bb82a0806c0d96bf5c90589d34bb73e0d539))
* correct the stale course count in every manifest ([0f5ac62](https://github.com/soreavis/ai-docent/commit/0f5ac620054c531d7c72b70756e0909442904dc9))
* correct what a deep audit of every Markdown file found ([bffde81](https://github.com/soreavis/ai-docent/commit/bffde81c4f0306160241a198d025d25a193a4110))
* credit the lethal trifecta, and correct a stale validator comment ([28ef104](https://github.com/soreavis/ai-docent/commit/28ef1045522bef69c7814122b4e55a4b08a672f1))
* drop an unsourced trend claim and de-collide the card marker ([d145ca3](https://github.com/soreavis/ai-docent/commit/d145ca3c8b10fee470b131a443d6c59d2187e864))
* harden CI supply chain, manifests, and the build validator ([3e81120](https://github.com/soreavis/ai-docent/commit/3e811204b9c100a0438b9577dfcfa559a5ce41b7))
* harden frontmatter validation against silent YAML hazards ([f51e2d3](https://github.com/soreavis/ai-docent/commit/f51e2d3fb1b5857d9790c8b040cb41455f6c7d1d))
* keep the README version badge in lockstep ([b455b2f](https://github.com/soreavis/ai-docent/commit/b455b2f70a00ff0854e51db8567d7f922f426459))
* load companion's game-mode.md, and gate orphaned references ([7d64114](https://github.com/soreavis/ai-docent/commit/7d64114c6f07cb47458304393cc54085fea9a7ef))
* make the courses survive a year change ([ab93187](https://github.com/soreavis/ai-docent/commit/ab931878b7a03445a4ae1c48b27338f0640b1977))
* **readme:** use object form for enabledPlugins ([3519004](https://github.com/soreavis/ai-docent/commit/351900464f6e506f6e2b4405380e74e75b21c00a))
* six skills had frontmatter that did not parse as YAML ([1371513](https://github.com/soreavis/ai-docent/commit/1371513abd030f632acc92c051069f510df4b174))
* use the shields static/v1 form for the version badge ([ca7d40d](https://github.com/soreavis/ai-docent/commit/ca7d40d0f8240c132fd03db8ba2134fff12075c2))
* validate the plugin, not just the marketplace manifest ([4f60791](https://github.com/soreavis/ai-docent/commit/4f60791b73287711a50edc5afcc065f26f19fa3d))

In detail:

* **The validator had 75 assertions and nothing testing any of them.** `build/test_validate.py` now copies the repo, breaks one thing, and asserts the gate fires with the message that names it — 22 cases, run in CI. Writing it immediately caught two mistakes in its own fixtures, one of which (a link replaced once where the file mentions it twice) would have made a passing test prove nothing. ([4e58bea](https://github.com/soreavis/ai-docent/commit/4e58bea8aae4ae5c3415929f7dd4bb3ceb32527b))
* **`companion` never loaded its own `game-mode.md`.** The file exists and is written for revision — XP for items held and retired, a ladder counted by items retired rather than by lessons cleared — but no line of the skill ever read it, while the Progress Card still asked for `Rank: [rank] ([xp] XP · next at [n])`. With the bands unreachable the only options were to invent a rank or borrow the courses' ladder, which counts something else; either way the made-up number persisted to the save file. `build/validate.py` now checks the reference contract in both directions, so a file nothing loads fails the build.
* The README's level column is recounted against the `## LEVEL n` headings in each curriculum. Nothing previously held the two together, so adding a level would have quietly left the table wrong.
* The **lethal trifecta** is now credited to Simon Willison where `security` teaches it. Teaching a coined framing without attribution is the habit this project spends a whole course arguing against.
* `CLAUDE.md` moved to `.claude/CLAUDE.md` and now uses the documented `@AGENTS.md` import rather than a prose link, which only suggested the file. At the repo root it also sat at the plugin root, where installed plugins never load it — `claude plugin validate --strict` flagged it.
* Frontmatter is now checked for the hazards a YAML parser accepts silently: duplicate keys (only the last survives), tabs in indentation, and a missing opening `---`.
* **Six of ten skills had frontmatter that did not parse as YAML.** An unquoted `": "` inside the `description` field broke the mapping, and the runtime drops *all* metadata when that happens — those skills would have installed with no name and no description, undiscoverable and uninvocable. Found by `claude plugin validate --strict`; `build/validate.py` missed it because it read the frontmatter with a regex. It now parses the YAML properly, and CI installs PyYAML so the strong check always runs.
* The guardrail block told every course that `docs.claude.com` is stale. It isn't — it 301s to the current documentation. The rule (cite the canonical domain) stands; the false reason is gone.
* Two invented statistics removed: `shipping` claimed a technique "prevents half of all review round-trips", and `mechanics` asserted "most learners finish in 5–8 sessions" and instructed the tutor to say so — a population figure this project cannot have.
* Every course rank ladder now carries XP bands. The Progress Card asks for `next at [n]`, and without bands that number was underivable, so it was invented and then persisted to the save file each session.
* `mechanics` had no retro, yet instructed the tutor to mention the companion "at the ~5-session retro". Both the retro and a gate for it now exist.
* The enumerated-doc-domains guardrail was checked against the whole file rather than the GROUND RULES block, so `SECURITY.md`'s claim that relocating a guardrail is caught was false for that one rule.
* Corrected counts: seven guardrails not six (`AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`), two support skills not three (`docs/README.md`), eight branch questions not seven (`long-haul`), skill files 15–20 KB not 12–15 KB (`README.md`).

## [0.1.0](https://github.com/soreavis/ai-docent/releases/tag/v0.1.0) (2026-07-24)

### Added

- Eight multi-session tutor courses as Agent Skills: `foundations`, `prompt-craft`, `reliability`, `shipping`, `long-haul`, `security`, `mechanics`, `builder`.
- Install lanes for Claude Code, Codex, Cursor, Gemini CLI, Copilot/GitHub CLI, Grok, Claude web/Desktop/Cowork, and the generic `.agents/` convention, plus standalone skill zips for runtimes without a marketplace.
- File-based Progress Cards at `~/.ai-docent/progress-<course>.md`, with a pasted-card fallback where there is no filesystem.
- `version.txt` as the single source of truth, kept in lockstep across every manifest by Release Please and enforced by CI.
- Anti-hallucination guardrails in every course — a tool guard, an uncertainty rule, a never-construct-a-URL rule, and enumerated documentation domains, all inside the truncation-resilient GROUND RULES block and gated by `build/validate.py`.
