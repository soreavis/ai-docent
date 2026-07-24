# Master curriculum — raw material, adapt freely

Select, reorder, rename, merge, and cut to fit the learner. Each level ends with a boss fight that is a real gate.

## LEVEL 1 — Foundations of a great prompt

- **1.1 The anatomy of a prompt:** the four parts that carry the load — context, task, format, constraints. Why a one-liner underperforms: you're making Claude guess the other three. Exercise: take a real one-line prompt of theirs and label what's missing; add the missing parts and compare answers.
- **1.2 Specificity beats hope:** vague asks get average answers; the fix is concrete detail (audience, purpose, scope, what "good" looks like). Exercise: rewrite a vague prompt three times, each more specific, and watch the output sharpen.
- **1.3 The "ask Claude to ask YOU first" trick:** for anything fuzzy, have Claude interview them before answering ("ask me 3 questions that would change your answer"). Exercise: run a real task this way and see how much better the result is than a cold first attempt.
- **1.4 Give it a role and a goal:** telling Claude who it's being and what success looks like reshapes the whole answer. Exercise: same task, with and without a clear role + success criterion; compare.
- **1.5 The iteration loop — refine, don't restart:** how to steer an answer with targeted follow-ups ("more like X, less like Y, keep the third point") instead of starting a new chat. Exercise: take one mediocre answer to exactly-right in four refinements.
- **1.6 Diagnosing a failed prompt:** when an answer is bad, the prompt usually is too — a quick checklist (missing context? unclear task? no format? conflicting constraints?). Exercise: they bring a prompt that disappointed them; diagnose and fix it together.
- **1.7 Level 1 boss fight:** take a genuinely vague real prompt and rebuild it into a great one — then run both and prove the before/after difference out loud. Pass = Level 2.

## LEVEL 2 — Shaping the output

- **2.1 Show, don't just tell (few-shot):** giving one or two examples of what you want is the single biggest lever for format and style. Exercise: "here's one I like, make five more in this exact style" on their real material.
- **2.2 Role & system prompts — and where they live:** the difference between a one-off role and a *standing* instruction; in claude.ai that standing layer is a Project's custom instructions / project knowledge (verify the current setup in the docs before walking them through it). Exercise: move a role they keep retyping into a Project so every chat inherits it.
- **2.3 Controlling format:** asking for exactly the shape you need — a tight list, a table, Markdown, or clean JSON — and why naming the format up front beats reformatting after. Exercise: get the same content as a table, then as JSON, then as a three-bullet summary.
- **2.4 Length & tone control:** dialing answer length ("two sentences", "one tight paragraph") and tone ("plain", "formal", "blunt") on purpose instead of accepting the default wall of text. Exercise: take one answer and produce three calibrated versions.
- **2.5 Constraints & negative instructions:** telling Claude what NOT to do ("no preamble, no caveats, don't invent statistics") and setting hard boundaries. Exercise: strip the fluff from a verbose answer with constraints alone.
- **2.6 Delimiters & structure:** separating *instructions* from the *content* Claude should act on (headings, quotes, fenced blocks) so it never confuses the two — a habit that also quietly reduces prompt-injection risk (see `/ai-docent:security`). Exercise: restructure a messy prompt so instructions and source material are clearly separated.
- **2.7 Give it your voice and your world:** generic output is usually a context failure, not a model failure - it writes like everyone because it knows writing in general and nothing about *you*. Feeding the voice, the history, the constraints, and the samples *before* the ask, rather than editing the genericness out afterwards. Exercise: run the same request cold, then with a voice-and-context brief attached, and name what changed.
- **2.8 Level 2 boss fight:** hit an exact spec — a given format + tone + length — in a single prompt, no back-and-forth. Pass = Level 3.

## LEVEL 3 — Reasoning & complex tasks

- **3.1 Ask for the thinking:** prompting for step-by-step reasoning on problems where the first instinct is often wrong (logic, math, multi-constraint decisions). Exercise: a problem Claude flubs when rushed, solved correctly when asked to reason first.
- **3.2 Decompose big tasks:** breaking one overwhelming ask into ordered stages, each a clean sub-prompt. Exercise: take a task that fails as one giant prompt and nail it as a sequence.
- **3.3 Chained prompts:** feeding the output of one step as the input to the next, deliberately — and where to check between steps. Exercise: build a two- or three-step chain for a real workflow of theirs.
- **3.4 Self-critique & refine:** "now critique your own answer against these criteria, then improve it" — making Claude its own first editor. Exercise: run a draft through a self-critique pass and measure the lift. (For *honest* critique that doesn't just flatter, borrow the anti-sycophancy moves from `/ai-docent:reliability`.)
- **3.5 Handling ambiguity:** teaching Claude to surface assumptions and offer options instead of guessing, when the task is genuinely underspecified. Exercise: an ambiguous request answered well by making the ambiguity explicit.
- **3.6 Let it plan before it acts:** for big or risky tasks, ask for a plan/outline first, approve it, then execute — fewer wasted full attempts. Exercise: plan-then-build a real deliverable.
- **3.7 Level 3 boss fight:** take a hard multi-step task that fails as a single prompt and get it right via decomposition + chaining, narrating the strategy. Pass = Level 4.

## LEVEL 4 — Systems & reuse

- **4.1 From prompt to template:** turning a prompt that worked into a reusable template with clearly marked fill-in slots. Exercise: convert their best recent prompt into a template they can reuse tomorrow.
- **4.2 Your personal prompt library:** organizing templates by task type so they stop reinventing them — a library they actually open. Exercise: start the library with the three prompts they'd use most.
- **4.3 A catalog of patterns:** the reusable shapes worth knowing by name (few-shot, role+goal, plan-then-do, critique-then-revise, extract-to-format, interview-me) and when each fits. Exercise: match three of their real tasks to the right pattern.
- **4.4 Meta-prompting:** using Claude to write and improve prompts ("here's my prompt and the weak output — rewrite the prompt to fix it"). Exercise: improve a stubborn prompt by prompting for a better prompt.
- **4.5 Context engineering - designing what the model actually sees:** the discipline that sits above prompt wording: deciding what occupies the window at all. Three moves worth naming - *state management* (when to summarize, when to drop, when to persist), *context budgeting* (what earns the limited space, and what you are paying to re-send every turn), and *reference design* (how you organize the material the model can pull in, so it is findable rather than merely present). The wording matters less than the contents once a task runs longer than a single exchange. (For projects spanning days, `/ai-docent:long-haul`; for the cost of a full window, `/ai-docent:mechanics`; for building this into software, `/ai-docent:builder`.) Exercise: take a task where their prompt is already good but the output still misses, and fix it by changing what the model sees rather than what it is told.
- **4.6 Evaluating prompts honestly:** simple A/B comparisons and a lightweight rubric so they *know* a change helped instead of assuming it — and how to judge fairly without fooling themselves (lean on the honest-evaluation and second-opinion techniques in `/ai-docent:reliability`). Exercise: A/B two versions of a real prompt and score them on a 3-point rubric.
- **4.7 Promote your best prompts:** turning the winners into standing infrastructure — Project custom instructions, saved templates, a Claude Code CLAUDE.md (verify the current mechanism in the docs). Exercise: install one battle-tested prompt as a standing instruction and confirm it changes behavior.
- **4.8 Graduation — the prompt library + cheat-sheet.** Assemble everything into a real, organized **prompt library** for the work they do, plus a one-page **keepable cheat-sheet** (go-to patterns, before/after checklist, the "ask me first" habit) they pin up and actually use. Final exam: take one real recurring task and engineer a reusable, *tested* prompt for it end to end — context, format, constraints, an example, and an A/B that proves it beats the old approach. Grade honestly: what's strong, what's still weak, what to practice. Then write a short "prompt craft diploma" — strengths, blind spots, and the three habits to keep forever.

## WOVEN THROUGHOUT (every session, no exceptions)

- The mantra: *the prompt is the spec; specificity beats hope; test, don't trust.*
- Every technique gets applied to THEIR real prompts and tasks, never toy examples.
- Always show the before/after — a technique that can't beat the old prompt in a live comparison doesn't get claimed.
- Staying current: Claude's products change fast — when something learned here about *where a feature lives* stops matching what they see, trust the product, check the docs, update the notes. The prompting craft is durable; the buttons move.
