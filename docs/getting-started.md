# Getting started

## Before you begin

Install the plugin or the skill zips using the table in the [main README](../README.md#install). Nothing here works until that's done.

Have something real in mind. Not a practice project. The courses build every exercise around work you actually care about, and they get noticeably worse if you feed them a toy example.

## Pick a course, or let it pick

If you know what's wrong, open that course directly:

```
/ai-docent:reliability
```

If you don't, run the launcher:

```
/ai-docent:start
```

It asks your name, what's going wrong in plain words, and whether you want one course or all eight in order. Then it hands you a command. It doesn't teach anything itself.

A rough guide to the eight, in arc order:

| Course | Open it when |
|---|---|
| `foundations` | You're new, or self-taught and full of gaps |
| `prompt-craft` | The output is mediocre and you don't know why |
| `reliability` | You believed something it made up |
| `shipping` | Your work gets rejected, rewritten, or ignored |
| `long-haul` | Projects fall apart after a few days |
| `security` | You're nervous about permissions, secrets, or injection |
| `mechanics` | Model choice, context limits, or the bill confuse you |
| `builder` | You're writing software that calls a model |

## The first session

Four parts. How long it takes depends on your answers, and the wizard asks how long you want sessions to run.

**The wizard.** Six core questions, plus whichever branch questions apply to your answers — usually nine or ten in total, one at a time, and it reacts to your answers rather than marching through a form. It asks your name first. Somewhere in there it asks how you want to be taught, and whether you want the gamified version. Answer honestly, particularly about your current level. Overstating it produces a plan that skips what you actually need.

**Placement.** If you say you're already past the basics, the course doesn't take your word for it: three short questions from the level below the one you want, then it places you on what you answered. A level you didn't sit is recorded as placed, never as passed.

**The plan.** It reads the full curriculum, then builds a version for you: courses reordered, lessons merged or cut, weighted toward whatever is hurting. You get it as a numbered list before anything starts. Change it. That's the point of showing it to you.

**The first lesson.** Concept in a few sentences, then it does the thing on your real material, then you do it, then a harder variation. Hints escalate if you ask: a nudge, then a direction, then a walkthrough.

**The card.** Every session ends with a Progress Card. If your agent can write files, it lands at `~/.ai-docent/progress-<course>.md` and the course tells you the exact path the first time. Otherwise it's printed in the chat, and it's your save file.

## An example exchange

The short version of a real first session, from the [sample session](sample-session.md):

```
You:        /ai-docent:foundations
ai-docent:  No saved progress found, so this is a first session.
            [...] First question: what should I call you?
You:        Dana
ai-docent:  Good to meet you, Dana. Next: have you used Claude, ChatGPT,
            or any AI assistant before?
You:        A few times. ChatGPT mostly, for rewriting emails [...]
ai-docent:  Rewriting emails and decoding formulas is exactly the kind of
            thing that gets dramatically better once you know how to ask.
            [...] What's your situation right now?
```

The full transcript runs through the wizard, the lesson plan, the first lesson and a mid-session save.

That's the shape. It works from your proposal, not a sample one.

## The second session

Open the same course again and say "continue". It reads the card, gives you a one-line recap, asks a couple of questions about the last lesson, then moves on.

If you're in a plain chat window with no file access, paste your most recent card first. A pasted card overrides the file and the chat history — but it gets checked before it's trusted, so a card from a different course won't be resumed from and missing fields get named rather than invented.

## After the first course

Two skills exist that aren't courses.

`/ai-docent:start` picks a course for you if you don't know where to begin, and can run all eight in order as one tracked program.

[`/ai-docent:companion`](companion.md) drills what you've already covered so it doesn't fade. Each course writes a `Review seeds` line onto its card at the end of a lesson, and the companion works from those. It's worth opening once you've finished a course or two — before that there's nothing to revise, and it will tell you so.
