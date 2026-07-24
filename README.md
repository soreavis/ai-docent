# claude-docent

[![CI](https://github.com/soreavis/claude-docent/actions/workflows/ci.yml/badge.svg)](https://github.com/soreavis/claude-docent/actions/workflows/ci.yml)
![Version](https://img.shields.io/badge/version-0.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-blue)
![Agent Skills](https://img.shields.io/badge/Agent%20Skills-6%20courses-green)

Six multi-session tutor courses that take you from Claude beginner to power user — an onboarding wizard, a personalized plan, hands-on exercises on your own real work, boss fights as level gates, and progress that survives across sessions.

> [!IMPORTANT]
> **This is an independent, community-maintained project.** It is **not officially affiliated with, endorsed by, or supported by Anthropic.** This is not an official Anthropic or Claude product. Use of this software is entirely at your own risk.

## The courses

The arc: **Use → Craft → Trust → Secure → Afford → Build.**

| Course | Levels | What it teaches |
|---|---|---|
| `foundations` | 0–4 | beginner → power user, built around a capstone project |
| `prompt-craft` | 4 | getting dramatically better outputs |
| `reliability` | 4 | guardrails against hallucination and fabrication |
| `security` | 4 | prompt injection, data leaks, runaway agents |
| `mechanics` | 3 | models, context windows, plans and cost |
| `builder` | 5 | the API, tool use, agents, MCP, evals |

Start with `foundations` unless you already use Claude daily. Each course is independent, but they cross-reference each other.

## Install — Claude Code

```shell
/plugin marketplace add soreavis/claude-docent
/plugin install claude-docent@claude-docent
/reload-plugins
```

Then start a course:

```shell
/claude-docent:foundations
```

Works the same in the terminal, your IDE, and the Claude desktop app's plugin browser.

### Stay up to date automatically

Claude Code can update marketplaces and their plugins in the background after startup, but **third-party marketplaces have auto-update off by default.** Turn it on once:

1. Run `/plugin`
2. Go to the **Marketplaces** tab
3. Select **claude-docent**
4. Choose **Enable auto-update**

After that, new course versions arrive on their own — Claude Code checks shortly after each session starts and prompts you to run `/reload-plugins` when something changed.

To update by hand instead:

```shell
/plugin marketplace update claude-docent
```

### For a team or a repo

Add this to a project's `.claude/settings.json` and everyone who trusts the folder is prompted to install it:

```json
{
  "extraKnownMarketplaces": {
    "claude-docent": {
      "source": { "source": "github", "repo": "soreavis/claude-docent" }
    }
  },
  "enabledPlugins": ["claude-docent@claude-docent"]
}
```

## Install — claude.ai and Cowork

Claude Code plugins do **not** appear on claude.ai. That surface takes one zip per course:

1. Download the zips from the [latest release](https://github.com/soreavis/claude-docent/releases/latest), or build them yourself with `./build/zip.sh`
2. On claude.ai go to **Customize → Skills** and upload the zip for each course you want
3. Toggle it on

Requires code execution to be enabled (Settings → Capabilities on Free/Pro/Max; Organization settings on Team/Enterprise). Cowork loads whatever skills are enabled on your claude.ai account, so uploading once covers both.

> [!NOTE]
> **There is no auto-update on this surface.** claude.ai has no mechanism to refresh an uploaded skill — when a new version ships you re-download the zip and upload it again. Auto-update is Claude Code only.

## Where your progress is saved

Each course writes a Progress Card at the end of every session.

| Surface | Where it goes |
|---|---|
| Claude Code, Cowork | `~/.claude-docent/progress-<course>.md`, written automatically |
| claude.ai chat | shown in the conversation — copy it somewhere safe |

Plain chat has no filesystem that persists between conversations, so there the card is your save file: paste the most recent one into a new session to pick up where you left off. A pasted card always outranks everything else.

## Structure

```
claude-docent/
├── .claude-plugin/marketplace.json     # the catalog users add
├── build/
│   ├── validate.py                     # spec + convention checks, run by CI
│   └── zip.sh                          # builds the claude.ai zips
└── plugins/claude-docent/
    ├── .claude-plugin/plugin.json      # name here = the /claude-docent: namespace
    └── skills/<course>/
        ├── SKILL.md                    # the operating manual, loads on activation
        └── references/
            ├── curriculum.md           # loaded when building the lesson plan
            └── game-mode.md            # loaded only if Game Mode is on
```

Splitting the curriculum into `references/` keeps each `SKILL.md` small — the body loads in full when a course starts, while reference files load only when read.

## Conventions

- **Descriptions stay under 200 characters.** The open spec allows 1024, but the claude.ai uploader is stricter and one file has to work on both surfaces.
- **`disable-model-invocation: true`** keeps courses user-invoked, so a six-level curriculum never activates itself in the middle of unrelated work. It's a Claude Code extension, not part of the open spec — `build/zip.sh` strips it from the claude.ai zips.
- **No hardcoded prices, usage limits, or model IDs.** Every changeable number routes to live docs. A well-formed but stale figure is a hallucination.
- **Doc domains:** `code.claude.com/docs`, `platform.claude.com/docs`, `support.claude.com`, `claude.com/pricing`. Never `docs.claude.com` — it's stale.

`python3 build/validate.py` enforces all of this, and CI runs it on every push.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — including the [release process](CONTRIBUTING.md#releasing), since installed users only receive an update when `version` in `plugin.json` is bumped.

## Credits

- **Maintained by**: [Julian Soreavis](https://github.com/soreavis)

## License

MIT — see [LICENSE](LICENSE).
