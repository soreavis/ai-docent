# Changelog

All notable changes to this project are documented here.

This project follows [Keep a Changelog](https://keepachangelog.com/) and [Semantic Versioning](https://semver.org/).

Bumping the `version` in `plugins/claude-docent/.claude-plugin/plugin.json` is what delivers an update to installed users — see [CONTRIBUTING.md](CONTRIBUTING.md#releasing).

## [Unreleased]

## [0.1.0] - 2026-07-24

### Added

- Six multi-session tutor courses as Agent Skills: `foundations`, `prompt-craft`, `reliability`, `security`, `mechanics`, `builder`.
- Claude Code plugin and marketplace manifests, so the set installs with `/plugin install claude-docent@claude-docent`.
- File-based Progress Cards written to `~/.claude-docent/progress-<course>.md`, with the pasted-card fallback for surfaces without a filesystem.
- `build/zip.sh` to package each skill for upload to claude.ai.
- `build/validate.py` enforcing the Agent Skills spec plus this repo's conventions, wired into CI.
