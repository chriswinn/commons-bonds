#!/usr/bin/env bash
# docker-render.sh — convenience wrapper for the canonical Docker render pipeline.
#
# Forwards all positional args + flags to tools/scripts/build-derivatives-alt.sh
# inside the commons-bonds-render image, with --platform=linux/amd64 and the
# repo-root bind-mount already set. The wrapper is a transparent passthrough —
# no flag-by-flag duplication, no added semantics.
#
# Usage:
#   tools/scripts/docker-render.sh [flags] FILE [FILE ...]
#
# Paths must be repo-relative (the docker bind-mount is the repo root). Run
# the wrapper from the repo root so shell glob expansion lands in the right
# spot.
#
# Examples:
#   # Render one chapter; outputs land alongside the source (gitignored by policy).
#   tools/scripts/docker-render.sh manuscript/chapters/Chapter__1_TheQuietMath.md
#
#   # Render to an ephemeral $HOME-side location for proofing.
#   tools/scripts/docker-render.sh -o ~/proof \
#     manuscript/chapters/Chapter__5_*.md
#
#   # Render straight into a committed-evidence dir for a delivery (Colden-style).
#   tools/scripts/docker-render.sh -o research/outreach/subjects/colden \
#     manuscript/chapters/Chapter__3_TheWaterman.md
#
#   # Skip PDFs.
#   tools/scripts/docker-render.sh -f docx core/technical-appendix/*.html
#
# Output-path constraint: -o must be repo-relative OR under $HOME. Colima only
# bind-mounts $HOME into the container by default; absolute paths elsewhere
# (incl. /tmp on macOS) are rejected up-front by the pre-flight rather than
# silently dropping the bytes.
#
# Flag inventory passes through to build-derivatives-alt.sh; run
# `tools/scripts/build-derivatives-alt.sh -h` (host-side; quick help text) or
# `tools/scripts/docker-render.sh -h` (forwards through Docker) for the full list.
#
# Pre-flight checks before exec'ing docker:
#   - Inside a git repo (resolves repo root via git rev-parse --show-toplevel)
#   - Docker daemon reachable (or Colima running, on macOS)
#   - commons-bonds-render:latest image present
#
# Each check fails with a useful next-step hint when it fails — see the error
# branches below.

set -euo pipefail

# Resolve repo root.
if ! repo_root="$(git rev-parse --show-toplevel 2>/dev/null)"; then
  echo "Error: not inside a git repository. Run from somewhere under the commons-bonds repo tree." >&2
  exit 1
fi

# Pre-flight: docker daemon reachable.
if ! docker info >/dev/null 2>&1; then
  echo "Error: docker daemon not reachable." >&2
  echo "  On macOS, start Colima first:" >&2
  echo "    colima start" >&2
  echo "  (First-time setup: see tools/scripts/README.md → \"Install Colima + docker on macOS\".)" >&2
  exit 2
fi

# Pre-flight: canonical render image present.
if ! docker images commons-bonds-render --format '{{.ID}}' 2>/dev/null | grep -q .; then
  echo "Error: commons-bonds-render image not built." >&2
  echo "  From the repo root, run:" >&2
  echo "    docker build --platform=linux/amd64 -t commons-bonds-render \\" >&2
  echo "      -f tools/scripts/Dockerfile.render ." >&2
  echo "  First build takes ~15 minutes on Apple Silicon (apt + texlive under QEMU)." >&2
  exit 2
fi

# Pre-flight: an absolute -o path must land somewhere that's bind-mounted
# into the container, otherwise the wrapper reports success while the bytes
# die with the --rm container before reaching the host. Two paths work:
# repo-relative (resolves under /work) or any path under $HOME (resolves
# under the $HOME bind-mount below). Absolute paths outside both areas
# (e.g., /tmp on macOS, /etc, etc.) are rejected up-front with a fix-it hint.
prev=""
for arg in "$@"; do
  if [ "$prev" = "-o" ]; then
    case "$arg" in
      /*)
        # Absolute path. Must be under $HOME or under repo root.
        case "$arg" in
          "${HOME}"/*|"${HOME}"|"${repo_root}"/*|"${repo_root}") : ;;
          *)
            echo "Error: -o path '$arg' is absolute but outside \$HOME and the repo root." >&2
            echo "  Colima only bind-mounts \$HOME into the container by default; this wrapper" >&2
            echo "  adds the repo root. Other absolute paths (incl. /tmp on macOS) silently fail." >&2
            echo "  Use a repo-relative path (e.g., -o output/proof) or a \$HOME path (e.g., -o ~/proof)." >&2
            exit 1
            ;;
        esac
        ;;
    esac
  fi
  prev="$arg"
done

# Render. Bind-mount strategy:
#   - /work        ← repo root (cwd for build-derivatives-alt.sh; repo-relative
#                    input + output paths resolve here)
#   - $HOME        ← so absolute -o paths under $HOME work (a common pattern for
#                    ephemeral proofing dirs like ~/proof)
# Other absolute paths are rejected by the pre-flight above — the silent-failure
# footgun (writes land in the container's ephemeral FS, get reaped by --rm) is
# not worth the convenience.
exec docker run --rm \
  --platform=linux/amd64 \
  -v "${repo_root}:/work" \
  -v "${HOME}:${HOME}" \
  -w /work \
  commons-bonds-render \
  tools/scripts/build-derivatives-alt.sh "$@"
