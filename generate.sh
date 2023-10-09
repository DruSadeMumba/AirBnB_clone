#!/usr/bin/env bash
# script that generate AUTHORS file
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel)"

set -x
cat > "${ROOT_DIR}/AUTHORS" <<- EOF
        # AUTHORS OF THIS REPO:

        $(git -C "$ROOT_DIR" log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf)
EOF
