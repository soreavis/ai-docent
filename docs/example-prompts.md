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

**Deciding something**

```
I'm choosing between <A> and <B> for <purpose>. Give me the strongest
case for each, then tell me what would have to be true for each one
to be the wrong choice.
```

**Getting help with a task you'd normally do by hand**

```
Walk me through <task> one step at a time. Wait for me to finish
each step before giving me the next one.
```

Useful early on, because a wall of ten steps is where beginners lose the thread.

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

## Two habits worth skipping

**Politeness padding.** "Please could you kindly help me with" costs you nothing but adds nothing. Be direct; it isn't rude.

**Piling on emphasis.** Writing IMPORTANT in capitals, or asking three times, is not a substitute for saying the thing precisely once. If a constraint keeps getting dropped, state it as a constraint — "no more than 120 words" — rather than louder.

## Where this goes next

Everything here is Level 1 material. [`prompt-craft`](../README.md#the-courses) covers the rest: shaping output format, giving the model a role and a success criterion, breaking hard tasks into steps, and building a reusable set of prompts for the things you do repeatedly.

If your prompts are fine and the answers still aren't, the problem is probably somewhere else — [Getting started](getting-started.md) has a table for picking the right course.
