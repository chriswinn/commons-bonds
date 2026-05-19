#!/usr/bin/env bash
# session-start-render-toolchain.sh — SessionStart hook wrapper.
#
# Invoked by .claude/settings.json on every Claude Code session start. Two
# gates determine whether the canonical installer fires:
#
#   1. CLAUDE_CODE_REMOTE=true. Only run inside Anthropic remote-container
#      sessions; skip on local laptop sessions (laptop renders via Docker
#      through Colima, not via host apt — see tools/scripts/README.md).
#
#   2. Toolchain not already present. If install-render-toolchain.sh --check
#      passes, the toolchain is already installed (either by a prior session's
#      hook run cached into the env, or by an Anthropic-web-UI setup script).
#      Skip the apt install in that case — the SessionStart hook fires on
#      EVERY session including resume, and a no-op fast-path keeps startup
#      latency low.
#
# Per Claude Code on web docs: setup scripts (UI-configured) benefit from
# environment caching across sessions; SessionStart hooks do not. The
# recommended primary mechanism is to configure the canonical installer as
# the environment's web-UI setup script (then this hook is a no-op).
# This hook exists as a belt-and-suspenders for repos cloned into freshly-
# spun-up environments that haven't yet had their setup script configured.
#
# Exit codes per docs:
#   - 0: success (either skipped or installed cleanly).
#   - non-zero: install failure surfaced to user; session continues
#     (SessionStart hooks do not block session start on non-zero exit).
#
# Reference: tools/scripts/install-render-toolchain.sh + tools/scripts/README.md.

set -euo pipefail

# Gate 1: only fire in Anthropic remote-container sessions.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Resolve installer path. $CLAUDE_PROJECT_DIR is set by Claude Code; fall
# back to a path inferred from this script's location for direct
# invocation cases.
project_dir="${CLAUDE_PROJECT_DIR:-}"
if [ -z "$project_dir" ]; then
  script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  project_dir="$(cd "${script_dir}/../.." && pwd)"
fi

installer="${project_dir}/tools/scripts/install-render-toolchain.sh"

if [ ! -x "$installer" ]; then
  echo "session-start-render-toolchain: installer not found at $installer; skipping." >&2
  exit 0
fi

# Gate 2: skip if toolchain already present + healthy.
if "$installer" --check >/dev/null 2>&1; then
  exit 0
fi

# Install. apt-runner inside install-render-toolchain.sh handles sudo.
echo "session-start-render-toolchain: canonical toolchain absent; installing via apt..."
"$installer"
