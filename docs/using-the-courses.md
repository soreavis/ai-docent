# Using the courses

## How a session runs

Every lesson has the same seven steps:

1. **Warm-up** — a question or two on last time, plus what happened since
2. **Concept** — the idea in a few sentences, with one analogy
3. **Watch one** — it demonstrates on your material
4. **Do it now** — you try
5. **Challenge** — a harder variation, minimal help
6. **Review** — one thing you did well, one to fix, with the stronger version shown next to yours
7. **Card** — the recap that lets you resume

One lesson per session by default. If you're moving fast it compresses and says so. If you're struggling it adds repetitions rather than pushing on.

The review is the part people want to skip. It's where most of the value is.

## Levels and boss fights

Courses are organised into levels. `foundations` runs 0 to 4, `builder` 1 to 5, `mechanics` 1 to 3, the rest 1 to 4.

Levels are gated by boss fights: a real task with no hints, judged against stated criteria. Failing one isn't a setback. It routes you into a remedial loop on the specific thing you missed, which is more useful than passing would have been.

Every five sessions or so you get a three-minute retro. What's working, what's dull, what to change. The plan gets a version bump when you change it.

## Progress and resuming

Each course keeps its own card, independent of the others.

**With file access.** Cards are written to `~/.ai-docent/progress-<course>.md`, falling back to `./.ai-docent/` if your home directory isn't writable. Say "continue" and it finds the file.

**Without file access.** The card is printed at the end of each session. Copy it somewhere. To resume, paste the most recent one into a new conversation. Lose it and you lose your place.

A pasted card takes precedence over the file and the chat history — but it gets checked first. The course confirms the card belongs to it, refuses to resume from another course's card, and names any missing fields instead of filling them in. If a file exists and is further along than what you pasted, it says so and asks which to use rather than quietly losing your newer work.

Hand-edit a card and that check is what catches it. Delete the `Tone:` line and you'll be asked for it again.

The two support skills keep their own cards on the same terms: `progress-start.md` tracks which courses are done, `progress-companion.md` holds the review queue. The per-course cards are unaffected.

If nothing survives at all, you won't be sent back through onboarding. Three questions — what you covered, what stuck, what's next — rebuild a card marked `reconstructed`, and you carry on from there.

You can also say **save** at any point to get the card mid-session, which is worth doing if you're about to be interrupted.

## Keeping it after the course ends

`/ai-docent:companion` is a separate skill that revises rather than teaches. It drills what's due on a widening schedule — a day, three days, a week, three weeks, then retired once you've held it twice.

It isn't guessing what to ask you. Each course writes a `Review seeds` line onto its card at the end of a lesson: one or two situations, caught while the coach was watching you work. The companion drills those first and fills gaps from the rest of the card. Courses mention it twice — at the five-session retro and when you finish — and not after every lesson, because early on there's nothing worth drilling.

It also doesn't re-interview you. Your name, tone and game-mode setting come off the newest card; the only thing it asks is how often you want to revise.

It also does what no single course can: read across all your cards at once and say which habit has gone quiet. And it has a five-minute mode for days you have nothing else.

Two limits worth knowing. It never teaches new material — if a drill exposes something you never covered, it names the course and stops. And there's no scheduler, so nothing will remind you; coming back is on you.

## Tone

Each course asks once how you want to be taught:

| Voice | What it sounds like |
|---|---|
| **Coach** | Warm and direct. Names the problem, then helps. The default. |
| **Blunt** | Verdict first, no praise for showing up, short sentences. |
| **Socratic** | Mostly questions. Slower, and more effective. |
| **Peer** | A colleague at the next desk. Assumes competence. |
| **Patient** | Defines terms, checks understanding, never implies you should know already. |
| **Formal** | Structured, no slang, numbered steps. |

Describe your own if none fit. "Like Patient but funnier" works. So does "no metaphors, ever".

Change it whenever you like, including halfway through a session. The choice is recorded on the card, so it carries over.

One thing the voice cannot do is change what's true. A blunt voice is not more certain than a warm one, and no voice gets to skip a verification or drop a hedge to sound decisive. Where the voice and the accuracy rules conflict, the rules win and the course tells you that's what happened.

## Game mode

Off by default. Turn it on in the wizard and you get XP, ranks, a streak, and badges.

Scoring is recomputed each session from what's actually logged rather than carried as a running total. If you didn't do the work, no points appear, and the course won't invent a streak it can't account for. Turn it off any time and the card drops the line.

## Accuracy

The courses verify product facts against current documentation instead of stating them from memory. Versions, prices, limits, and menu paths change, and a well-formed wrong number is worse than no number.

Two consequences worth knowing. If web search isn't available in your session, the course will teach the durable technique and refuse to give you version-specific steps, saying so rather than guessing. And it won't produce a URL it hasn't actually seen, so occasionally you'll get "check this domain for X" instead of a link.

That's deliberate. `reliability` spends a whole course on why.
