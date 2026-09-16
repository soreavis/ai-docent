---
type: regex
pattern: '\b\d+(\.\d+)?\s?(mb|gb|kb|files|attachments|documents)\b|\bmillion\b'
match: not_contains
flags: i
target: last_message
---
