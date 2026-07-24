# Changelog

All notable changes to this project are documented here.

This project follows [Keep a Changelog](https://keepachangelog.com/) and [Semantic Versioning](https://semver.org/). Releases are managed by Release Please from Conventional Commits — see [CONTRIBUTING.md](CONTRIBUTING.md#releasing).

## [Unreleased]

## [0.1.0]

### Added

- Six multi-session tutor courses as Agent Skills: `foundations`, `prompt-craft`, `reliability`, `security`, `mechanics`, `builder`.
- Install lanes for Claude Code, Codex, Cursor, Gemini CLI, Copilot/GitHub CLI, Grok, and the generic `.agents/` convention, plus per-course zips for claude.ai and Cowork.
- File-based Progress Cards at `~/.ai-docent/progress-<course>.md`, with a pasted-card fallback where there is no filesystem.
- `version.txt` as the single source of truth, kept in lockstep across every manifest by Release Please and enforced by CI.
