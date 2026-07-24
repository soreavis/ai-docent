# Contributing

Contributions are welcome.

## Getting started

```bash
git clone git@github.com:soreavis/claude-docent.git
cd claude-docent
claude --plugin-dir ./plugins/claude-docent
```

Run `/reload-plugins` after edits to pick them up without restarting.

## Validating

```bash
python3 build/validate.py    # spec + repo conventions, same script CI runs
claude plugin validate .     # manifest check, same one the marketplace review runs
```

`build/validate.py` enforces:

- folder name matches the SKILL.md `name`, lowercase-kebab, ≤64 chars
- `description` ≤200 characters (the claude.ai upload cap, stricter than the open spec's 1024)
- SKILL.md under 500 lines, with detail in `references/`
- every `references/` link resolves
- the name-first wizard question, `disable-model-invocation: true`, a file-based progress card, and the Game Mode scoring-honesty rule are all present
- no `docs.claude.com` citations and no leftover paste-in scaffolding

## Course conventions

These are deliberate. Keep them.

- **No hardcoded prices, usage limits, or model IDs.** Route every changeable number to live docs. A well-formed but stale figure is a hallucination.
- **Doc domains:** `code.claude.com/docs`, `platform.claude.com/docs`, `support.claude.com`, `claude.com/pricing`. Never `docs.claude.com`.
- **Game Mode scoring stays honest.** XP is recomputed from logged events, never carried as a remembered total.
- **`reliability` must keep its planted-error protocol** — every deliberately planted fabrication is tracked and revealed before the session ends.
- **`security` must keep its describe-don't-perform protocol** — attacks are shown as inert, fenced, labeled text and neutralized before the exercise closes. Never executed.
- **No personal, employer, or client names** anywhere in the courses.

## Submitting changes

1. Fork the repo
2. Create a branch (`fix/description` or `feat/description`)
3. Make your changes
4. Ensure `python3 build/validate.py` passes
5. Open a pull request

## Releasing

Installed users only receive an update when the `version` field in `plugins/claude-docent/.claude-plugin/plugin.json` changes. A commit alone does nothing for them.

1. Bump `version` in `plugins/claude-docent/.claude-plugin/plugin.json` (semver: patch for fixes, minor for new lessons or a new course, major for breaking changes)
2. Add a `CHANGELOG.md` entry under a new version heading
3. Merge to `main`
4. Tag and publish a release: `gh release create vX.Y.Z --title "vX.Y.Z: summary" --notes "..."`

Publishing the release triggers `.github/workflows/release.yml`, which validates, builds the per-skill zips, and attaches them to the release for claude.ai users.
