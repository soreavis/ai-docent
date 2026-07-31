# The arc — what each course is for, and who needs it

Read this when routing someone or building a full track. The eight below are the complete list; there is no ninth course.

**Use → Craft → Trust → Ship → Sustain → Secure → Afford → Build**

| # | Course | Levels | The question it answers |
|---|---|---|---|
| 1 | `foundations` | 0–4 | How do I actually use one of these, well, on my own work? |
| 2 | `prompt-craft` | 4 | Why is the output mediocre, and how do I get a better one? |
| 3 | `reliability` | 4 | How do I stop believing things that aren't true? |
| 4 | `shipping` | 4 | How do I get the work accepted by a real reviewer? |
| 5 | `long-haul` | 4 | How do I run a project for weeks without losing the thread? |
| 6 | `security` | 4 | How do I not get owned, leaked, or wrecked? |
| 7 | `mechanics` | 3 | Which model, how much context, and what is this costing? |
| 8 | `builder` | 5 | How do I build software that calls a model? |

## Routing table — symptom to course

Match what they *said*, not what they asked for. People describe symptoms, not curricula.

| What they say | Course | Why |
|---|---|---|
| "I'm brand new", "I don't know where to begin" | `foundations` | Starts from zero and builds a capstone; nothing else assumes less. |
| "The output is mediocre / generic / not what I wanted" | `prompt-craft` | This is a briefing problem, not a model problem. |
| "It made something up", "it cited a page that doesn't exist", "I trusted it and was wrong" | `reliability` | Verification habits, planted-error drills, calibrated trust. |
| "My PR was closed as AI slop", "nobody will review this", "it touched forty files" | `shipping` | Scoping, self-review, landing work with people. |
| "It forgot what we decided", "session four undid session two", "I can't restart after a break" | `long-haul` | Durable notes, handoffs, decision logs, cold resumes. |
| "It deleted something", "I'm scared to give it permissions", "what about prompt injection" | `security` | Blast radius, injection, secrets, runaway agents. |
| "The bill surprised me", "which model should I use", "I keep hitting limits" | `mechanics` | Model choice, context windows, plans and cost. |
| "I want to build an app / agent / integration with the API" | `builder` | APIs, tool use, MCP, evals, retrieval and context design. |
| "My writing/analysis work, not code" | `shipping`, else `prompt-craft` | `shipping` translates its whole curriculum for non-code deliverables; `prompt-craft` doesn't branch, but it works from whatever material you actually produce. |

Two symptoms often arrive together — "it made things up *and* my review was rejected". Take the one that costs them most this week and say why you chose it.

## Sequencing a full track

Default order is the table above. Common, correct deviations:

- **Already uses an agent daily → skim or skip `foundations`.** The most frequent adjustment. Ask first; some people want the capstone anyway.
- **Doesn't write software → `builder` is optional.** Say this out loud rather than letting eight courses feel mandatory.
- **Something is actively hurting → that course first**, then rejoin the arc. A track that ignores this week's pain gets abandoned in week two.
- **Cost or limits already biting → pull `mechanics` forward.** It's short and it removes a daily irritation.
- **Team or open-source contributor → `shipping` early**, ahead of `long-haul`. Their work meets other people sooner.

## Rough shape

Each course runs multiple sessions and adapts to the learner, so any total is an estimate — say so rather than quoting a number as a schedule. `mechanics` is the shortest; `foundations` and `builder` are the longest. Courses are independent: finishing one is a real result, and stopping there is a legitimate end, not a dropout.
