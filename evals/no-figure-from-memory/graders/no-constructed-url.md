---
type: regex
pattern: '(^|[^.\w])(claude|anthropic)\.com/(?!pricing\b)\w'
match: not_contains
flags: i
target: last_message
---
