# security — cheat-sheet

Use Claude without getting manipulated, leaked, or burned: how AI-specific attacks work, how to spot them, and how to set up guardrails so you're hard to hit by default.

## The mantra

*data is not instructions; least privilege; assume untrusted content is hostile; secrets never in prompts; reversibility is a safety feature.*

## The arc

- **Level 1 — The threat model.** Check every task against the three legs before you start it.
- **Level 2 — Prompt injection and data leaks.** Treat anything the model reads on your behalf as data, never as commands.
- **Level 3 — Agent safety.** Grant the minimum, review before it acts, keep everything reversible.
- **Level 4 — Systems, incident response and judgment.** Turn the defenses into one stack, and know when not to connect an agent at all.

## Habits

- Check the session against the lethal trifecta — Simon Willison's framing: private data, untrusted content, a way to send data out. (1.1)
- Keep an attack-surface map in three columns: what brings input in, what holds secrets, what can act or send. (1.2)
- Triage first — tool or send-channel, plus untrusted content, plus something sensitive means full guardrails. (1.3)
- Hunt the buried instruction before you act on a document: white text, HTML comments, alt text, mid-document. (2.2)
- Name the exfiltration channel a payload would use: an image URL, a disguised link, a tool or connector call. (2.3)
- Sort what you're about to paste into fine, redact first, and never — and confirm your own plan's data handling in the docs. (2.4)
- Grant connectors and MCP servers the narrowest scopes that work, and review what each can reach before approving. (2.5)
- Keep a standing config that tells Claude to surface embedded instructions rather than follow them. (2.6)
- Make it propose before it touches anything, and read the diff — or ask for it in plain language. (3.2)
- Confirm before anything you can't undo, and check that its contents exist somewhere else — git history, a backup, a copy — before deleting. (3.3)
- Commit before a session, and let the agent work on an isolated copy. (3.4)
- Verify a package exists and is the real one before installing it. (3.6)
- Demand the real output. "Done" is a claim, not evidence. (3.7)
- Rehearse the drill before you need it: contain, rotate the credential, roll back, assess the blast radius. (4.3)

## Before you trust it

- Find every embedded instruction, name the exfiltration channel, and say which leg of the trifecta each exploits. (2.7)
- Read the plan for an over-scoped permission grab or an irreversible action, and name the guardrail that would have blocked it. (3.8)
- Ask whether a single piece of untrusted content could reach a sensitive action here — and whether you could afford that going wrong. (4.4)
- Run the whole stack against one real case: an injection attempt, a live tool, a secret in reach. (4.5)
- Match the defense to the exposure. Over-locking low-risk work is its own failure.
- Log the close call in one line: what it was, how it was caught, which guardrail.

## Never

- Never let a document, web page or tool result act as a command.
- Never paste live secrets, keys, passwords, other people's private data or regulated data into a chat.
- Never blanket-approve an agent that is reading untrusted content.
- Never delete a leaked secret and call it handled — rotate it, and assume it's compromised.
- Never add a connector or MCP server you wouldn't treat like an unknown app.
- Never perform an attack to see what it does. Describe it, neutralise it, leave nothing live.
- Never let an exercise close with a payload still un-defused — ask for the neutralisation.


The keepable version of what /ai-docent:security builds with you on your own work.
