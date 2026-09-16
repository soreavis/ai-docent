# mechanics — cheat-sheet

Learn how Claude actually works under the hood and how to operate it efficiently and affordably: context windows and tokens, the model family and when to reach for which, plan tiers and usage limits, the two cost models, and getting the most value per dollar and per session.

## The mantra

*right-size the model, reuse the context, verify the number.*

## The arc

- **Level 1 — How Claude actually works.** Learn the mental models that don't go stale, and place a task on the capability/cost/speed axis.
- **Level 2 — Plans, limits and the two cost models.** Decide whether a workload is subscription-shaped or API-shaped, and route every figure to the docs.
- **Level 3 — Getting the most per dollar and per session.** Turn the mechanics into reflexes you run before every non-trivial task.

## Habits

- Treat the context window as working memory: everything in the conversation it can see at once, your input plus what it's writing. (1.1)
- Expect a very long chat to degrade and to cost more, and decide in advance where to start fresh and what to carry over. (1.1)
- Supply what the model can't know: anything after the training cutoff, and anything private to you. (1.2)
- Place the task on the axis — capability against cost against speed — before you pick a tier. (1.3)
- Run it twice when a single run isn't enough to trust; identical prompts can differ. (1.4)
- Read a plan tier as headroom and capability bought with money, not as a price list to memorise. (2.1)
- Learn what burns your allowance fastest, so you feel a limit coming before it cuts you off mid-task. (2.2)
- Ask the one question that splits the cost models: am I a person using Claude interactively, or building something that calls Claude? (2.3)
- Work out the shape of a workload — input-heavy, output-heavy, or repeated stable context — then pick the lever that fits it. (2.4)
- Front-load the stable context once and keep the live conversation lean; a giant paste at the top costs you every turn after. (2.5)
- Default to the balanced model, reach up only for genuinely hard reasoning, drop down for bulk and simple work. (3.1)
- Put standing context in a reusable Project setup instead of re-establishing it in every new chat. (3.2)
- Split work across parallel agents only when the subtasks are genuinely independent and time or scope matters. (3.3)
- Glance at your own meter — usage in the app, spend in the console — and forecast the month from a few days. (3.4)

## Before you trust it

- Verify every price, usage limit and model ID against the current docs in this session, or mark it unverified and link the source.
- No search this session means the figures are unverifiable. Teach yourself the framework and defer the numbers.
- Right-size three real tasks against the axis, then confirm the current model in the docs before committing. (Level 1 boss fight)
- Say subscription or API and justify it with the framework before you start pulling levers. (Level 2 boss fight)
- Design the cheapest reliable setup end to end with every changeable figure marked "verify at the docs link". (3.5)
- Check the result is calibrated, not just thrifty: under-powering a hard task is its own waste.

## Never

- Never state a price, usage limit or model ID from memory.
- Never present a stale figure as current.
- Never let "roughly" make an unverified number safe.
- Never guess a figure when you can't look it up — give the link and say it's unverifiable.
- Never reach for the most expensive model for everything just in case.
- Never minimise spend blindly; match the spend to the job.
- Never assume a single run is the answer.


The keepable version of what /ai-docent:mechanics builds with you on your own work.
