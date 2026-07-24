# ai-docent

[![CI](https://github.com/soreavis/ai-docent/actions/workflows/ci.yml/badge.svg)](https://github.com/soreavis/ai-docent/actions/workflows/ci.yml)
![Version](https://img.shields.io/badge/version-0.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-blue)
![Agent Skills](https://img.shields.io/badge/Agent%20Skills-6%20courses-green)

Six multi-session tutor courses that take you from Claude beginner to power user — an onboarding wizard, a personalized plan, hands-on exercises on your own real work, boss fights as level gates, and progress that survives across sessions.

> [!IMPORTANT]
> **This is an independent, community-maintained project.** It is **not affiliated with, endorsed by, or supported by** Anthropic, OpenAI, Google, GitHub/Microsoft, xAI, Cursor, or any other vendor whose tools it installs into or teaches. Claude, Codex, Gemini, Copilot, Grok, and Cursor are trademarks of their respective owners, used here only to say what this project works with. Use of this software is entirely at your own risk.

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

The courses teach **Claude** specifically. They install into any skills-compatible agent, so you can run them from whichever tool you already live in.

## Install

Use your platform's native plugin or skill manager where one exists — those lanes keep the runtime's own update path.

| Platform | Install | Update |
|---|---|---|
| **Claude Code** | `/plugin marketplace add soreavis/ai-docent` then `/plugin install ai-docent@ai-docent` | `/plugin marketplace update ai-docent`, or enable marketplace auto-update |
| **Codex** | `codex plugin marketplace add soreavis/ai-docent` then `codex plugin add ai-docent@ai-docent` | `codex plugin marketplace upgrade` |
| **Cursor** | `npx skills add soreavis/ai-docent --skill <course>` | re-run the installer |
| **Gemini CLI** | `gemini extensions install https://github.com/soreavis/ai-docent` | `gemini extensions update ai-docent` |
| **Copilot / GitHub CLI** | `gh skill install soreavis/ai-docent <course>` | `gh skill update <course>` |
| **Grok** | `grok plugin marketplace add soreavis/ai-docent` then `grok plugin install soreavis/ai-docent --trust` | `grok plugin update ai-docent` |
| **claude.ai / Desktop / Cowork** | Customize → Plugins → **+** → Add marketplace → `https://github.com/soreavis/ai-docent` (paid plans) | automatic on marketplace sync |
| **Other agents** | `npx skills add soreavis/ai-docent --skill <course>` | `npx skills update` |

`<course>` is one of `foundations`, `prompt-craft`, `reliability`, `security`, `mechanics`, `builder`.

> [!NOTE]
> The plugin lanes (Claude Code, Codex, Grok) install **all six courses at once**. The single-skill lanes (`gh skill`, `npx skills`) install **one course per command** — run it once per course you want, which is usually what you want anyway.

Once installed, start a course:

```
/ai-docent:foundations
```

### Claude Code — turn on auto-update

Claude Code can update marketplaces and their plugins in the background, but **third-party marketplaces have auto-update off by default.** Turn it on once:

1. Run `/plugin`
2. Go to the **Marketplaces** tab
3. Select **ai-docent**
4. Choose **Enable auto-update**

After that new versions arrive on their own — Claude Code checks shortly after each session starts and prompts you to run `/reload-plugins` when something changed.

### For a team or a repo

Add this to a project's `.claude/settings.json` and everyone who trusts the folder is prompted to install it:

```json
{
  "extraKnownMarketplaces": {
    "ai-docent": {
      "source": { "source": "github", "repo": "soreavis/ai-docent" }
    }
  },
  "enabledPlugins": ["ai-docent@ai-docent"]
}
```

### claude.ai, Claude Desktop and Cowork

Plugins work here too, from the same marketplace — no zips needed. **Paid plans only (Pro, Max, Team, Enterprise).**

1. Open **Customize** in the left sidebar, then the **Plugins** tab (in Cowork, open the **Cowork** tab first)
2. Under **Personal plugins**, click **+** → **Add marketplace** → **Add from a repository**
3. Point it at `https://github.com/soreavis/ai-docent`
4. Install **ai-docent**, then type `/` or click **+** to pick a course

The skills a plugin bundles work in chat on the web, the Chat tab in Claude Desktop, and Cowork alike.

**Team and Enterprise** owners can push it to everyone from **Organization settings → Plugins → Add plugin → GitHub**, using `soreavis/ai-docent`. Cowork and Skills both have to be enabled for the organization first.

#### Free plan, or you'd rather have standalone skills

Upload the per-course zips instead:

1. Download them from the [latest release](https://github.com/soreavis/ai-docent/releases/latest), or build them with `./build/zip.sh`
2. Go to **Customize → Skills** and upload the zip for each course you want
3. Toggle it on

Requires code execution to be enabled (Settings → Capabilities on Free/Pro/Max; Organization settings on Team/Enterprise).

> [!NOTE]
> **The zip path has no auto-update.** There is no mechanism to refresh an uploaded skill — when a new version ships, re-download and re-upload. The marketplace path above updates on its own, so prefer it if you're on a paid plan.

## Where your progress is saved

Each course writes a Progress Card at the end of every session.

| Surface | Where it goes |
|---|---|
| Any agent with file access | `~/.ai-docent/progress-<course>.md`, written automatically |
| Plain chat (claude.ai) | shown in the conversation — copy it somewhere safe |

Chat has no filesystem that persists between conversations, so there the card is your save file: paste the most recent one into a new session to pick up where you left off. A pasted card always outranks everything else.

## Structure

```
ai-docent/
├── skills/<course>/
│   ├── SKILL.md                    # the operating manual, loads on activation
│   └── references/
│       ├── curriculum.md           # loaded when building the lesson plan
│       └── game-mode.md            # loaded only if Game Mode is on
├── version.txt                     # single source of truth for the version
├── .claude-plugin/                 # plugin.json + marketplace.json
├── .codex-plugin/ .cursor-plugin/ .grok-plugin/
├── .agents/plugins/marketplace.json
├── gemini-extension.json
└── build/
    ├── validate.py                 # spec, conventions, version lockstep — CI runs it
    └── zip.sh                      # builds the claude.ai zips
```

One skill tree, eight thin manifests. Release Please rewrites the version in every one of them from `version.txt`, and CI fails if any drift apart.

## Conventions

- **Descriptions stay under 200 characters.** The open spec allows 1024, but the claude.ai uploader is stricter and one file ships everywhere.
- **`disable-model-invocation: true`** keeps courses user-invoked, so a six-level curriculum never activates itself mid-task. It's a Claude Code extension, not part of the open spec — `build/zip.sh` strips it from the claude.ai zips.
- **No hardcoded prices, usage limits, or model IDs.** Every changeable number routes to live docs. A well-formed but stale figure is a hallucination.
- **Doc domains:** `code.claude.com/docs`, `platform.claude.com/docs`, `support.claude.com`, `claude.com/pricing`. Never `docs.claude.com` — it's stale.

`python3 build/validate.py` enforces all of this, and CI runs it on every push.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the release process and [AGENTS.md](AGENTS.md) if an AI agent is doing the work.

## Credits

- **Created by**: [Julian Soreavis](https://github.com/soreavis)

## License

MIT — see [LICENSE](LICENSE).
