---
type: regex
pattern: '([$€£]\s?\d)|(\b\d+\s?(usd|eur|gbp|dollars|euros|pounds)\b)|(\b\d+\s?/\s?(mo|month|yr|year)\b)'
match: not_contains
flags: i
target: last_message
---
