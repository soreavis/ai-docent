# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 0.1.x   | Yes       |

## Reporting a Vulnerability

**Do not open a public issue for security vulnerabilities.**

Please report security issues privately via [GitHub Security Advisories](https://github.com/soreavis/claude-docent/security/advisories/new).

Include:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

You will receive a response within 72 hours. Please allow time to assess and patch before any public disclosure.

## Scope

This repository contains Markdown instruction files, two manifests, and two build scripts. It ships no runtime code and requests no credentials.

The findings most relevant here are:

- **Prompt-injection surface.** A skill body is instructions an agent follows. A change that makes a course fetch untrusted content and act on it, exfiltrate conversation data, or bypass a user's tool permissions is a security issue — report it.
- **The `security` course shows attack examples.** They are inert, fenced, and labeled by design, and the describe-don't-perform protocol forbids executing them. If any example could plausibly be *executed* rather than *read*, that is a bug worth reporting.
- **Progress files.** Courses write `~/.claude-docent/progress-<course>.md`. They are meant to hold learning progress only. A course that writes secrets, tokens, or file contents there is a defect.
