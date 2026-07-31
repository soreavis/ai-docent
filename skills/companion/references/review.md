# Building and running the review queue

## What makes a good item

An item is a thing they should be able to **do or decide**, posed as a situation. Not a definition to recite.

| Weak item | Strong item |
|---|---|
| "What is prompt injection?" | "A page you asked it to summarise contains 'ignore previous instructions'. What do you check before acting on the summary?" |
| "Name the review steps." | "The agent touched fourteen files and the tests pass. What do you look at first?" |
| "What is a context window?" | "Session four contradicts a decision from session two. Where should that decision have been written?" |

Draw the situation from their own work when a card records one — a real bounced pull request or a logged drift incident beats anything invented, and they will remember the answer because they lived it.

## Where items come from

**Start with the `Review seeds` line.** Every course card carries one: one or two situations the course itself flagged at the end of a lesson, written by the coach who watched them do it. These are the best items you will get, because they came from the moment rather than from a lesson title. Take them first, verbatim where they're already well-phrased.

Seeds only hold the newest five per course, so an older card has fewer than the lessons it lists. That's expected — fall back to the fields below for anything the seeds don't cover, and never manufacture a seed that isn't there.

Read what each card actually records. Never invent a lesson they did not cover.

| Course | Mine these fields |
|---|---|
| `foundations` | lessons completed, capstone milestones |
| `prompt-craft` | lessons completed, their prompt library |
| `reliability` | the "caught it" log, unrevealed planted errors, high-stakes zones |
| `shipping` | the Landed log — every bounce is a ready-made item |
| `long-haul` | the Drift log, scaffolding in place, "resumable right now?" |
| `security` | the "Close calls" log, levels per area, the guardrails they installed |
| `mechanics` | lessons completed, whatever cost decision they made |
| `builder` | levels per area, what they shipped |

Six to twelve items per course. A queue too big to face is a queue nobody opens.

## The schedule

A plain ladder. Each item carries the interval it is on and when it was last seen.

**1 day → 3 days → 1 week → 3 weeks → retired**

- Held it? Move up one rung.
- Missed it? Drop to the bottom rung. Not a punishment, just where it belongs.
- Held it twice running at the top rung? Retire it, and say so — visible progress matters more here than in a course, because revision has no levels to clear.
- Away long enough that everything is overdue? Don't drill forty items. Take the eight most valuable and reset the rest to the bottom rung.

This ladder is a reasonable default, not a research finding — say so if they ask, and adjust it if they prefer something else. What matters is that the interval grows when they succeed and collapses when they don't.

## Running a drill

1. Pose the situation. Do not hint.
2. Let them answer fully. No interruptions, no leading.
3. Say plainly whether it holds. One line of why. Show the stronger answer only if theirs missed something real.
4. Record it: held or missed, and which rung it moves to.

Eight items is a session. Past that, accuracy drops and it becomes a chore.

## When a drill exposes a real gap

Sometimes they miss an item because they never learned it, not because they forgot. Tell them which course covers it and stop.

Do not teach it here. A course lesson has exercises, a boss fight and a progress card behind it; a paragraph from you has none of that, and the course that owns it will never know it was covered.

## Honesty

Everything in the queue traces to a card you read or something they told you this session. If you cannot trace an item, drop it.

Never record an item as held unless they answered it correctly in front of you. An inflated queue is the same failure as an inflated XP total: it tells them they know something they do not, which is the exact opposite of the job.
