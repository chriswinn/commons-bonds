#!/usr/bin/env bash
# Double-spaced read-through PDF with a wide right margin for marginalia.
# Usage: build.sh <input.md> <output.pdf> "<header label>" "<cover title>" "<cover subtitle>"
# Needs pandoc and the container's pre-installed Playwright/Chromium.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
in="$1"; out="$2"; label="$3"; title="$4"; sub="${5:-}"
tmp="$(mktemp -d)"
# Drop a leading HTML comment block (front-matter notes) if the file starts with one.
if head -c 4 "$in" | grep -q '<!--'; then
  awk 'BEGIN{c=1} c&&/-->/{c=0;next} !c' "$in" > "$tmp/body.md"
else
  cp "$in" "$tmp/body.md"
fi
pandoc -f gfm -t html5 "$tmp/body.md" -o "$tmp/body.html"
{
  printf '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>' "$(cat "$here/print.css")"
  printf '<div class="cover"><b>%s</b><span class="s">%s</span></div>' "$title" "$sub"
  cat "$tmp/body.html"
  printf '</body></html>'
} > "$tmp/full.html"
node "$here/render.cjs" "$tmp/full.html" "$(realpath -m "$out")" "$label"
rm -rf "$tmp"
