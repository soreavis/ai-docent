![A robed guide holding a lantern points out a route across a vast twilight valley to a child standing beside them, with a line of glowing waypoints tracing the path toward the horizon.](docs/assets/hero.jpg)

# ai-docent

[![CI](https://github.com/soreavis/ai-docent/actions/workflows/ci.yml/badge.svg)](https://github.com/soreavis/ai-docent/actions/workflows/ci.yml)
![Version](https://img.shields.io/static/v1?label=version&message=0.2.1&color=blue) <!-- x-release-please-version -->
![License](https://img.shields.io/badge/license-MIT-blue)
![Agent Skills](https://img.shields.io/badge/Agent%20Skills-8%20courses-green)

Eight multi-session tutor courses that take you from beginner to genuine power user of AI agents — an onboarding wizard, a personalized plan, hands-on exercises on your own real work, boss fights as level gates, a coaching voice you choose, and progress that survives across sessions.

Installs into whichever agent you already use: Claude Code, ChatGPT, Codex, Cursor, Gemini CLI, Copilot, Grok, and anything else that reads the [Agent Skills](https://agentskills.io) standard.

> [!IMPORTANT]
> **An independent project, built and maintained by Julian Soreavis.** Not affiliated with, endorsed by, or sponsored by any of the vendors whose tools it installs into or teaches. Product names and trademarks belong to their respective owners, used here only to describe compatibility. Use at your own risk.

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
| **Cursor** | `npx skills add soreavis/ai-docent --skill <course> -a cursor` | `npx skills update` |
| **Gemini CLI** | `gemini extensions install https://github.com/soreavis/ai-docent` | `gemini extensions update ai-docent` |
| **Copilot / GitHub CLI** | `gh skill install soreavis/ai-docent <course>` | `gh skill update <course>` |
| **Grok** | `grok plugin marketplace add soreavis/ai-docent` then `grok plugin install soreavis/ai-docent --trust` | `grok plugin update ai-docent` |
| **Claude web / Desktop / Cowork** | Customize → Plugins → **+** → Add marketplace → `https://github.com/soreavis/ai-docent` | automatic on marketplace sync |
| **ChatGPT** | Skills → **Create** → **Upload from your computer**, one [release zip](https://github.com/soreavis/ai-docent/releases/latest) per course | re-upload the newer zip |
| **Other agents** | `npx skills add soreavis/ai-docent --skill <course>` | `npx skills update` |

`<course>` is one of `foundations`, `prompt-craft`, `reliability`, `shipping`, `long-haul`, `security`, `mechanics`, `builder` — or one of the two support skills, `start` (picks a course for you) and `companion` (drills what you've learned). The plugin lanes include everything automatically; on the single-skill lanes, install the support skills alongside at least one course, since neither has anything to work with on its own.

> [!NOTE]
> The plugin lanes install **all eight courses at once**. The skill lanes take one course per command by default, which is usually what you want — but `npx skills add soreavis/ai-docent --skill '*'` installs the lot if you'd rather. `gh skill` is in preview and its flags may change. `gemini extensions install` stops at a confirmation prompt; pass `--consent` when scripting it.

Once installed, if you're not sure where to begin, start here — it asks what's actually going wrong and points you at one course:

```
/ai-docent:start
```

It also runs the whole eight-course arc in order as a single guided program, keeping the track's place across sessions. Or skip it and open a course directly:

```
/ai-docent:foundations
```

Once you've finished something, a third skill keeps it from fading:

```
/ai-docent:companion
```

It drills what you've already covered on a widening schedule, reads across every course's progress at once to spot which habits have gone quiet, and has a five-minute mode for days you have nothing else. It never teaches new material — if a drill exposes a gap, it names the course that covers it and stops. There's no scheduler behind it: coming back is on you, and it says so rather than implying reminders will arrive.

> [!IMPORTANT]
> **New to this and not sure what to actually type?** Read **[Example prompts](docs/example-prompts.md)** first — a page of copyable starting points, no course required.
>
> It covers the four parts most beginner prompts leave out, how to make the model interview you when the task is still fuzzy in your own head, prompts for everyday work, and the two questions that tell you whether an answer can be trusted at all.

### Choosing how it talks to you

Every course asks, once, how you want to be taught: **Coach** (warm and direct, the default), **Blunt** (terse, no praise), **Socratic** (mostly questions), **Peer** (casual colleague), **Patient** (no assumed background), **Formal** (professional and structured) — or describe your own. The choice is recorded on your Progress Card, so it survives between sessions, and you can change it any time by saying so.

Tone is delivery, never content. No voice will drop a hedge, skip a verification, or state a figure it didn't look up — where a voice and a guardrail conflict, the guardrail wins and the course says so.

Longer guides — your first session, example prompts, how sessions run, the companion, best practices, troubleshooting — are in [docs/](docs/).

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
  "enabledPlugins": {
    "ai-docent@ai-docent": true
  }
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

On a tool with no skill support at all — Perplexity Spaces, a plain chat window — paste a course's `SKILL.md` in as the standing instruction and keep its `references/` files to hand. Every course is written to survive this: with no filesystem, the Progress Card becomes your save file, and pasting the most recent one back resumes the course. Check the tool's instruction-length limit first, though — the courses run roughly 15–20 KB each, and a silently truncated course is worse than none.

## Where your progress is saved

Each course writes a Progress Card at the end of every session.

| Surface | Where it goes |
|---|---|
| Any agent with file access | `~/.ai-docent/progress-<course>.md`, written automatically |
| Plain chat, no filesystem | shown in the conversation — copy it somewhere safe |

Cards are checked rather than trusted. A card from another course won't be resumed from, missing fields are named instead of filled in, and if a file is further along than something you pasted, you're asked which to use rather than quietly losing the newer one. If nothing survives at all, three questions rebuild it — you don't get sent back through onboarding. Say **save** at any point to get the card mid-session.

Chat surfaces have no filesystem that persists between conversations, so there the card is your save file: paste the most recent one into a new session to pick up where you left off. A pasted card outranks the file and the chat history — after the course has checked it.

## Structure

```
ai-docent/
├── skills/<course>/                # the eight courses
│   ├── SKILL.md                    # the operating manual, loads on activation
│   └── references/
│       ├── curriculum.md           # loaded when building the lesson plan
│       ├── tone.md                 # the voices, and what no voice may change
│       └── game-mode.md            # loaded only if Game Mode is on
├── skills/start/                   # launcher — routes, sequences the full arc
├── skills/companion/               # revision — drills what the courses seeded
├── docs/                           # how to use the courses
├── version.txt                     # single source of truth for the version
├── .claude-plugin/                 # plugin.json + marketplace.json
├── .codex-plugin/ .cursor-plugin/ .grok-plugin/
├── .agents/plugins/marketplace.json
├── gemini-extension.json
└── build/
    ├── validate.py                 # spec, conventions, version lockstep — CI runs it
    └── zip.sh                      # builds the standalone skill zips
```

One skill tree, eight thin manifests — one per platform. Every one of them takes its version from `version.txt`, they are all rewritten together when a release is cut, and CI fails if any drift apart.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the release process and [AGENTS.md](AGENTS.md) if an AI agent is doing the work.

## Credits

- **Created by**: [Julian Soreavis](https://github.com/soreavis)

## License

MIT © 2026 Julian Soreavis — see [LICENSE](LICENSE).
