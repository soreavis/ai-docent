# Example prompts

For people who have just started. These are starting points to copy and change, not templates to follow exactly — a prompt that fits your actual situation beats a good generic one.

If you want to understand *why* these work rather than just use them, that's [`prompt-craft`](../README.md#the-courses). This page is what to type on day one.

## The four parts

Most weak prompts are weak the same way: they carry the task and leave out everything else. There are four parts that do the work — **context, task, format, constraints** — and a one-line prompt makes the model guess three of them.

A typical first attempt:

```
Write a product description for my running shoes.
```

The same request with the other three parts filled in:

```
I sell trail running shoes to people who mostly run on hills and mud,
not roads. They care about grip and ankle support, and they've usually
been let down by shoes that wore out in a season.

Write a product description for one shoe model.

Around 120 words, plain sentences, no marketing superlatives.
Don't invent specifications — I'll give you the real ones below.
```

You don't need all four every time. A quick question stays a quick question. Reach for the full shape when the answer matters or the first attempt disappointed you.

## When you don't know what to ask

The most useful beginner prompt is the one that makes the model do the work of figuring out what you need:

```
I want to <what you're trying to do>. Before you answer, ask me
three questions that would change your answer.
```

Use this whenever the task is fuzzy in your own head. It costs one extra exchange and usually saves three.

A variation for when you're stuck on wording rather than substance:

```
Here's my rough attempt. Don't rewrite it yet — tell me what's
unclear about it first.
```

## Everyday starting points

**Understanding something**

```
Explain <topic> to me. I know <what you already know> and I don't
know <what you don't>. Use an example rather than a definition.
```

```
I read this and didn't follow it: <paste>. Which part is the part
I'm missing?
```

**Writing and editing**

```
Here's a draft. Keep my voice — don't smooth it into corporate
English. Point out the three weakest sentences and say why, then
show me a stronger version of each.
```

```
Rewrite this so someone who has never heard of <the thing> can
follow it. Same length.
```

**Working with a document**

```
Here's a <contract / report / thread>. Summarise it in five bullets,
then list anything in it that I'd regret not noticing.
```

Treat the second half as the point. A summary tells you what's there; the second question is the one that catches what matters.

Two things about long documents. Paste the document first and put your question after it, not before — the model answers best the thing it read last. And for anything long, make it show its working:

```
<the document>

First pull out the passages that bear on <my question>, word for
word. Then answer using only those passages.
```

**Deciding something**

```
I'm choosing between <A> and <B> for <purpose>. Give me the strongest
case for each, then tell me what would have to be true for each one
to be the wrong choice.
```

When you haven't got options yet, ask for them before you ask for an answer. The first idea it has is rarely its best one:

```
Give me three different ways to <do the thing>. Say what each one is
bad at. Then recommend one and say why.
```

**Getting help with a task you'd normally do by hand**

```
Walk me through <task> one step at a time. Wait for me to finish
each step before giving me the next one.
```

Useful early on, because a wall of ten steps is where beginners lose the thread.

**Learning something properly**

```
I've just read about <topic>. Ask me five questions to find out
whether I actually understood it, one at a time. Don't tell me the
answers until I've tried.
```

```
I'll explain <topic> back to you in my own words. Tell me what I got
wrong or left out, and don't be generous about it.
```

Explaining something back is the fastest way to find the hole in your own understanding. This is the one place where being marked harshly is the point.

**Email and messages**

```
Draft a reply to this. I want to say <what you actually mean>, but
without <what you want to avoid — sounding annoyed, over-promising,
being blunt with a client>. Keep it short.
```

```
Is this message clear about what I'm asking for, and what happens
next? Point at the sentence that does each. If one is missing,
say so.
```

The second one catches the most common failure in a work message — being polite and complete but never actually stating the ask.

**Meetings and messy notes**

```
Here are my raw notes. Pull out: decisions made, things someone
committed to doing, and open questions nobody answered. Leave
anything that fits none of those in a fourth list rather than
dropping it.
```

That last clause matters. Without it you get a tidy summary and no way to tell what was quietly discarded.

**Planning before doing**

```
Don't start yet. First give me a plan for <task> — the steps, in
order, and where you think it's most likely to go wrong. I'll tell
you when to begin.
```

Worth the extra step whenever the task takes more than one move, because a wrong plan is much cheaper to fix than wrong work.

## Prompts that make the answer checkable

An answer that sounds right and an answer that is right look identical. These are worth building into your habits early — and they're what [`reliability`](../README.md#the-courses) is about in full:

```
Mark anything in that answer you're not confident about, and say
what you'd need to check it.
```

```
Where did each of these facts come from? If you're going from
memory rather than something you looked up, say so.
```

```
What would make this answer wrong?
```

The last one is the highest-value question on this page. It's also the one nobody asks.

A cheaper check that needs no prompt at all: ask the same question again in a second chat. Where the two answers disagree is where it's guessing.

All three ask the same model to doubt itself, which it does half-heartedly. When the answer matters, hand it to a fresh chat whose only job is to knock it down:

```
Your job is to refute this, not to review it. Find the strongest
reason it is wrong. Point at the exact sentence, say what's wrong
with it, and say what evidence would settle the question. If you
can't find one, say "I could not refute it" — not "this looks right".
```

Paste only the answer, never the conversation that produced it — a chat that wrote something will defend it. For a single claim rather than a whole answer, the same shape works:

```
Someone claims: <the claim>. Try to refute it. Quote what you're
relying on, and if you'd have to look something up to be sure, say
what and don't guess.
```

Three things to know before you trust the result. "I could not refute it" means the answer survived one attempt, not that it's right. A refutation that doesn't point at a sentence and give a reason is noise — ignore it. And check the refutation itself before acting on it, because the refuter can invent a flaw as easily as the author invented a fact. When the stakes are high, run it two or three times in separate chats and compare: one grounded refutation outweighs any number of "could not refute".

## Fixing a bad answer

The instinct is to start a new chat. Steering the existing answer is usually faster:

```
Closer. Keep the second and third points, cut the first, and make
the tone flatter.
```

```
Too general. Redo it using my actual numbers below, and if something
doesn't follow from them, say so instead of filling the gap.
```

Say what to keep as well as what to change. Only saying what's wrong tends to lose the parts that were working.

A few more, for the failures you'll hit most:

```
That's too long. Same content, half the words, nothing important cut.
```

```
You've changed my meaning in the third paragraph. Put it back to what
I said and only fix the grammar.
```

```
Stop expanding it. I want it shorter each time, not longer.
```

## Saying what "good" looks like

The model can't tell whether it succeeded unless you say what success is. Two short additions do most of the work:

```
You're reviewing this as <the person who'll actually receive it —
a hiring manager, a sceptical client, a tired reader on a phone>.
It's good if <what would make it work>. Tell me whether it clears
that bar, then fix it so it does.
```

Naming the reader changes the whole answer more than any amount of extra instruction about tone.

## Showing it an example

An example does more than a paragraph of description, and it's the thing beginners most often leave out. For style or format, one finished sample is enough:

```
Here's one I wrote that I like: <paste>. Make three more in the same
style, on <topics>. Match the length and the tone; don't reuse the
content.
```

When the task has steps or a judgement inside it, show one *worked* example — the input, how you got from it to the output, and the output — so it copies the method rather than the look:

```
Here's one done the way I want, including how I got there.

Input: <what you started from>
Steps: <the two or three moves you made, in order>
Output: <the result>

Now do the same for: <new input>. Show the steps the same way.
```

When the failure is easier to show than to describe, put a bad one next to the good one:

```
Good: <paste>
Bad: <paste> — bad because <the reason>.
Make five more like the good one.
```

Examples pull harder than instructions, so check what yours accidentally teaches. If your one example is long, has three bullets and is about sales, you'll get long, three-bullet answers about sales. Vary the part that should vary across two or three examples, and include the awkward case, not only the easy one.

## Controlling the shape of the answer

Say the format outright rather than hoping:

```
Answer as a table with one row per option and columns for cost,
effort, and main risk. No preamble.
```

```
Give me three options, one line each. No explanation unless I ask.
```

"No preamble" and "no explanation unless I ask" are worth remembering. A lot of the bulk in an answer is throat-clearing you never wanted.

## Stopping it from guessing

Better said up front than corrected afterwards:

```
If you don't know something here, say "I don't know" rather than
giving me your best guess. A gap I can see is more useful than a
confident answer I have to check.
```

```
Use only what I've given you below. Don't add facts from elsewhere,
and if something's missing, tell me what's missing instead of
filling it in.
```

The second one is the single most useful constraint when working from your own document, because filling a gap plausibly is exactly what you won't notice.

## Turning something that worked into a reusable prompt

When an exchange goes well, don't lose it:

```
That worked. Write me a reusable prompt that would get that result
in one go next time, with <the parts that change> marked as blanks
I fill in.
```

Do this two or three times and you have a small personal set of prompts for the things you do every week — which is where the real time saving is, rather than in any individual clever prompt.

## Two habits worth skipping

**Politeness padding.** "Please could you kindly help me with" costs you nothing but adds nothing. Be direct; it isn't rude.

**Piling on emphasis.** Writing IMPORTANT in capitals, or asking three times, is not a substitute for saying the thing precisely once. If a constraint keeps getting dropped, state it as a constraint — "no more than 120 words" — rather than louder.

## Where this goes next

Everything here is a starting point, and mostly Level 1 material. [`prompt-craft`](../README.md#the-courses) covers the same ground properly and keeps going: teaching by example rather than instruction, breaking hard tasks into steps, asking for options before an answer, getting the model to critique its own draft, deciding what the model sees at all rather than only how you word it, working out whether one prompt is genuinely better than another instead of assuming, and promoting the ones that win into standing instructions so you stop retyping them.

If you only keep four things from this page: fill in the parts you left out, make it interview you when the task is fuzzy, say what "good" looks like, and ask what would make the answer wrong — then, when it matters, have a fresh chat try to refute it.

If your prompts are fine and the answers still aren't, the problem is probably somewhere else — [Getting started](getting-started.md) has a table for picking the right course.
