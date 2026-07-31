# The companion

`/ai-docent:companion` revises. It doesn't teach.

Courses hand you a lesson and the session ends. Nothing brings it back, and each course only ever sees its own card, so no part of the system is watching whether the habits from three courses ago are still there. That's this skill's whole job.

## When to open it

After you've finished a course, or at least a few lessons of one. Before that there's nothing to revise — it builds its queue *from* your course cards rather than inventing material, and if you run it cold it will say so and point you at `/ai-docent:start`.

## The first run

It reads every `~/.ai-docent/progress-*.md` it can find and takes your name, your chosen voice, and your game-mode setting off the newest one. Those were already answered by a course, so it doesn't ask again — it tells you what it picked up in a line, so a wrong guess costs you a second to correct.

The only thing it asks is how often you want to revise. That's the one fact no card records.

On a chat surface with no filesystem, paste the cards for the courses you want covered. One is enough to start.

## Three modes

| Say | What you get |
|---|---|
| **drill** *(default)* | What's due, oldest first, capped at eight items. 10–20 minutes. |
| **five minutes** | The three most overdue. No queue admin, no retro. |
| **retro** | Reads every card and names at most three things — which habit has gone quiet, which course you haven't touched, whether the levels you claim match how you just performed. |

## Where the questions come from

Each course writes a `Review seeds` line onto its card at the end of a lesson: one or two situations, caught while the coach was watching you work. The companion drills those first, because a seed written in the moment beats anything reconstructed from a lesson title afterwards.

Seeds keep only the newest five per course, so older cards have fewer than the lessons they list. The companion fills the gaps from the rest of the card — the "caught it" log in `reliability`, the Landed log in `shipping`, the Drift log in `long-haul`. Six to twelve items per course is the target. A queue too big to face is a queue nobody opens.

Items are situations, not definitions:

```
It:   Fourteen files changed and the tests pass. What do you look at first?
You:  Whether the tests actually cover the change.
It:   Good, but that's second. First is what the change does that nobody
      asked for — the tests can't tell you about the scope creep. Moving
      this one up a rung anyway; you got the harder half.
```

## The schedule

**1 day → 3 days → 1 week → 3 weeks → retired.**

Hold an item and it moves up a rung. Miss it and it drops to the bottom — not a punishment, just where it belongs. Hold it twice at the top rung and it retires, and you're told, because revision has no levels to clear and you need to see something moving.

Come back after a long gap and it won't dump forty overdue items on you. It takes the eight most valuable and resets the rest.

## What it won't do

**Teach you anything new.** If a drill exposes something you never covered, it names the course and stops. A paragraph from the companion has no exercise, no boss fight and no progress card behind it, and the course that owns the material would never know it had been covered.

**Remind you.** There's no scheduler in this architecture. The widening ladder only works if you come back on your own. Ten minutes a week beats an hour a month, and nothing will chase you for either.

**Score you generously.** An item counts as held only if you answered it correctly in front of it. With game mode on, XP is recomputed from the log each session rather than carried forward — an inflated queue would tell you that you know something you don't, which is the exact opposite of the job.

## Its own card

The queue lives at `~/.ai-docent/progress-companion.md` — items, which rung each is on, what you missed, which courses have gone quiet. Same rules as every other card: say **save** at any point to get it mid-session, and it's checked rather than trusted on read. A course card pasted into it is treated as source material for items, never mistaken for the queue itself.

## When it says there's nothing to do

"Nothing is due" is a normal answer, not a fault — items sit a day, then three, then a week, then three weeks apart. It will offer a retro or the items retiring soonest instead of manufacturing a drill to fill the time.

If you've retired everything, it says so and names the course you haven't touched.
