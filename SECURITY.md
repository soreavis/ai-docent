# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 0.2.2 <!-- x-release-please-version --> (latest) | Yes |
| Older   | No — update through your install lane |

## Reporting a Vulnerability

**Do not open a public issue for security vulnerabilities.**

Please report security issues privately via [GitHub Security Advisories](https://github.com/soreavis/ai-docent/security/advisories/new). Private vulnerability reporting is enabled on this repository, so that form is available to anyone who can read this file.

Include:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

You will receive a response within 72 hours. Please allow time to assess and patch before any public disclosure.

## Scope

This repository contains Markdown instruction files, eight platform manifests, and the three build scripts under `build/`. It ships no runtime code and requests no credentials.

The findings most relevant here are:

- **Prompt-injection surface.** A skill body is instructions an agent follows. A change that makes a course fetch untrusted content and act on it, exfiltrate conversation data, or bypass a user's tool permissions is a security issue — report it.
- **The `security` course shows attack examples.** They are inert, fenced, and labeled by design, and the describe-don't-perform protocol forbids executing them. If any example could plausibly be *executed* rather than *read*, that is a bug worth reporting.
- **Progress files.** Courses write `~/.ai-docent/progress-<course>.md`. They are meant to hold learning progress only. A course that writes secrets, tokens, or file contents there is a defect.
- **Anti-hallucination guardrails.** Every skill carries seven rules inside its GROUND RULES block — a tool guard, an uncertainty rule, a never-construct-a-URL rule, enumerated documentation domains, a never-state-an-unlooked-up-figure rule, a rule against acting on the learner's system unasked, and a rule that the learner's chosen tone can never change what is asserted or how certain it is. `build/validate.py` fails the build if any is removed. A change that weakens or relocates one of these out of that block is a security-relevant regression, because the guardrails are what stop a course from teaching confident fiction.
- **Tone selection.** Learners pick a coaching voice, and a persona is a classic vector for talking a model past its own limits. `references/tone.md` states the floor — tone is delivery, never content — and the GROUND RULES make the guardrail win any conflict. A change that lets a voice suppress a hedge, skip a verification, or manufacture an anecdote is in scope.
- **Courses that act on real work.** `shipping` reads diffs and `long-haul` touches long-running projects; both are explicitly forbidden from committing, pushing, rebasing, or otherwise mutating a learner's repository without being asked in that session. A change that relaxes those limits is in scope.
