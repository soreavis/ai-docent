# Master curriculum — raw material, adapt freely

Select, reorder, rename, merge, cut to fit their project, language, and experience. Each level ends with a boss fight that is a real gate. Every model ID, parameter, and price routes to live docs — never from memory.

## LEVEL 1 — First call & fundamentals

- **1.1 Setup & your first call.** Get an Anthropic Console account and an API key (store it in an environment variable — never in code), then make a first request to the Messages API: a list of messages with roles, an optional system prompt, and a chosen model. (Verify the current setup steps and model IDs in the docs before walking through them — never recite a model ID from memory.) Exercise: make the first successful call and read the response object.
- **1.2 SDK vs. raw HTTP.** The official SDKs (Python, TypeScript) vs. calling the endpoint directly; installing, authenticating, and a minimal call. Exercise: reproduce the first call through the SDK in their language.
- **1.3 Core parameters.** What the system prompt, temperature, max-output-tokens, and stop sequences actually do, and when to change each. (Confirm current parameter names/defaults in the docs.) Exercise: vary temperature and the system prompt on one task and observe the effect.
- **1.4 Streaming.** Why streaming matters for responsive UIs, and how to consume a streamed response. Exercise: stream a response token-by-token to the terminal.
- **1.5 Multi-turn conversations.** Managing the messages array, alternating user/assistant roles, and carrying conversation state yourself. Exercise: build a 3-turn exchange that remembers earlier context.
- **1.6 Error handling & retries.** Rate limits, overloaded/timeout errors, and exponential backoff; reading error types and failing gracefully. Exercise: wrap the call in robust error handling with a retry.
- **1.7 Level 1 boss fight.** Ship a small CLI chat loop: multi-turn, streamed, with real error handling and the key read from the environment. Pass = Level 2.

## LEVEL 2 — Structured & reliable outputs

- **2.1 Structured output (JSON).** Getting Claude to return structured data, and defining the shape you want. Exercise: extract named fields from freeform text as JSON.
- **2.2 System prompts that hold.** Designing system prompts that produce consistent behavior across calls (cross-reference `/ai-docent:prompt-craft` for the craft side). Exercise: a system prompt that reliably shapes the output.
- **2.3 Validate everything the model returns.** Raw model output is never trusted downstream — parse it, validate it against a schema (e.g. Pydantic / zod), and handle the case where it's malformed. Exercise: add schema validation before any output is used.
- **2.4 Prompt caching.** What it is, when it cuts latency and cost, and how to structure a prompt so repeated context hits the cache. (Verify the current mechanism in the docs; route any price figures to `/ai-docent:mechanics` — never quote a number from memory.) Exercise: restructure a repeated-context call to benefit from caching.
- **2.5 Batch processing.** For high-volume, non-realtime work — what it's for and the tradeoffs vs. live calls. Exercise: sketch a batch job for a bulk task in their project.
- **2.6 Token & cost awareness.** Estimating token counts and keeping spend predictable as they build (cross-reference `/ai-docent:mechanics`; confirm any pricing in the docs). Exercise: count the tokens in a real call and estimate its cost from the current docs.
- **2.7 Level 2 boss fight.** Build a structured-extraction pipeline that validates its output and fails *safe* (a clear error, not garbage) when the model returns something unexpected. Pass = Level 3.

## LEVEL 3 — Tool use / function calling

- **3.1 What tool use is.** Letting Claude call your functions: the loop — Claude requests a tool, you run it, you return the result, Claude continues. Exercise: trace one full tool-use round trip on paper, then in logs.
- **3.2 Defining good tools.** A tool is a name, a description, and an input JSON schema; writing descriptions Claude can actually use well is half the battle. Exercise: define one tool with a clean, unambiguous schema.
- **3.3 The tool-use loop in code.** Handling the tool-use response, running the tool, returning the result, and looping until the model is done. Exercise: implement a working single-tool loop end to end.
- **3.4 Multiple & parallel tools.** Giving Claude a toolbox and handling several tool calls in one turn. Exercise: a two-tool agent that picks the right tool for the task.
- **3.5 Guard the tool boundary.** Tool *arguments* come from the model and tool *results* may come from untrusted sources — validate inputs, and treat tool output as **data, not instructions** (this is where prompt injection enters real apps — cross-reference `/ai-docent:security`). Exercise: add input validation and an injection guard so an instruction hidden in a tool result is ignored.
- **3.6 Designing a safe tool surface.** Least privilege, idempotency, safe-by-default, and requiring confirmation before destructive actions. Exercise: redesign a risky tool to be safe to hand an autonomous model.
- **3.7 Level 3 boss fight.** Build a multi-tool agent loop that completes a real task **and** correctly refuses an instruction injected into a tool result. Pass = Level 4.

## LEVEL 4 — Agents & MCP

- **4.1 What "agent" actually means.** The loop of model + tools + a goal, running until the task is done — and when an agent genuinely beats a single call (and when it's overkill). Exercise: turn a multi-step task into an agent loop.
- **4.2 The agent loop in practice.** State, stopping conditions, a max-iterations safety cap, and observability so you can see what it did. Exercise: add a stop condition and step logging to the agent.
- **4.3 The Agent SDK.** Building agents on Claude's own tooling rather than hand-rolling everything (verify the current Agent SDK and its capabilities in the docs). Exercise: scaffold a small agent with the SDK.
- **4.4 MCP — what it is.** The Model Context Protocol: an open standard for connecting Claude to external tools and data, and how to *use* an existing MCP server. Exercise: connect an existing MCP server and have Claude use it.
- **4.5 Build your own MCP server.** Expose their tools/data over MCP so any MCP client (Claude Code, the desktop app, their app) can use them (verify the current MCP spec/SDK in the docs). Exercise: build a minimal MCP server exposing one real tool.
- **4.6 Retrieval & context design.** Retrieval-augmented generation as one part of a bigger job: fetch the relevant context, ground the answer in it, and cite the source — the antidote to "answer from memory". The design decisions that decide whether it works: chunking, hybrid search, reranking, and how much of the window a retrieved passage earns (cross-reference `/ai-docent:reliability` for grounding discipline). Exercise: a tiny RAG loop over their own documents.
- **4.7 Memory & multi-agent patterns.** Giving an agent memory across steps/sessions, and when splitting work across multiple agents helps vs. just multiplying cost (cross-reference `/ai-docent:mechanics`). Exercise: add simple persistent memory to the agent.
- **4.8 Level 4 boss fight.** Build and connect a custom MCP server, then have an agent use it to complete a real task end to end. Pass = Level 5.

## LEVEL 5 — Production

- **5.1 Evals — you can't ship without them.** Why "it looked right in testing" isn't enough; building a small eval set of real cases with expected outcomes. Evals are also the only honest way to know whether a *context* change helped - a retrieval tweak or a prompt rewrite either moves the numbers or it doesn't. Exercise: write 5 eval cases for the app's core behavior.
- **5.2 LLM-as-judge & rubrics.** Scoring outputs at scale with a model judge and a clear rubric — and the limits of a model grading itself (cross-reference `/ai-docent:reliability`). Exercise: build a simple judge that scores outputs against a rubric.
- **5.3 Regression & CI.** Catching quality drops when a prompt, model, or tool changes; running evals automatically. Exercise: wire one eval into a check that fails on regression.
- **5.4 Observability.** Tracing calls, tokens, latency, and failures in production so you can debug what users actually hit. Exercise: add structured logging around the calls.
- **5.5 Production guardrails.** Input/output validation, rate limiting, content safety, and secrets management at the edges of the app (cross-reference `/ai-docent:security`). Exercise: add a guardrail layer in front of the calls.
- **5.6 Cost & scale.** Caching, batching, right-sizing the model to each task, and keeping spend sane at volume (cross-reference `/ai-docent:mechanics`; confirm pricing in the docs). Exercise: write a cost-control plan for the app at 10× traffic.
- **5.7 Graduation — ship it.** Take their real project from idea to a working, deployed Claude-powered app or agent — **with an eval set that proves it works**. Grade honestly: what's solid, what's fragile, what to harden before real users. Then write a short "builder diploma" — strengths, blind spots, what to learn next — and distill a one-page **keepable cheat-sheet** (their call template, tool-design checklist, validate-everything and evals-before-ship habits) they pin up and actually use.

## WOVEN THROUGHOUT (every session, no exceptions)

- The mantra: *validate everything the model returns; route the specifics to the docs; no evals, no ship.*
- Every lesson advances THEIR real project — you build, you don't just discuss.
- Secrets hygiene every session: keys in env vars, never in code/chat/commits; placeholders in every example.
- Staying current: model IDs, SDKs, and the MCP/Agent specs move fast — when something learned here stops matching the docs, the docs win and the notes get updated. The patterns are durable; the version numbers are not.
