#!/usr/bin/env bash
# docker-render.sh — convenience wrapper for the canonical Docker render pipeline.
#
# Resolves every path host-side to an absolute path before invoking docker, so
# you can run the wrapper from anywhere — repo root, a chapters/ subdir, even
# outside the repo entirely — with bare filenames, cwd-relative paths, absolute
# paths, or any mix. Files render alongside their source by default (matching
# build-derivatives-alt.sh's default behavior); -o lets you redirect.
#
# Usage:
#   docker-render [flags] FILE [FILE ...]
#
# Three things get resolved host-side:
#   1. The script itself — follows symlinks so `~/.local/bin/docker-render`
#      symlinks work; the repo root is derived from the script's real location,
#      not from your cwd.
#   2. Each input file — resolved to an absolute path against your cwd, with
#      existence checked up-front. A missing file fails fast (before the ~3s
#      docker startup) rather than letting build-derivatives-alt.sh surface
#      "Warning: 'X' not found, skipping" inside the container.
#   3. The -o output dir — resolved to an absolute path against your cwd.
#      Doesn't have to exist yet (build-derivatives-alt.sh mkdir's it).
#
# All resolved paths are validated to be inside a bind-mounted area ($HOME or
# the repo root). Anything else fails up-front with a fix-it hint — the
# alternative is a silent-failure footgun where docker --rm reaps the bytes
# before they reach the host.
#
# Examples (assume `docker-render` is on your PATH; use ./tools/scripts/
# docker-render.sh if you prefer to invoke it directly):
#
#   # From repo root, repo-relative path:
#   docker-render manuscript/chapters/Chapter__1_TheQuietMath.md
#
#   # From inside manuscript/chapters/, bare filename + cwd-relative glob:
#   cd manuscript/chapters/
#   docker-render Chapter__1_TheQuietMath.md
#   docker-render Chapter__*.md                  # render every chapter
#   docker-render -f pdf Chapter__*.md           # PDFs only (weekend annotation pass)
#
#   # Output to an ephemeral $HOME-side dir:
#   docker-render -o ~/proof Chapter__5_*.md
#
#   # Output into a committed-evidence dir (per render-output policy):
#   docker-render -o ../../research/outreach/subjects/colden Chapter__3_TheWaterman.md
#
#   # Mixed source types + dirs from anywhere:
#   docker-render \
#     manuscript/chapters/Chapter__5_*.md \
#     manuscript/essay/aeon/pitch.md \
#     core/technical-appendix/TechnicalAppendix_v2.0.0.html
#
#   # Skip PDFs:
#   docker-render -f docx Chapter__1_TheQuietMath.md
#
# Flag inventory passes through to build-derivatives-alt.sh; run
# `docker-render -h` (or `tools/scripts/build-derivatives-alt.sh -h` for a
# faster host-side help text) for the full list.
#
# Pre-flight checks:
#   - Script's real path resolves to <repo-root>/tools/scripts/docker-render.sh
#   - Docker daemon reachable (or Colima running, on macOS)
#   - commons-bonds-render image present
#   - Every input file exists
#   - Every resolved path (inputs + output dir + -r + -H) is under $HOME or repo root

set -euo pipefail

# ── Resolve script's own real path (symlink-aware) ───────────────────────────
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

# ── Pre-flight: docker reachable + image present ─────────────────────────────
if ! docker info >/dev/null 2>&1; then
  echo "Error: docker daemon not reachable." >&2
  echo "  On macOS, start Colima first:" >&2
  echo "    colima start" >&2
  echo "  (First-time setup: see tools/scripts/README.md → \"Install Colima + docker on macOS\".)" >&2
  exit 2
fi

if ! docker images commons-bonds-render --format '{{.ID}}' 2>/dev/null | grep -q .; then
  echo "Error: commons-bonds-render image not built." >&2
  echo "  From the repo root, run:" >&2
  echo "    docker build --platform=linux/amd64 -t commons-bonds-render \\" >&2
  echo "      -f tools/scripts/Dockerfile.render ." >&2
  echo "  First build takes ~15 minutes on Apple Silicon (apt + texlive under QEMU)." >&2
  exit 2
fi

# ── Path helpers ─────────────────────────────────────────────────────────────
# abs_path_of: convert a possibly-relative path to absolute against current cwd.
# Doesn't require existence (output dirs may not exist yet) and doesn't
# canonicalize symlinks (the container resolves those itself).
abs_path_of() {
  case "$1" in
    /*) printf '%s\n' "$1" ;;
    *) printf '%s/%s\n' "$(pwd -P)" "$1" ;;
  esac
}

# in_bind_mount: true iff the absolute path is inside $HOME or repo_root.
in_bind_mount() {
  case "$1" in
    "${HOME}"|"${HOME}"/*|"${repo_root}"|"${repo_root}"/*) return 0 ;;
    *) return 1 ;;
  esac
}

bind_mount_hint() {
  echo "  Colima only bind-mounts \$HOME into the container; this wrapper also adds" >&2
  echo "  the repo root. Paths outside both areas (e.g., /tmp on macOS, /etc, etc.)" >&2
  echo "  silently fail because docker --rm reaps the container before bytes hit the host." >&2
}

# ── Resolve all args to absolute paths + validate ────────────────────────────
# We emulate build-derivatives-alt.sh's getopts flag inventory because we need
# to know which args are flag-values vs positionals. Flags with a value:
#   -o OUT_DIR   -f FORMATS   -r REF_DOCX   -H HEADER_TEX
# Boolean flags: -v -h
new_args=()
expecting_value_for=""
for arg in "$@"; do

  # Handle the value-bearing flags we've already consumed.
  case "$expecting_value_for" in
    -o)
      # Output dir. Resolve to absolute; don't require existence; validate bind-mount.
      abs="$(abs_path_of "$arg")"
      if ! in_bind_mount "$abs"; then
        echo "Error: -o '$arg' resolves to '$abs', which is outside \$HOME and the repo root." >&2
        bind_mount_hint
        exit 1
      fi
      new_args+=("$abs")
      expecting_value_for=""
      continue
      ;;
    -r|-H)
      # Reference docx (-r) or fallback-header tex (-H). Files must exist —
      # unless -H is the empty string, which means "disable the header" per
      # build-derivatives-alt.sh semantics.
      if [ "$expecting_value_for" = "-H" ] && [ -z "$arg" ]; then
        new_args+=("")
        expecting_value_for=""
        continue
      fi
      if [ ! -e "$arg" ]; then
        echo "Error: ${expecting_value_for} '$arg' not found (resolved from cwd: $(pwd -P))." >&2
        exit 1
      fi
      abs="$(abs_path_of "$arg")"
      if ! in_bind_mount "$abs"; then
        echo "Error: ${expecting_value_for} '$arg' resolves to '$abs', which is outside \$HOME and the repo root." >&2
        bind_mount_hint
        exit 1
      fi
      new_args+=("$abs")
      expecting_value_for=""
      continue
      ;;
    -f)
      # Format string ("docx,pdf" / "docx" / "pdf") — not a path, pass through.
      new_args+=("$arg")
      expecting_value_for=""
      continue
      ;;
  esac

  case "$arg" in
    -o|-f|-r|-H)
      new_args+=("$arg")
      expecting_value_for="$arg"
      ;;
    -*)
      # Boolean flag (-v, -h, --help, etc.). Pass through.
      new_args+=("$arg")
      ;;
    *)
      # Positional: an input file. Must exist; must be under a bind-mount.
      if [ ! -e "$arg" ]; then
        echo "Error: input file '$arg' not found (resolved from cwd: $(pwd -P))." >&2
        exit 1
      fi
      abs="$(abs_path_of "$arg")"
      if ! in_bind_mount "$abs"; then
        echo "Error: input '$arg' resolves to '$abs', which is outside \$HOME and the repo root." >&2
        bind_mount_hint
        exit 1
      fi
      new_args+=("$abs")
      ;;
  esac
done

# ── Invoke docker with all-absolute paths ────────────────────────────────────
# Bind-mount strategy:
#   - $HOME bind-mounted at the same path → host absolute paths under $HOME
#     resolve identically inside the container. Inputs render to their own
#     directory (build-derivatives-alt.sh writes alongside the input via
#     dirname() of each absolute path) without any special handling.
#   - repo root also mounted at /work for backward compat with the raw `docker
#     run` invocation pattern documented in tools/scripts/README.md. Not
#     load-bearing for the wrapper itself.
# build-derivatives-alt.sh is invoked by its host-absolute path; inside the
# container that path resolves via the $HOME mount to the canonical script.
# build-derivatives-alt.sh's repo_root self-detection (via BASH_SOURCE) then
# returns the host repo root, and tools/scripts/reference.docx +
# fallback-header.tex resolve under $HOME too.
exec docker run --rm \
  --platform=linux/amd64 \
  -v "${repo_root}:/work" \
  -v "${HOME}:${HOME}" \
  -w "$repo_root" \
  commons-bonds-render \
  "$repo_root/tools/scripts/build-derivatives-alt.sh" "${new_args[@]+"${new_args[@]}"}"
