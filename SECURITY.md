# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 0.1.x   | Yes       |

## Reporting a Vulnerability

**Do not open a public issue for security vulnerabilities.**

Please report security issues privately via [GitHub Security Advisories](https://github.com/soreavis/ai-docent/security/advisories/new), or by email to REDACTED if that form is unavailable to you.

Include:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

You will receive a response within 72 hours. Please allow time to assess and patch before any public disclosure.

## Scope

This repository contains Markdown instruction files, eight platform manifests, and two build scripts. It ships no runtime code and requests no credentials.

The findings most relevant here are:

- **Prompt-injection surface.** A skill body is instructions an agent follows. A change that makes a course fetch untrusted content and act on it, exfiltrate conversation data, or bypass a user's tool permissions is a security issue — report it.
- **The `security` course shows attack examples.** They are inert, fenced, and labeled by design, and the describe-don't-perform protocol forbids executing them. If any example could plausibly be *executed* rather than *read*, that is a bug worth reporting.
- **Progress files.** Courses write `~/.ai-docent/progress-<course>.md`. They are meant to hold learning progress only. A course that writes secrets, tokens, or file contents there is a defect.
- **Anti-hallucination guardrails.** Every course carries four rules inside its GROUND RULES block — a tool guard, an uncertainty rule, a never-construct-a-URL rule, and enumerated documentation domains. `build/validate.py` fails the build if any is removed. A change that weakens or relocates one of these out of that block is a security-relevant regression, because the guardrails are what stop a course from teaching confident fiction.
- **Courses that act on real work.** `shipping` reads diffs and `long-haul` touches long-running projects; both are explicitly forbidden from committing, pushing, rebasing, or otherwise mutating a learner's repository without being asked in that session. A change that relaxes those limits is in scope.
