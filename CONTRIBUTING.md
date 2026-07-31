# Contributing

Contributions are welcome. If an AI agent is doing the work, point it at [AGENTS.md](AGENTS.md).

This is maintained by one person, so review is the bottleneck rather than ideas. The sections below say what lands quickly, what needs a conversation first, and what will be declined — so you don't spend an evening on something that was never going to merge.

## What's most useful

**Corrections, above everything else.** A course stating something wrong, stale, or unsupported is a defect, and a stranger who hits one is better placed to catch it than the maintainer who wrote it. Open a [Course Correction](../../issues/new?template=course_correction.yml) issue with a source. These get fixed fastest of anything here.

**New platform lanes.** A runtime that reads Agent Skills and isn't in the README table yet. Small, testable, obviously valuable — see [Adding a platform lane](#adding-a-platform-lane).

**Validator improvements.** `build/validate.py` is where this project's conventions are actually enforced. A new gate that catches a real class of mistake is worth more than a fix for one instance of it.

**Typos, broken links, dead commands.** Straight to a PR, no issue needed.

## What needs an issue first

**A new course.** Nobody should write a 500-line `SKILL.md` speculatively. Open a Feature Request with the gap it fills, evidence that people actually hit it, and a sketch of its levels. A course that arrives as a surprise pull request will probably be declined however good it is, and that's a bad outcome for both of us.

**A new level, or restructuring an existing course.** Same reasoning, smaller scale.

**Anything touching the guardrails.** The GROUND RULES blocks, the planted-error protocol in `reliability`, the describe-don't-perform protocol in `security`. These look like ordinary prose and are load-bearing.

## What will be declined

- **Rewriting lesson prose for style.** Eight courses in one voice is a feature. Style preferences are not defects.
- **Changing the tone options** or how a course sounds, without a specific problem it solves.
- **Adding a figure, price, limit, or model ID** to course text. Those route to live documentation on purpose.
- **Bulk changes** — a hundred files touched, or a PR that does three unrelated things. Split it.

## Using AI to contribute

Use an agent if you want. This project exists to teach people to do that well, and a policy forbidding it would be both hypocritical and unenforceable.

What matters is the same standard the `shipping` course teaches:

- **You have read every line and can explain any of it.** "The agent did it" is not an answer to a review comment.
- **It is scoped small enough to review in one sitting.** Generating is cheap and reviewing is expensive, and that cost lands on someone else.
- **Every product fact is verified against current docs, with the source in the PR.** Not "the model said so."
- **You disclose it** in the pull request template. Honestly. It changes how a PR is read, not whether it's welcome — and an undisclosed generated PR that turns out to be generated gets closed.

Fully automated pull requests — opened by a bot, or by someone who has not read the diff — will be closed without review.

## Getting started

```bash
git clone git@github.com:soreavis/ai-docent.git
cd ai-docent
claude --plugin-dir .        # the repo root is the plugin
```

Run `/reload-plugins` after edits to pick them up without restarting.

## Validating

```bash
python3 build/validate.py                              # spec, conventions, version lockstep — the same script CI runs
claude plugin validate . --strict                      # the marketplace manifest
claude plugin validate .claude-plugin/plugin.json --strict   # the plugin AND every skill's frontmatter
```

Run all three. `claude plugin validate .` stops at the marketplace manifest and never reaches the skills — pointing it at `plugin.json` is what validates them, and that is how six broken frontmatters went unnoticed.

`build/validate.py` enforces:

- **frontmatter parses as YAML** — an unquoted `": "` in a description silently drops every field at runtime; also no tabs, no duplicate keys, and the file opens with `---`
- folder name matches the SKILL.md `name`, lowercase-kebab, ≤64 chars
- `description` ≤200 characters (the claude.ai upload cap, stricter than the open spec's 1024)
- SKILL.md under 500 lines, with detail in `references/`
- every `references/` link resolves
- the name-first wizard question, `disable-model-invocation: true`, a file-based progress card, and the Game Mode scoring-honesty rule are all present
- no `docs.claude.com` citations and no leftover paste-in scaffolding
- the seven anti-hallucination guardrails are present **inside** each skill's GROUND RULES block: the tool guard, the uncertainty rule, the never-construct-a-URL rule, enumerated doc domains, the never-state-an-unlooked-up-figure rule, the never-act-on-their-system rule, and the rule that tone never overrides any of them
- every skill offers a tone in its wizard, carries `references/tone.md` with the delivery-not-content floor, and records the choice on its Progress Card
- prose counts match reality — a manifest or the README claiming "eight courses" fails if the course count changes (skills carrying a `role:` are support skills and are excluded: `start`, `companion`)
- no file under `skills/` pins a calendar year, and every Progress Card grounds its date rather than guessing
- cards are validated on read: wrong-course, stale and truncated cards are all caught rather than trusted
- every skill carries the edge-case block, a cold-start rebuild, and a mid-session `save`
- courses carry `Review seeds` and point at the companion; wizards state core/branch/ceiling counts that match the questions actually written
- every skill is registered in `release-please-config.json`, so its version bumps with the rest
- the issue templates offer every skill, so a new one can be reported against
- every skill guards against acting on the learner's system unasked, and every rank ladder carries the XP bands that make the Progress Card's `next at` derivable
- **every one of the eight platform manifests, and the README version badge, carries the same version as `version.txt`**

## Course conventions

These are deliberate. Keep them.

- **No hardcoded prices, usage limits, or model IDs.** Route every changeable number to live docs. A well-formed but stale figure is a hallucination.
- **Doc domains:** `code.claude.com/docs`, `platform.claude.com/docs`, `support.claude.com`, `claude.com/pricing`. Never `docs.claude.com` — it redirects to the canonical domain; cite that.
- **Game Mode scoring stays honest.** XP is recomputed from logged events, never carried as a remembered total.
- **`reliability` must keep its planted-error protocol** — every deliberately planted fabrication is tracked and revealed before the session ends.
- **`security` must keep its describe-don't-perform protocol** — attacks are shown as inert, fenced, labeled text and neutralized before the exercise closes. Never executed.
- **No personal, employer, or client names** anywhere in the courses.
- **Cross-references** use `/ai-docent:<course>`. Rename a course and you update every sibling: `grep -rn "/ai-docent:" skills/`.

## Submitting changes

1. Fork the repo
2. Create a branch (`fix/description` or `feat/description`)
3. Make your changes
4. Ensure `python3 build/validate.py` passes
5. Open a pull request with a [Conventional Commits](https://www.conventionalcommits.org/) title — `feat:`, `fix:`, `docs:`, `chore:`. Release Please reads these to decide the next version.

## Releasing

**Never edit a version by hand.** `version.txt` is the source of truth, and Release Please rewrites it plus all eight platform manifests, the README badge, and every SKILL.md frontmatter block together. Editing one alone breaks lockstep and CI fails.

The flow:

1. Merge conventional commits to `main`
2. Release Please opens a release PR with the version bump and CHANGELOG entry
3. Merge that PR — it tags the release and publishes it
4. The same workflow run then builds the per-course zips and attaches them to the release. This lives in `release-please.yml` rather than a separate `release:` trigger because a release created with `GITHUB_TOKEN` does not start another workflow run.

`feat:` bumps the minor, `fix:` the patch, and `feat!:` or a `BREAKING CHANGE:` footer the major.

Installed users on the plugin lanes only receive an update when the version changes — a commit alone does nothing for them.

## Adding a platform lane

1. Add the manifest under the platform's convention (see the existing `.codex-plugin/`, `.cursor-plugin/`, `.grok-plugin/` for the shape — thin: name, version, description, and a `"skills": "./skills"` pointer where supported)
2. Register its version path in `release-please-config.json` under `extra-files`
3. Add it to `MANIFESTS` in `build/validate.py` so lockstep is enforced
4. Document the install and update commands in the README table
