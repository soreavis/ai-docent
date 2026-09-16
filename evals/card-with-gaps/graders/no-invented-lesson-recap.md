---
type: regex
pattern: '(previously|last time|you (finished|completed|covered)).{0,80}(lesson|level)\s*\d'
match: not_contains
flags: is
target: last_message
---
