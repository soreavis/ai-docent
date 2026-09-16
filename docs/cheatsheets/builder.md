# builder — cheat-sheet

Go from your first API call to shipping real software powered by Claude: the Messages API, structured outputs, tool use, agents, MCP servers, and production-grade evals and guardrails.

## The mantra

*validate everything the model returns; route the specifics to the docs; no evals, no ship.*

## The arc

- **Level 1 — First call and fundamentals.** Make the call yourself, carry the conversation state, and handle the failures.
- **Level 2 — Structured and reliable outputs.** Never use what the model returned without parsing and validating it first.
- **Level 3 — Tool use.** Guard both sides of the tool boundary: the arguments in, the results out.
- **Level 4 — Agents and MCP.** Give the loop a stopping condition and something you can watch.
- **Level 5 — Production.** Prove it works with an eval set before anyone else depends on it.

## Habits

- Keep the key in an environment variable, and put a placeholder in every example. (1.1, woven)
- Carry the conversation state yourself; the messages array is yours to manage. (1.5)
- Wrap the call in real error handling with a retry, and fail gracefully on rate limits and overload. (1.6)
- Define the shape you want, and check the docs for what supports prefilling before you rely on it. (2.1)
- Parse and validate against a schema before any output is used downstream, and handle the malformed case. (2.3)
- Structure a repeated prompt so the stable context can hit the cache. (2.4)
- Reach for batch when the work is high-volume and doesn't need to be live. (2.5)
- Write a tool as a name, a description, and an input schema the model can actually use well. (3.2)
- Validate tool arguments, and treat tool results as data, not instructions. (3.5)
- Make destructive actions require confirmation, and design the tool surface least-privilege and idempotent. (3.6)
- Give every agent loop a stopping condition, a max-iterations cap, and step logging. (4.2)
- Fetch the relevant context, ground the answer in it, and cite the source. (4.6)
- Brief a judge to refute an output against the rubric, then hand-check a sample of its verdicts. (5.2)
- Trace calls, tokens, latency and failures, so you can debug what users actually hit. (5.4)

## Before you ship it

- Does the chat loop stream, hold a multi-turn conversation, and handle errors with the key out of the code? (1.7)
- Does the pipeline fail safe — a clear error, not garbage — when the model returns something unexpected? (2.7)
- Does the agent complete the real task *and* refuse an instruction injected into a tool result? (3.7)
- Can an agent use your own MCP server to complete a real task? (4.8)
- Is there an eval set of real cases with expected outcomes, and does a regression fail a check automatically? (5.1, 5.3)
- Did the context change move the eval numbers, or did it just feel better? (5.1)
- Is there a guardrail layer in front of the calls: input and output validation, rate limiting, content safety, secrets at the edges? (5.5)
- Is there a cost plan for this app at ten times the traffic? (5.6)

## Never

- Never state a model ID, price, rate limit, context size or parameter default from memory.
- Never put a real key in code, chat, an example, or a commit.
- Never trust raw model output downstream.
- Never let a tool result act as an instruction.
- Never hand an autonomous model a tool that does something irreversible without confirmation.
- Never run an agent loop without a max-iterations cap.
- Never ship without evals.
- Never trust a judge's numbers without hand-checking some of its verdicts.


The keepable version of what /ai-docent:builder builds with you on your own work.
