# reliability — cheat-sheet

Teaches you to use Claude in ways that minimize fabrication, to catch errors when they happen anyway, and to set up guardrails so your sessions are trustworthy by default.

## The mantra

*confident ≠ correct; cited ≠ verified; claimed ≠ done.*

## The arc

- **Level 1 — Know your enemy:** tie verification effort to stakes, not to how much you trust the tool today.
- **Level 2 — Guardrails in Claude chats:** ground the answer in source material instead of memory.
- **Level 3 — Guardrails in Claude Code:** demand the output; never accept "done" as evidence.
- **Level 4 — Cowork, systems and judgment:** decide what not to delegate, and contain what you catch.

## Habits

- Before any task, ask: will someone act on this, and is it hard to undo? (1.3)
- Permit "I don't know" explicitly, and ask which part of the answer it is least sure about. (2.1)
- Give it the document, put the document before the question, and demand a quoted passage per claim — "not in the document" if it isn't there. (2.2)
- Click the citation. A citation is a claim, not proof. (2.3)
- Make it compute instead of estimating, then spot-check one number by hand. (2.4)
- Phrase neutrally, and ask for the strongest case against. (2.5)
- Brief the second opinion to refute, not review, and paste the output rather than the conversation. (2.6)
- Check a refutation at its source before acting on it. (2.6)
- Ask what's already there before you ask for a plan. (3.1)
- Demand the actual command output, and re-run it yourself. (3.2)
- Check that a package, function, or config option exists before it goes in. (3.5)
- Sample bulk work at random plus the riskiest items. (4.3)
- After a catch, trace where the wrong fact already went and correct downstream. (4.5)
- Log every fabrication caught: what it was, how you caught it, which guardrail. (woven)

## Before you trust it

- Triage first: will someone act on it, and is it hard to undo? (1.3)
- Grounded — is every claim backed by a quoted passage from the source? (2.2)
- Cited — did you open the source and confirm it says that, in context? (2.3)
- Computed, not estimated — and did you spot-check one number yourself? (2.4)
- Claimed done — did you see the output and re-run it? (3.2)
- Can you verify this at all, and if not, can you afford it being wrong? Two no's, don't delegate. (4.4)

## Never

- Never treat fluency or confidence as evidence.
- Never let verification effort follow your trust in the tool instead of the stakes.
- Never accept "done", "tests pass", or "I checked it" as evidence.
- Never install a package before confirming it exists.
- Never let an agent touch originals without a copy.
- Never delegate something irreversible that you cannot verify.
- Never paste passwords, keys, or other people's private data into any AI.
- Never let a spot-the-fake round close without the full answer key — ask for it.

The keepable version of what /ai-docent:reliability builds with you on your own work.
