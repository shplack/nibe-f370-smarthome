#!/usr/bin/env bash
# Fetch the upstream NibeGW ESPHome configuration at the reviewed commit and
# prepare secrets.yaml. Use --latest to take upstream main instead (re-check
# the docs if you do).
set -euo pipefail

PINNED=01f8f22314367ec8005ea21d12f5b5075e6cbbf0
REPO=https://github.com/beolink/Nibe-F-series-ModbusAdapter.git
DEST="$(cd "$(dirname "$0")" && pwd)/upstream"

if [[ -d "$DEST/.git" ]]; then
  git -C "$DEST" fetch --quiet origin
else
  git clone --quiet "$REPO" "$DEST"
fi

if [[ "${1:-}" == "--latest" ]]; then
  git -C "$DEST" checkout --quiet origin/main
  echo "Checked out upstream main: $(git -C "$DEST" rev-parse --short HEAD) (NOT the reviewed commit)"
else
  git -C "$DEST" checkout --quiet "$PINNED"
  echo "Checked out reviewed commit ${PINNED:0:7}"
fi

if [[ ! -f "$DEST/esphome/secrets.yaml" ]]; then
  cp "$DEST/esphome/secrets.example.yaml" "$DEST/esphome/secrets.yaml"
  key=$(python3 -c "import base64,secrets;print(base64.b64encode(secrets.token_bytes(32)).decode())")
  sed -i.bak "s|REPLACE-WITH-32-RANDOM-BYTES-BASE64|$key|" "$DEST/esphome/secrets.yaml" && rm -f "$DEST/esphome/secrets.yaml.bak"
  echo "Created $DEST/esphome/secrets.yaml with a random API key. Edit Wi-Fi, IPs and device_name now."
fi

cat <<EOF

Next:
  1. Edit firmware/upstream/esphome/secrets.yaml
     device_friendly_name: "NIBE F370"
  2. esphome run firmware/upstream/esphome/nibe-gw.yaml
Do NOT change GPIO17/18/21, 9600 baud or the MODBUS40 blocks.
EOF
