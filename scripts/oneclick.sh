#!/usr/bin/env bash
set -euo pipefail

# One-click: setup + launch Blender with BVTK autoload enabled.
# Usage:
#   bash scripts/oneclick.sh /path/to/blender-4.2.10-linux-x64/blender
# If omitted, will try $HOME/Source/blender-4.2.10-linux-x64/blender

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BLENDER_BIN="${1:-$HOME/Source/blender-4.2.10-linux-x64/blender}"

echo "[oneclick] Using blender: $BLENDER_BIN"
bash "$REPO_ROOT/scripts/setup.sh" "$BLENDER_BIN"

LAUNCHER="$HOME/Desktop/blender-bvtk"
if [[ ! -x "$LAUNCHER" ]]; then
  echo "[oneclick] Launcher not found or not executable: $LAUNCHER" >&2
  exit 1
fi

exec "$LAUNCHER"



