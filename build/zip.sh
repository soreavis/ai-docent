#!/usr/bin/env bash
# Build one zip per skill for upload to claude.ai (Customize → Skills).
# The zip root must be the skill folder itself, and the folder name must match
# the SKILL.md `name` field, or the upload is rejected.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills="$root/plugins/claude-docent/skills"
dist="$root/dist"
rm -rf "$dist"
mkdir -p "$dist"

for skill in "$skills"/*/; do
  name="$(basename "$skill")"
  staging="$(mktemp -d)"
  cp -R "$skill" "$staging/$name"

  # disable-model-invocation is a Claude Code extension, not part of the open
  # spec. Drop it so the claude.ai uploader never sees an unknown field.
  # Written portably: BSD and GNU sed disagree on in-place editing.
  sed '/^disable-model-invocation:/d' "$staging/$name/SKILL.md" > "$staging/SKILL.md.tmp"
  mv "$staging/SKILL.md.tmp" "$staging/$name/SKILL.md"

  (cd "$staging" && zip -qr "$dist/$name.zip" "$name")
  rm -rf "$staging"
  echo "dist/$name.zip"
done
