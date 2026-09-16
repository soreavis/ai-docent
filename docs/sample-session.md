# Sample session

A real first session of `foundations`, verbatim. It was run headlessly against v0.5.0 of the plugin with Claude Code: the opening turn was captured from the first invocation, and each later turn continued that same conversation with one learner message. The course's side is exactly what came back. The learner's answers were scripted to play a plausible beginner; nothing on the course's side was touched. Read it to see what a first session feels like before you install anything.

Three things worth noticing as you read. The course looks for a saved record before it starts and says what it found. It asks the core questions one at a time and skips the ones your answers already covered, though it bundled its two follow-ups about the report into one turn. And when the learner ignored a question (where the report's numbers come from), it kept the gap open on the card as a parked question rather than filling it in.

Speaker labels were added; the text is verbatim.

---

**You:** /ai-docent:foundations

**ai-docent:**

No saved progress found, so this is a first session. Welcome to Claude Foundations.

Quick note before we start: I'll verify every product claim against the official docs before stating it, and I won't touch your files or run anything unless you ask.

First question: **what should I call you?** A name or nickname is fine. It'll go on every Progress Card so you can pick up where you left off.

---

**You:** Dana

**ai-docent:**

Good to meet you, Dana.

Next: **have you used Claude, ChatGPT, or any AI assistant before?** Never, a few times, or regularly? And if so, what for?

---

**You:** A few times. ChatGPT mostly, for rewriting emails and once to explain a spreadsheet formula.

**ai-docent:**

Rewriting emails and decoding formulas is exactly the kind of thing that gets dramatically better once you know how to ask. Good starting point.

**What's your situation right now?** Studying, working, between things? What field or subjects? This gives me real material for your exercises instead of made-up examples.

---

**You:** Working. I'm in marketing at a mid-sized company, mostly campaign reporting and copy.

**ai-docent:**

Campaign reporting and copy is rich territory. Both involve repetitive structure and messy inputs, which is where Claude earns its keep.

**Coding or technical experience, 0 to 10?** 0 is "what's a file path", 10 is "I write code daily". Be honest. It only changes how I teach, never whether.

---

**You:** 2. I can open a terminal but I don't really know what to do in it.

**ai-docent:**

A 2 that can already open a terminal is a fine place to start. Claude Code does the typing anyway, and the first Claude Code lesson includes a short terminal survival kit. That also answers my terminal question, so I'll skip it.

**Now dream a bit.** If a really capable assistant handled the hard parts, what do you wish you could do? Automate reporting, write better copy faster, build a small tool, analyze campaign data, anything at all.

---

**You:** Honestly, I'd like to stop building the same weekly campaign report by hand. And write better first drafts faster.

**ai-docent:**

Both are very achievable. The weekly report is a classic automation target, and faster drafts come almost entirely from prompting skill.

**Pick one as your capstone.** One concrete thing you'd be proud to have finished in 4 to 6 weeks. My read: the weekly report is the stronger capstone, because it's a real deliverable with a clear "done", and the drafting skill gets built along the way in every lesson anyway. But it's your call.

Also tell me roughly what goes into that report today: where the numbers come from (a spreadsheet export, an ad platform, a dashboard) and where the finished report ends up (email, slides, a doc).

---

**You:** The weekly report. If that ran itself with me just checking it, I'd be proud of that.

**ai-docent:**

Capstone locked: **the weekly campaign report that runs itself, with you as the reviewer.** Good choice.

I still need the shape of it, since that decides which tools we build with. Two things:

1. Where do the numbers come from today? A CSV export, a spreadsheet, an ad platform, a dashboard?
2. Where does the finished report go? Email, slides, a doc, a chat channel?

---

**You:** Mac. 30 minutes, maybe three times a week. Tiny steps, I've bounced off tech courses before by getting lost early. Coach tone, no game mode.

**ai-docent:**

Coach voice it is, and no Game Mode. Tiny steps with lots of practice, and I'll keep the terminal parts small and safe so you never feel lost early. Noted.

Here's how I have you, Dana:

- **You:** marketing, campaign reporting and copy. Used ChatGPT a few times for email rewrites and a formula explanation.
- **Technical comfort:** 2 out of 10, on a Mac. Can open a terminal, not sure what to do in it.
- **Capstone:** a weekly campaign report that builds itself, with you as reviewer.
- **How you learn:** tiny steps, lots of practice. Burned before by courses that lost you early.
- **Sessions:** 30 minutes, about three times a week. Coach tone, no Game Mode.

Did I get you right?

One gap I still need for the plan, since it decides which tools your capstone uses: where do the report numbers come from today (CSV export, spreadsheet, ad platform), and where does the finished report end up (email, slides, a doc)?

---

**You:** Yes, that's me.

**ai-docent:**

Here's your plan, Dana. Built for 30-minute sessions and tiny steps. Every level ends with a "boss fight", a real task you do solo. It's a gate, not a test to fear: if it doesn't go, we find the gap and retry next session.

One assumption baked in: I still don't know where your report numbers come from or where the report ends up. I've assumed a spreadsheet or CSV export in, and a doc or email out. Tell me when you know and I'll adjust.

**Your Lesson Plan v1**

**Level 0: First contact** (1 session)
- 0.1 Talk to it like a colleague, not a search engine. Exercise: one campaign question asked badly, then well. Compare.

**Level 1: claude.ai fundamentals** (7 sessions)
- 1.1 Anatomy of a great prompt. Exercise: rebuild a real email-draft prompt together. (1)
- 1.2 Your voice, from your samples. Exercise: paste two pieces of your copy, get five more in that style. (1)
- 1.3 Files as fuel. Exercise: upload last week's report and have Claude summarize, then critique it. (1)
- 1.4 Artifacts. Exercise: a first draft of your report layout, built in chat. Capstone step one. (1)
- 1.5 Search and honest answers. Exercise: check two claims from a campaign brief. (1)
- 1.6 Projects. Exercise: a "Weekly Report" project with standing instructions. Capstone step two. (1)
- 1.8 Boss fight: last week's numbers to a finished report, with minimal coaching. (1)
- Cut: 1.7 memory habits. Folded into 1.6.

**Level 2: Claude Code, from zero** (8 sessions)
- 2.1 Terminal survival kit. Ten minutes, then straight into 2.2. (merged)
- 2.2 Install and first contact. Exercise: Claude Code introduces your report folder to you. (1)
- 2.3 What that command will actually do. Safe, reversible, one-way. (1)
- 2.4 The build loop. Exercise: a script that turns your export into report text. Capstone step three. (1 to 2)
- 2.5 Plan mode and staying in control. (1)
- 2.6 Git as a seatbelt. Break it on purpose, recover. Directly aimed at your "getting lost" worry. (1)
- 2.7 CLAUDE.md for the report project. (merged into 2.4 or 2.9)
- 2.9 Capstone sprint I. The report generates itself from an export. (2)
- 2.10 Boss fight: add one small feature solo. (1)
- Cut: 2.8 debugging. Woven into the sprint instead.

**Level 3: Power user** (5 sessions)
- 3.3 Data and sanity-checking numbers. Exercise: verify your report's numbers against the source. (1)
- 3.5 Repeatable workflows. Exercise: three templates for your recurring copy tasks. (1)
- 3.1 Cowork or 3.2 Connectors: whichever matches where your data lives. (1)
- 3.6 Capstone sprint II. Run it for real, on a real week. You just review. (2)
- Cut: 3.4 deep research, 3.7 boss fight (sprint II is the gate).

**Level 4: Advanced** (only when you're ready)
- 4.1 A custom command that runs the report. 4.10 scheduling it. 4.9 judgment and what never goes into a prompt. 4.11 staying current.

Roughly 21 sessions to a shipped capstone, about seven weeks at three a week. Want any changes, or shall we start Lesson 0.1 right now? It fits in what's left of this session.

---

**You:** Looks good, keep it as is. Let's start.

**ai-docent:**

**Lesson 0.1: talk to it like a colleague, not a search engine.**

**The idea.** A search engine wants keywords. Claude wants what you'd tell a sharp new colleague on their first day: what you're trying to do, who it's for, what you already have, and what "good" looks like. Everything you leave out, Claude fills in with a guess. Most disappointing AI answers aren't the model being dumb. They're the model guessing at the half of the brief you kept in your head.

**Watch one.** Illustrative example, in your world:

Search-engine style:
```
write campaign report summary
```
Colleague style:
```
I'm writing the weekly summary for our paid social campaign for the marketing director.
She reads it on her phone in 30 seconds. Last week spend was up but leads were flat.
Write 3 short bullets: what happened, why it probably happened, what we'll change this week.
Plain language, no jargon, no exclamation marks.
```
Same task. The first gets a generic template. The second gets something you could nearly send.

**Do it now.** Take one real thing from your week: a report line, a subject line, a formula, anything.

1. Write the search-engine version of the ask. One line, keywords only.
2. Paste it here, then we'll build the colleague version together before you run either one.

Step 1 only for now. What's the one-liner?

---

**You:** save

**ai-docent:**

Saved to `~/.ai-docent/progress-foundations.md`. Next session, I'll read it from there automatically. Copy of the card, in case you switch devices:

```
<!-- ai-docent:card v1 course=foundations -->
CLAUDE FOUNDATIONS — PROGRESS CARD (saved mid-session)
Student: Dana | Date: 2026-09-16 | Session #: 1
Tone: Coach
Storage: file: ~/.ai-docent/progress-foundations.md
Plan version: v1
Lessons completed: none yet (0.1 in progress — concept taught, exercise step 1 not yet started)
Levels: prompting 0/5 · claude.ai 0/5 · Claude Code 0/5 · advanced 0/5
Capstone: Weekly campaign report that builds itself, Dana reviews — status: idea — next capstone step: confirm data source (CSV/spreadsheet/ad platform) and output (email/doc/slides)
Strengths noticed: none yet
Working on: the colleague-not-search-engine rule (context, audience, what you have, what good looks like)
Review seeds: You've typed five keywords to ask Claude for a report summary. What four things are missing from the brief?
Open questions parked: where the weekly report's numbers come from and where the finished report goes
Next session: Lesson 0.1 continued — finish the bad-vs-good prompt exercise, then 1.1 if time allows (estimated 30 min)
Profile: marketing (campaign reporting + copy), tech comfort 2/10, Mac, 30 min x3/week, tiny steps, bounced off tech courses before by getting lost early, no Game Mode
<!-- ai-docent:card-end -->
```

Back to where we were: what's your one-line, keywords-only version of a real ask from this week?
