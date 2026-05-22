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
# The wrapper honors your current working directory — bare filenames + cwd-
# relative globs work the same as they would for any local tool. Symlinking
# this script into your PATH (e.g., ~/.local/bin/docker-render → tools/scripts/
# docker-render.sh) is supported; the script resolves the repo root from
# its own real location, not from your cwd.
#
# Examples (all assume the wrapper is on your PATH or invoked as ./docker-render.sh):
#
#   # From repo root, repo-relative path:
#   docker-render manuscript/chapters/Chapter__1_TheQuietMath.md
#
#   # From inside manuscript/chapters/, bare filename + glob:
#   cd manuscript/chapters/
#   docker-render Chapter__1_TheQuietMath.md
#   docker-render Chapter__*.md         # render every chapter at once
#
#   # Output to an ephemeral $HOME-side dir for proofing:
#   docker-render -o ~/proof manuscript/chapters/Chapter__5_*.md
#
#   # Output into a committed-evidence dir (per render-output policy):
#   docker-render -o research/outreach/subjects/colden \
#     manuscript/chapters/Chapter__3_TheWaterman.md
#
#   # Skip PDFs:
#   docker-render -f docx core/technical-appendix/*.html
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

# Resolve repo root from the script's own real location — robust to symlinks
# (e.g., when this script is symlinked from ~/.local/bin/docker-render) and
# independent of the user's cwd. Earlier versions used `git rev-parse
# --show-toplevel` which broke under both of those — from outside a git
# checkout it errored "not a git repository," and from inside a different
# repo it picked the wrong repo's root.
script="${BASH_SOURCE[0]}"
while [ -L "$script" ]; do
  link_target="$(readlink "$script")"
  case "$link_target" in
    /*) script="$link_target" ;;
    *) script="$(cd "$(dirname "$script")" && pwd -P)/$link_target" ;;
  esac
done
script_dir="$(cd "$(dirname "$script")" && pwd -P)"
# Canonical layout: tools/scripts/docker-render.sh — repo root is two levels up.
repo_root="$(cd "$script_dir/../.." && pwd -P)"

if [ ! -f "$repo_root/tools/scripts/build-derivatives-alt.sh" ]; then
  echo "Error: cannot find tools/scripts/build-derivatives-alt.sh under '$repo_root'." >&2
  echo "  This script must live at <repo-root>/tools/scripts/docker-render.sh (symlinks are fine)." >&2
  echo "  If you symlinked docker-render.sh, double-check the symlink target points into the" >&2
  echo "  commons-bonds repo's tools/scripts/ dir." >&2
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

# Translate the user's host cwd to the corresponding path inside the
# container. This is what makes `docker-render Chapter__1.md` work when
# invoked from manuscript/chapters/, not just from the repo root. Without
# this, the container's working directory is always /work (= repo root)
# and a bare filename resolves as /work/Chapter__1.md — which doesn't
# exist; the file is at /work/manuscript/chapters/Chapter__1.md.
host_cwd="$(pwd -P)"
case "$host_cwd" in
  "${repo_root}")
    container_cwd="/work"
    ;;
  "${repo_root}"/*)
    container_cwd="/work/${host_cwd#${repo_root}/}"
    ;;
  "${HOME}"|"${HOME}"/*)
    # Outside the repo but under $HOME — resolves via the $HOME bind-mount below.
    container_cwd="$host_cwd"
    ;;
  *)
    # Outside repo + outside $HOME. Fallback to /work; if the user passed
    # cwd-relative paths from here, build-derivatives-alt.sh will surface
    # a "file not found" inside the container.
    container_cwd="/work"
    ;;
esac

# Render. Bind-mount strategy:
#   - /work        ← repo root (-w lands here when cwd is the repo root;
#                    sub-cwd's translate to /work/<rest>)
#   - $HOME        ← so absolute -o paths under $HOME work AND so invoking
#                    the wrapper from anywhere under $HOME works too.
# Reference build-derivatives-alt.sh by absolute path inside the container
# so the working directory can be any subdir of /work, not just /work itself.
# Other absolute paths are rejected by the pre-flight above — the silent-
# failure footgun (writes land in the container's ephemeral FS, get reaped
# by --rm) is not worth the convenience.
exec docker run --rm \
  --platform=linux/amd64 \
  -v "${repo_root}:/work" \
  -v "${HOME}:${HOME}" \
  -w "$container_cwd" \
  commons-bonds-render \
  /work/tools/scripts/build-derivatives-alt.sh "$@"
