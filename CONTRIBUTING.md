# Contributing

Contributions are welcome. If an AI agent is doing the work, point it at [AGENTS.md](AGENTS.md).

## Getting started

```bash
git clone git@github.com:soreavis/ai-docent.git
cd ai-docent
claude --plugin-dir .        # the repo root is the plugin
```

Run `/reload-plugins` after edits to pick them up without restarting.

## Validating

```bash
python3 build/validate.py    # spec, conventions, and version lockstep — the same script CI runs
claude plugin validate .     # Claude Code manifest check
```

`build/validate.py` enforces:

- folder name matches the SKILL.md `name`, lowercase-kebab, ≤64 chars
- `description` ≤200 characters (the claude.ai upload cap, stricter than the open spec's 1024)
- SKILL.md under 500 lines, with detail in `references/`
- every `references/` link resolves
- the name-first wizard question, `disable-model-invocation: true`, a file-based progress card, and the Game Mode scoring-honesty rule are all present
- no `docs.claude.com` citations and no leftover paste-in scaffolding
- the four anti-hallucination guardrails are present **inside** each course's GROUND RULES block: the tool guard, the uncertainty rule, the never-construct-a-URL rule, and enumerated doc domains
- **every one of the eight platform manifests carries the same version as `version.txt`**

## Course conventions

These are deliberate. Keep them.

- **No hardcoded prices, usage limits, or model IDs.** Route every changeable number to live docs. A well-formed but stale figure is a hallucination.
- **Doc domains:** `code.claude.com/docs`, `platform.claude.com/docs`, `support.claude.com`, `claude.com/pricing`. Never `docs.claude.com`.
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

**Never edit a version by hand.** `version.txt` is the source of truth, and Release Please rewrites it plus all eight platform manifests and all six SKILL.md frontmatter blocks together. Editing one alone breaks lockstep and CI fails.

The flow:

1. Merge conventional commits to `main`
2. Release Please opens a release PR with the version bump and CHANGELOG entry
3. Merge that PR — it tags the release and publishes it
4. Publishing triggers `.github/workflows/release.yml`, which validates, builds the per-course zips, and attaches them to the release

`feat:` bumps the minor, `fix:` the patch, and `feat!:` or a `BREAKING CHANGE:` footer the major.

Installed users on the plugin lanes only receive an update when the version changes — a commit alone does nothing for them.

## Adding a platform lane

1. Add the manifest under the platform's convention (see the existing `.codex-plugin/`, `.cursor-plugin/`, `.grok-plugin/` for the shape — thin: name, version, description, and a `"skills": "./skills"` pointer where supported)
2. Register its version path in `release-please-config.json` under `extra-files`
3. Add it to `MANIFESTS` in `build/validate.py` so lockstep is enforced
4. Document the install and update commands in the README table
