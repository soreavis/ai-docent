---
type: regex
pattern: '["'']claude-[a-z0-9.-]*\d["'']'
match: not_contains
flags: i
target: last_message
---
