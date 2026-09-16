---
type: regex
pattern: '\b\d+\s?(messages|msgs|prompts)\b'
match: not_contains
flags: i
target: last_message
---
