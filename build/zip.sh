#!/usr/bin/env bash
# Build one zip per skill for upload to claude.ai (Customize → Skills).
# The zip root must be the skill folder itself, and the folder name must match
# the SKILL.md `name` field, or the upload is rejected.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills="$root/skills"
dist="$root/dist"
rm -rf "$dist"
mkdir -p "$dist"
spec_keys="name description license compatibility metadata allowed-tools"

for skill in "$skills"/*/; do
  name="$(basename "$skill")"
  staging="$(mktemp -d)"
  cp -R "$skill" "$staging/$name"

  # The claude.ai and ChatGPT uploaders reject any frontmatter key the open spec
  # does not allow, so keep only the spec's keys rather than deleting known
  # extensions by name: the next Claude Code-only key would slip through.
  awk -v keep="$spec_keys" '
    BEGIN { n = split(keep, k, " "); for (i = 1; i <= n; i++) ok[k[i]] = 1 }
    NR == 1 && /^---$/ { fm = 1; print; next }
    fm && /^---$/ { fm = 0; print; next }
    fm && /^[^ \t#-]/ { key = $0; sub(/:.*/, "", key); show = (key in ok) }
    !fm || show { print }
  ' "$staging/$name/SKILL.md" > "$staging/SKILL.md.tmp"
  mv "$staging/SKILL.md.tmp" "$staging/$name/SKILL.md"

  (cd "$staging" && zip -qr "$dist/$name.zip" "$name")
  rm -rf "$staging"

  # Check what actually shipped, not what the filter meant to do.
  for key in $(unzip -p "$dist/$name.zip" "$name/SKILL.md" | sed -n '2,/^---$/p' | grep -E '^[A-Za-z]' | cut -d: -f1); do
    case " $spec_keys " in
      *" $key "*) ;;
      *) echo "dist/$name.zip: frontmatter key '$key' is outside the Agent Skills spec" >&2; exit 1 ;;
    esac
  done
  echo "dist/$name.zip"
done
