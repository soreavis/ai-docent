# shipping — cheat-sheet

Teaches you to turn what an agent produces into work a real reviewer accepts: scoped small enough to review, checked before anyone else sees it, landed without burning the people downstream.

## The mantra

*generating is cheap, reviewing is not; one change, one purpose; read the diff before anyone else does.*

## The arc

- **Level 1 — The shipping gap:** treat the agent finishing as the start of a review, not the end.
- **Level 2 — Scoping so it lands:** make one change do one thing.
- **Level 3 — Reviewing your own work:** read every line before anyone else does.
- **Level 4 — Landing it with other people:** tell the reviewer what changed, why, and what you left out.

## Habits

- Estimate the change in reviewer-minutes, not in what it cost you to produce. (1.2)
- Before handing anything over, ask who reviews it, what it costs them, and how fast it can be undone. (1.3)
- Make each change do one thing, and name every separate thing it currently does. (2.1)
- Split a big change into an ordered series, each step independently correct, the risky part last. (2.2)
- Strip everything from the diff that wasn't asked for. (2.3)
- State scope as a boundary: what to touch, what not to touch, what done looks like, and what to do when it hits something unexpected. (2.4)
- Define done in advance, then stop there. (2.5)
- Ask for a current-state report and confirm the premise before changing anything. (2.6)
- Write the acceptance criterion before the work, not after. (2.6)
- Read the diff, not the agent's summary of the diff. (3.1)
- Audit for removals and defaults — what got smaller or looser. (3.3)
- At volume, read every deletion and every file you didn't expect to be touched. (3.5)
- Check what anything the agent pulled in is licensed under before it lands. (4.2)
- Apply feedback as a minimal follow-up, not a fresh generation. (4.4)

## Before you hand it over

- Too long to read in one pass? That's a scoping signal — go back and split it. (3.1)
- Does every claim in the description match what's actually in the diff? (1.4)
- What did it delete, and which defaults or permissions got looser? (3.3)
- Run your own pre-handover checklist, short enough that you'll really run it. (3.4)
- Give a clean session the diff alone, briefed to refute rather than review. (3.6)
- Does the description say what changed, why, what you left out, and how you verified it? (4.1)

## Never

- Never let "it runs" or "the tests pass" close a review.
- Never ship unrequested edits — renames, reformatting, adjacent improvements, new dependencies.
- Never take the agent's summary of the diff in place of the diff.
- Never accept a claim of work as work.
- Never regenerate the whole change in response to one review comment.
- Never imply more human authorship than there was, and never claim verification you didn't do.
- Never feed in work you'd need permission to copy.
- Never read a rejection with no explanation as a verdict; it's data.

The keepable version of what /ai-docent:shipping builds with you on your own work.
