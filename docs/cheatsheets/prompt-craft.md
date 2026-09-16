# prompt-craft — cheat-sheet

Takes you from writing one-line requests to engineering prompts that reliably get great results out of Claude.

## The mantra

*the prompt is the spec; specificity beats hope; test, don't trust.*

## The arc

- **Level 1 — Foundations of a great prompt:** stop making it guess the parts you left out.
- **Level 2 — Shaping the output:** name the shape you want before you ask, not after.
- **Level 3 — Reasoning and complex tasks:** decompose, and get a plan before it acts.
- **Level 4 — Systems and reuse:** promote what worked into standing infrastructure.

## Habits

- Label what's missing before you rewrite: context, task, format, constraints. (1.1)
- Replace vagueness with audience, purpose, scope, and what "good" looks like. (1.2)
- On anything fuzzy, ask it for three questions that would change its answer. (1.3)
- Give it a role and a success criterion. (1.4)
- Steer with targeted follow-ups — more like X, less like Y, keep the third point. (1.5)
- When the answer is bad, diagnose the prompt: missing context, unclear task, no format, conflicting constraints. (1.6)
- Use a finished sample to teach the look; use a worked example to teach the method. (2.1)
- Check what your example accidentally teaches, and include the awkward case, not only the easy one. (2.1)
- Name the format up front instead of reformatting afterwards. (2.3)
- Separate instructions from source material with headings, quotes, or fenced blocks. (2.6)
- Put the document first and the question last; for long material, pull the quotes first and answer from those. (2.6)
- Ask for the general principle first, then the specific answer. (3.1)
- Ask for three approaches and what each is bad at, then a recommendation. (3.6)
- Run the same prompt two or three times in separate chats; where the answers disagree is where it's underspecified. (4.6)

## Before you claim it works

- Run both versions and show the before and after out loud. (1.7)
- Hit the exact spec — format, tone, length — in a single prompt, no back-and-forth. (2.8)
- Take the task that fails as one prompt and get it right by decomposition and chaining. (3.7)
- A/B the two versions on a three-point rubric, then run the winner three times and note what varied. (4.6)
- Install the winner as a standing instruction and confirm behaviour actually changed. (4.7)

## Never

- Never claim a technique that can't beat the old prompt in a live comparison.
- Never practise on toy examples — run everything on your real prompts and tasks.
- Never treat a technique as a magic word; they are testable heuristics.
- Never teach or accept version-specific steps from memory when search is unavailable.
- Never state a figure you did not look up; hedging it with "roughly" does not make it safe.
- Never invent what you did not read or run — a file, an output, or a URL path you haven't seen.
- Never let a choice of tone drop a hedge or skip a verification.

The keepable version of what /ai-docent:prompt-craft builds with you on your own work.
