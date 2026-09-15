# Troubleshooting

## The command does nothing

Courses don't start themselves. In Claude Code they carry a flag that blocks automatic invocation outright; elsewhere each course describes itself as needing an explicit request. Either way you have to ask for one by name.

Check the skill is installed and enabled. On plugin lanes that's the plugin manager for your runtime; on zip uploads it's a per-skill toggle. If you installed through a marketplace and nothing appears, the marketplace may have synced without the plugin being enabled.

In Claude Code, `/reload-plugins` picks up changes without a restart.

## It started over instead of continuing

It couldn't find your place.

With file access, check whether `~/.ai-docent/progress-<course>.md` exists. If your home directory isn't writable the course falls back to `./.ai-docent/` in the working directory, which means a different directory gives you a different file.

Without file access, paste your most recent Progress Card. That overrides everything, and it's the intended way to resume in a chat window.

If you have no card and no file, say roughly where you got to. It'll pick up from your description rather than restarting the wizard.

## It won't give me exact steps

If web search isn't available in the session, the courses refuse to teach version-specific instructions from memory. Menus, flags, and prices change, and stale steps stated confidently are worse than none.

Enable web search, or paste the relevant documentation page and it'll work from that.

## It says a domain instead of a link

Same reason. The courses only link to paths they've actually seen in a search result or on a page they fetched. An invented URL looks authoritative and 404s, so you get "check code.claude.com/docs for X" instead.

## The plugin isn't updating

Installed copies only change when the version number changes. A new commit on the repository does nothing for you.

Auto-update exists in Claude Code but is off by default for third-party marketplaces. Turn it on under `/plugin` in the Marketplaces tab, or run the update command for your lane from the table in the [main README](../README.md#install).

Skill zips have no update mechanism at all. Re-download and re-upload.

## Game mode numbers look wrong

XP is recomputed from the logged events each session rather than carried forward, so a number can change if the log did. What shouldn't happen is points appearing for work you didn't do. If a badge or a streak shows up that you can't account for, say so, and it should recalculate from the log rather than defend the total.

## The companion has nothing to drill

It only works from cards. If you haven't finished any course, there's nothing to build a queue from and it will say so rather than inventing drills — open `/ai-docent:start` instead.

If you have done a course but it still comes up empty, it couldn't read the cards. On a filesystem check `~/.ai-docent/`; in a chat window, paste the cards for the courses you want covered.

"Nothing is due" is a normal answer, not a fault. Items sit at 1 day, 3 days, 1 week, then 3 weeks apart. Ask for a retro or the items retiring soonest instead.

## It asked me something it should already know

Name, tone and game-mode setting are read off your newest card, and the companion asks only for your revision cadence. If you're being asked again, the card it found didn't carry those fields — usually a hand-edited card, or one from a session that ended before the card was written.

## A course said something that isn't true

Tell it. The courses are built to correct themselves and note it rather than argue, and `reliability` treats catching this as the skill being taught.

If it's reproducible and looks like a defect in the course itself rather than a one-off, open an issue. Anything that looks like it could be exploited belongs in [SECURITY.md](../SECURITY.md) instead of a public issue.

## The tone won't stick

The chosen voice is recorded on the Progress Card. If a card arrives without one, the course asks rather than guessing, so a hand-edited card missing the `Tone:` line will produce that question again.

Note that a voice will not override an accuracy rule. If you asked for confident and it still hedged, that's working as intended: it hedges because the evidence is thin, not because of the persona.
