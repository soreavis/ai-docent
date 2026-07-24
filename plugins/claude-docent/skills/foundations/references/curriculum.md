# Master curriculum — raw material, adapt freely

Select, reorder, rename, merge, and cut to fit the learner. Each level ends with a boss fight that is a real gate.

## LEVEL 0 — First contact *(skip or compress if they're not a total beginner)*

- **0.1 Meet Claude:** what Claude is, what it's good and bad at, the one golden rule (talk to it like a smart colleague, not a search engine). Exercise: ask the same question badly and well, compare results.
- **0.2 The conversation loop:** iterating instead of restarting, asking follow-ups, saying "no, more like this". Exercise: refine one answer through 4 rounds until it's exactly right.

## LEVEL 1 — Claude (claude.ai) fundamentals

- **1.1 Anatomy of a great prompt:** context + task + format + constraints. The "ask Claude to ask YOU questions first" trick. Exercise: write a prompt for something from their real life; critique it and rebuild it together. (For depth, point to `/claude-docent:prompt-craft`.)
- **1.2 Giving examples & setting format:** few-shot prompting in plain language — "here's one I like, make 5 more in this style"; controlling length, tone, structure. Exercise: generate something in THEIR style from samples they paste.
- **1.3 Files as fuel:** uploading PDFs, documents, screenshots, photos; summarize, extract, compare, translate, critique. Exercise: bring a real document (school paper, contract, manual, anything) and put Claude to work on it.
- **1.4 Artifacts:** Claude builds documents, diagrams, and small interactive apps right in the chat — and you iterate on them like a designer giving feedback. Exercise: build a tiny personal tool (habit tracker, quiz, calculator) without writing a line of code.
- **1.5 Web search & honest answers:** when Claude searches vs. answers from training, how to demand sources, how to fact-check. Exercise: research something current and verify two claims independently.
- **1.6 Projects:** organizing work into projects, project knowledge, custom instructions. Meta-moment: reveal that this course is itself a packaged set of instructions — dissect how it works as the live example.
- **1.7 Memory, past chats & long-game habits:** how continuity works, when to start fresh vs. continue, naming chats, what Claude remembers. Exercise: design their personal "Claude workspace" — projects they'll actually keep.
- **1.8 Level 1 boss fight:** a single multi-step real task combining files + iteration + an artifact, done start to finish with minimal coaching. Pass = Level 2 unlocked.

## LEVEL 2 — Claude Code: from zero to building

- **2.1 Terminal survival kit** *(only if needed)*: cd, ls, what a folder path is, how to not be scared. 10 minutes, hands-on.
- **2.2 Install & first contact:** install Claude Code (verify current steps in official docs first!), open it in a folder, ask questions about files, make a first tiny change and see it happen. Exercise: have Claude Code introduce the machine to them — "what's in this folder, explain it like I'm new".
- **2.3 The build loop:** describe what you want → review Claude's plan → let it work → test → give feedback → repeat. The skill is *describing and reviewing*, not typing code. Exercise: build a single-page personal website from scratch, locally.
- **2.4 Plan mode & staying in control:** making Claude Code propose before it acts, reviewing diffs, saying no, asking "why did you do it that way". Exercise: request a change, reject the first plan, shape a better one.
- **2.5 Git as a seatbelt — and recovering a runaway session:** just enough git to be fearless — commits as save points, undoing mistakes — plus what to do when the agent itself goes sideways (loops, edits the wrong thing, fills its context with junk, or "finishes" something half-done): stop it, reset the conversation, restore from git, re-scope. Knowing you can always undo is what makes you fearless. Exercise: break the project on purpose AND let a session get messy, then recover both cleanly.
- **2.6 CLAUDE.md & standing instructions:** teaching Claude Code your preferences and project rules once, so every session starts smart. Exercise: write a CLAUDE.md for the capstone project together.
- **2.7 Debugging together:** pasting errors, describing "it looks wrong", letting Claude investigate; the art of good bug reports. Exercise: plant a bug brief secretly; they drive the fix.
- **2.8 Capstone sprint I:** dedicate 1–3 sessions to building the real capstone project with everything from Level 2. Act as project lead: scope it small, ship something working.
- **2.9 Level 2 boss fight:** take a small feature from idea → plan → built → committed, solo, with you only observing and reviewing at the end.

## LEVEL 3 — Power user: Cowork, connectors & workflows

- **3.1 Claude Cowork:** Claude working on their actual computer for non-coding work — organizing files, processing documents, batch tasks. Exercise: pick one genuinely messy folder or recurring chore and have Cowork handle it.
- **3.2 Connectors & MCP (user side):** plugging Claude into other tools and services they use; what MCP is in plain words (a universal adapter that lets Claude use other apps). Exercise: connect one service they actually use and do something useful with it.
- **3.3 Data & analysis:** giving Claude spreadsheets/CSVs, getting charts, summaries, and answers; sanity-checking the numbers. Exercise: analyze real data from their life or studies (expenses, grades, stats from a hobby).
- **3.4 Deep research workflows:** structuring big research questions, using research features, synthesizing many sources into something usable. Exercise: produce a genuinely useful research brief on something they're deciding about.
- **3.5 Repeatable workflows:** turning things they do often into reusable prompts, project instructions, and checklists — a personal prompt library. Exercise: build and test 3 reusable templates for their real recurring tasks.
- **3.6 Capstone sprint II:** finish and polish the capstone. Ship it — deploy the site, run the automation for real, hand the document to a real person.
- **3.7 Level 3 boss fight:** design and execute a multi-tool workflow (e.g., research in claude.ai → build in Claude Code → organize output with Cowork) for a fresh task, solo.

## LEVEL 4 — Advanced & frontier *(only when ready — gate behind comfort, not calendar)*

- **4.1 Custom slash commands & automation in Claude Code:** packaging repeated instructions into their own commands. Exercise: create a command they'll use weekly.
- **4.2 Skills:** what skills are, finding/using them, then writing a simple custom skill for something they do often. Exercise: build one tiny skill for the capstone domain.
- **4.3 MCP, builder side:** how MCP servers work conceptually; configure/run an existing one for a tool they use; (if coding-inclined) sketch a minimal custom one with Claude Code's help. (For the full build, `/claude-docent:builder`.)
- **4.4 Subagents & parallel work:** delegating parts of a task to subagents, when parallelism helps vs. hurts. Exercise: a task split across subagents, compared with a single-agent run.
- **4.5 Hooks & guardrails:** making Claude Code automatically run checks (tests, formatters) at the right moments. Exercise: add one hook that catches a mistake before it lands.
- **4.6 Claude in CI / GitHub:** Claude reviewing or acting on a repository automatically (GitHub Actions integration). Exercise: set up one automated review or task on the capstone repo.
- **4.7 The API & building AI features:** calling Claude from code; build a tiny app *powered by* Claude rather than built with it. Exercise: a 30-line script or mini-app that uses the API for something fun. (Then `/claude-docent:builder` for the real track.)
- **4.8 Multi-session & big-project technique:** managing long-running projects — context strategy, when to start fresh sessions, keeping notes files, git worktrees for parallel attempts (advanced).
- **4.9 Judgment & taste — the real final boss:** when NOT to use AI, reviewing AI output critically, spotting hallucinations, security/privacy basics (what never to paste into any AI), and explaining to someone else how all this works. Final exercise: they teach you — explain three concepts back in their own words; grade the explanations.
- **4.10 Claude everywhere — surfaces, scheduling & automation:** the same Claude Code engine runs in the terminal, IDE, desktop app, the web, and phone — and can keep working while they're away. Routines/scheduled tasks for recurring work, background agents for parallel jobs, remote control + mobile continuation, automatic code review on pull requests, and chat-to-PR from Slack. (Verify the current surfaces and how to enable them in the docs first.) Exercise: pick one recurring chore and set it up to run without babysitting.
- **4.11 Staying current after this course:** Claude's products change fast, so the real graduation skill is keeping up — re-verifying against the docs, skimming release notes, re-baselining after time away. Standing habit: when something learned here stops matching what they see, trust the product, check the docs, update the notes. Exercise: find one thing that's changed since they started, confirm it in the docs, and update their workspace.
- **4.12 Graduation project:** propose, plan, and complete one ambitious project using at least four techniques from Levels 2–4, presented with a short write-up of what was built and how. Write an honest "diploma" — strengths, growth areas, and what to learn next beyond this course — and distill everything into a one-page **keepable cheat-sheet** (go-to prompts, workspace map, verify-before-trust habits) they pin up and actually use.

## WOVEN THROUGHOUT (no dedicated lessons — sprinkle into every session)

- Verification habit: trust but check, especially numbers, links, and claims.
- Decomposition: big task → small steps.
- Knowing the limits: what Claude is bad at and how to compensate.
- New chat vs. continue: context hygiene.
- Security sense: secrets, passwords, personal data — what stays out of prompts.
