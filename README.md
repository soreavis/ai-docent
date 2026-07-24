# ai-docent

[![CI](https://github.com/soreavis/ai-docent/actions/workflows/ci.yml/badge.svg)](https://github.com/soreavis/ai-docent/actions/workflows/ci.yml)
![Version](https://img.shields.io/badge/version-0.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-blue)
![Agent Skills](https://img.shields.io/badge/Agent%20Skills-8%20courses-green)

Eight multi-session tutor courses that take you from beginner to genuine power user of AI agents — an onboarding wizard, a personalized plan, hands-on exercises on your own real work, boss fights as level gates, and progress that survives across sessions.

Installs into whichever agent you already use: Claude Code, Codex, Cursor, Gemini CLI, Copilot, Grok, and anything else that reads the [Agent Skills](https://agentskills.io) standard.

> [!IMPORTANT]
> **This is an independent, community-maintained project.** It is **not affiliated with, endorsed by, or supported by** Anthropic, OpenAI, Google, GitHub/Microsoft, xAI, Cursor, or any other vendor whose tools it installs into or teaches. Claude, Codex, Gemini, Copilot, Grok, and Cursor are trademarks of their respective owners, used here only to say what this project works with. Use of this software is entirely at your own risk.

## The courses

The arc: **Use → Craft → Trust → Ship → Sustain → Secure → Afford → Build.**

| Course | Levels | What it teaches |
|---|---|---|
| `foundations` | 0–4 | beginner → power user, built around a capstone project |
| `prompt-craft` | 4 | getting dramatically better outputs |
| `reliability` | 4 | guardrails against hallucination and fabrication |
| `shipping` | 4 | scoping, reviewing and landing agent-generated work |
| `long-haul` | 4 | projects that span days: context, handoffs, recovery |
| `security` | 4 | prompt injection, data leaks, runaway agents |
| `mechanics` | 3 | models, context windows, plans and cost |
| `builder` | 5 | APIs, tool use, agents, MCP, evals |

Start with `foundations` unless you already use an agent daily. Each course is independent, but they cross-reference each other.

> [!NOTE]
> The courses run in any agent, but the curriculum currently uses **Claude** as its worked platform — the exercises walk through Claude Code, claude.ai, and the Claude API. The transferable craft (prompting, verification habits, injection defence, cost reasoning) applies anywhere; the specific menus and commands are Claude's.

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
| **Claude web / Desktop / Cowork** | Customize → Plugins → **+** → Add marketplace → `https://github.com/soreavis/ai-docent` | automatic on marketplace sync |
| **Other agents** | `npx skills add soreavis/ai-docent --skill <course>` | `npx skills update` |

`<course>` is one of `foundations`, `prompt-craft`, `reliability`, `shipping`, `long-haul`, `security`, `mechanics`, `builder`.

> [!NOTE]
> The plugin lanes install **all eight courses at once**. The single-skill lanes (`gh skill`, `npx skills`) install **one course per command** — run it once per course you want, which is usually what you want anyway.

Once installed, start a course:

```
/ai-docent:foundations
```

### Turning on automatic updates

Most runtimes can refresh a marketplace in the background, but **third-party marketplaces usually have auto-update off by default.** In Claude Code, turn it on once:

1. Run `/plugin`
2. Go to the **Marketplaces** tab
3. Select **ai-docent**
4. Choose **Enable auto-update**

After that new versions arrive on their own. The equivalent update command for every other lane is in the table above.

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

Team and Enterprise owners on Claude can push it to everyone from **Organization settings → Plugins → Add plugin → GitHub**, using `soreavis/ai-docent`.

### Standalone skill zips

If your runtime takes individual skill folders rather than a plugin — or you're on a plan where plugins aren't available — upload the per-course zips instead:

1. Download them from the [latest release](https://github.com/soreavis/ai-docent/releases/latest), or build them with `./build/zip.sh`
2. Upload the zip for each course you want, wherever your runtime accepts skills
3. Toggle it on

> [!NOTE]
> **The zip path has no auto-update.** Re-download and re-upload when a new version ships. Prefer a marketplace lane if your runtime has one.

## Where your progress is saved

Each course writes a Progress Card at the end of every session.

| Surface | Where it goes |
|---|---|
| Any agent with file access | `~/.ai-docent/progress-<course>.md`, written automatically |
| Plain chat, no filesystem | shown in the conversation — copy it somewhere safe |

Chat surfaces have no filesystem that persists between conversations, so there the card is your save file: paste the most recent one into a new session to pick up where you left off. A pasted card always outranks everything else.

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
    └── zip.sh                      # builds the standalone skill zips
```

One skill tree, eight thin manifests. Release Please rewrites the version in every one of them from `version.txt`, and CI fails if any drift apart.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the release process and [AGENTS.md](AGENTS.md) if an AI agent is doing the work.

## Credits

- **Created by**: [Julian Soreavis](https://github.com/soreavis)

## License

MIT © 2026 Julian Soreavis — see [LICENSE](LICENSE).
