#!/usr/bin/env bash
# Tag-then-delete the 28 stale branches reviewed in
# tools/workstream-handoffs/stale-branch-review_2026-11-11.md (author-approved 2026-11-11).
# Run from your own machine in the commons-bonds checkout. A cloud session could not do this:
# its GitHub access only allows pushing its own branch and main.
#
# Safe by construction: each branch is tagged archive/2026-11-10/<branch> at the exact commit
# reviewed, the tag is pushed, and the branch is deleted ONLY if its tip on GitHub still matches
# that commit. Undo any one:  git push origin archive/2026-11-10/<branch>:refs/heads/claude/<branch>
set -u
git fetch origin --prune --quiet
ok=0; skip=0
while read -r b sha; do
  [ -z "$b" ] && continue
  tip=$(git rev-parse -q --verify "refs/remotes/origin/claude/$b" || true)
  if [ "$tip" != "$sha" ]; then echo "SKIP $b (tip ${tip:-missing} != reviewed $sha)"; skip=$((skip+1)); continue; fi
  git tag -f "archive/2026-11-10/$b" "$sha" >/dev/null
  git push --quiet origin "refs/tags/archive/2026-11-10/$b" || { echo "TAG PUSH FAILED $b"; skip=$((skip+1)); continue; }
  git push --quiet origin --delete "claude/$b" && { echo "done $b"; ok=$((ok+1)); } || { echo "DELETE FAILED $b"; skip=$((skip+1)); }
  git branch -d "claude/$b" >/dev/null 2>&1 || true   # local ref, if any (never -D)
done <<'LIST'
atlantic-ideas-package-ratification-260601-e8593b eb418a98ab900aff23eb99c426a27e66a92104fd
book-proposal-tier1-260611-e0dbb7 c721061db007898e0f1080ef7cab5949a42a484b
pipeline-prose-revision-corpus-audit-260602-6b5eda d76f80492f4fa8c720ba12b26069407d69ca3525
pm-book-completion-260610-07b75f 62f6728a93f115b5a8a4e99cee79c05b32c6820f
ta-internal-fixes-260607-208b7b 9be1a51699dae2619dd61b2246e2f2d579533126
book-drafting-plan-260618-88009b 2d98e13aaafaf7a72e8b85595ec4824f1cbf440f
nyrb-vd-stage-5-essay-signoff-prepub-refresh-260601-93a0b1 1cf4fb69b6f85a002163ad4d6e60d0c9b0370f07
ta-provenance-11-3-11-4-integral-260610-d22bed 36264c770b25515f6b28c877f3b4300dc6ff9b4c
ta-stage4-markup-260610-70c0bf 8bd707dd9519ee86cd8bd504150f58b4d6c9cd05
ch10-insertion-placement-lucid-pike-cbf748 41509bdf0dcc813aee89a18197908520f56ef0ad
ch9-pass3-5-1fae85 8aeeadcbb45dfae83f440068a474a28dc6ea06e8
christophers-single-book-review-stage-0-663265 676a3fa275273504acd7dedf2587641ba0b180f7
laughing-raman-8b4564 deaa1d54b4de98db7259fb85223032e431819a10
ta-rcv-publication-stability-signoff-663265 792846a3f818a5a3f1ed4af3516c98dfa4e631ca
unruffled-elbakyan-af5b16 80b5aa67648f1db0b383ff162ee9d49cd651c922
rescue-main-checkout-20261110 17b5a3ede55e2dfb6600378f315c9a4d28c04a92
rescue-br-V-E-20261110 c70e6b0185d7e1031852f06e0c91179669cf009d
rescue-ch5-rebuild-20261110 a7db1ea52b3bb420f48cde7091ee554dac8777b0
rescue-mcdowell-recs-20261110 762af030b4905651a39caf678651b1d17b6bb9b9
rescue-noema-draft-20261110 1aaa31e98fab6819bb4cea15a543c153870800cc
rescue-noema-vd-cascade-20261110 e73b585c1a72dfabcf84dfb3dd833e4aea8beb3f
rescue-public-books-cover-letter-20261110 6fb5600c5f5ab7f5d8d5586ca4380e17ed8e93c7
rescue-redraft-campaign-resume-20261110 c30b71e14239c71aebfbc7b3c3282dc49d3a1a85
rescue-ta-bibconsol-20261110 fb256fe69b7b22048e6575ec2596c52efc50f67c
rescue-ta-reverse-csd-20261110 59afba3c037417de9f43595e5596e3466c4a4c70
rescue-ta-stage4-markup-20261110 80ce7ee6bd9f7faeb0ef6de49882a82de60dc1c5
rescue-tolerance-spot-fix-20261110 be373a7b2de8def301566d73679cf4e756e27eb5
rescue-agent-worktrees-20261110 053a90dd6ede74377d1d8406e62093515afdb7e9
LIST
echo "deleted: $ok  skipped/failed: $skip"
