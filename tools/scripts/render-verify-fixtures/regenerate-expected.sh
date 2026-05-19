#!/usr/bin/env bash
# regenerate-expected.sh — re-generate the CI render-verify fixture's
# checked-in expected outputs.
#
# Run when the canonical toolchain advances (apt update lands a new pandoc /
# xelatex / wkhtmltopdf / font version) and the CI render-verify workflow
# starts failing on text-diff drift. Procedure:
#
#   1. Rebuild the Docker image (no cache):
#      docker build --platform=linux/amd64 --no-cache \
#        -t commons-bonds-render -f tools/scripts/Dockerfile.render .
#
#   2. Update tools/quality-gates/render-baselines/build-environment.yaml
#      with the new toolchain stamp:
#      docker run --rm commons-bonds-render /tmp/install-render-toolchain.sh --capture-stamp
#
#   3. Run this script to regenerate the expected outputs:
#      tools/scripts/render-verify-fixtures/regenerate-expected.sh
#
#   4. Inspect the diff in git status — verify the changes are
#      intentional (toolchain-driven) and not real regressions.
#
#   5. Commit the updated build-environment.yaml + the expected/ outputs
#      together. CI will re-pass against the new baseline.

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/../../.." && pwd)"
fixtures_dir="${script_dir}"
expected_dir="${fixtures_dir}/expected"

mkdir -p "${expected_dir}"

# Render fixture inside Docker with SOURCE_DATE_EPOCH set for determinism.
# On macOS, Colima only bind-mounts paths under $HOME by default — /var/folders/
# (mktemp's default on macOS) is not visible to the container. Use a $HOME-rooted
# tmp dir so the bind-mount works on both macOS (Colima) and Linux (CI).
tmp_out="$(mktemp -d -p "$HOME" .render-verify-regen.XXXXXX)"
trap 'rm -rf "$tmp_out"' EXIT

echo "[regenerate-expected] Rendering fixture inside Docker..."
docker run --rm \
  --platform=linux/amd64 \
  -v "${repo_root}:/work" \
  -w /work \
  -e SOURCE_DATE_EPOCH=1700000000 \
  -v "${tmp_out}:/out" \
  commons-bonds-render \
  bash -c 'tools/scripts/build-derivatives-alt.sh -v \
    -o /out \
    tools/scripts/render-verify-fixtures/fixture.md 2> /out/xelatex-stderr.log'

if grep -F -q "Missing character" "${tmp_out}/xelatex-stderr.log" 2>/dev/null; then
  echo "[regenerate-expected] WARNING: xelatex reported Missing-character glyphs:"
  grep -F "Missing character" "${tmp_out}/xelatex-stderr.log" | head -5
  echo "  Check fonts coverage before committing the expected output."
fi

# Extract text representations (the actual diff target — bytes drift on
# pandoc / xelatex point releases, but extracted text is stable).
echo "[regenerate-expected] Extracting text..."
docker run --rm \
  --platform=linux/amd64 \
  -v "${tmp_out}:/work" -w /work \
  commons-bonds-render \
  pdftotext -layout fixture.pdf fixture.pdf.txt

docker run --rm \
  --platform=linux/amd64 \
  -v "${tmp_out}:/work" -w /work \
  commons-bonds-render \
  pandoc -f docx -t plain fixture.docx -o fixture.docx.txt

# Copy text outputs into the checked-in expected/ dir.
cp "${tmp_out}/fixture.pdf.txt" "${expected_dir}/fixture.pdf.txt"
cp "${tmp_out}/fixture.docx.txt" "${expected_dir}/fixture.docx.txt"

echo "[regenerate-expected] Done. Updated:"
ls -la "${expected_dir}/"
echo ""
echo "Inspect diffs via: git diff tools/scripts/render-verify-fixtures/expected/"
