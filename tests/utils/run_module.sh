#!/bin/bash -eu

set -o pipefail

# Check if parameter is empty
if [ -z "${1:-}" ]; then
  echo "Module name is required"
  exit 1
fi
# Goto script folder
cd "$( dirname "${BASH_SOURCE[0]}")"
# Get ansible collection parent directory
ANSIBLE_COLLECTION_DIR="$( cd "../../../../.." &> /dev/null && pwd )"
# Goto the root directory
cd ../..
# Update Python path
export PYTHONPATH="$ANSIBLE_COLLECTION_DIR:${PYTHONPATH:-}"
# Run the module
poetry run python3 "plugins/modules/$1.py" "plugins/args/$1.json"
