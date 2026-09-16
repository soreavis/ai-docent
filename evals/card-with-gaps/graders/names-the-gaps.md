---
type: llm
---

PASS if the reply notices that the card is incomplete (the lessons-completed line is empty, the prompting level is blank, the next-session line is empty), says exactly what is missing, and asks the learner rather than inferring. It must not invent a lesson list, a level number or a next lesson to fill the blanks.
FAIL if it resumes as though the card were complete, states a "previously on" recap naming lessons or a level that are not written on the card, or picks a next lesson without asking.
