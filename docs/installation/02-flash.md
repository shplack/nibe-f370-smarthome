# 2. Build and flash the gateway

Pick **one** route:

- **Route A**: Home Assistant OS/Supervised, using the ESPHome Device Builder add-on plus browser flashing. Works from any OS with Chrome/Edge.
- **Route B**: the ESPHome CLI on Windows, macOS or Linux. Use this with HA Container/Core.

## Route A: ESPHome Device Builder add-on (HA OS / Supervised)

1. **Settings → Add-ons → Add-on store → ESPHome Device Builder → Install → Start**, then **Open Web UI**.
2. **+ New device → Continue → skip**, and name it e.g. `nibe-gw` (you will replace the YAML).
3. Click **Edit** on the new device and replace the whole YAML with the upstream [`esphome/nibe-gw.yaml`](https://github.com/beolink/Nibe-F-series-ModbusAdapter/blob/main/esphome/nibe-gw.yaml).
4. Click **Secrets** (top right) and add the keys from the [secrets template](#secretsyaml) below.
5. **Install → Manual download → Factory format**. This compiles the firmware (it takes several minutes the first time).
6. Connect the board by USB‑C to the computer you are using the browser on. Open <https://web.esphome.io> in **Chrome or Edge**, click **Connect**, choose the serial port, then **Install** and select the downloaded `.bin`.

    !!! tip "Board not detected?"
        Hold **BOOT**, tap **RESET** (or plug in USB while holding BOOT), then release BOOT. The board then enters download mode. On Windows the native USB‑Serial/JTAG driver is built in, so no CH340 driver is needed.

## Route B: ESPHome CLI

```bash
# 1. Python 3.11+ and git required
python3 -m venv ~/esphome-venv
source ~/esphome-venv/bin/activate          # Windows: %USERPROFILE%\esphome-venv\Scripts\activate
pip install esphome

# 2. Get the pinned upstream config (or clone manually)
git clone https://github.com/beolink/Nibe-F-series-ModbusAdapter.git
cd Nibe-F-series-ModbusAdapter
git checkout 01f8f22314367ec8005ea21d12f5b5075e6cbbf0   # optional: the reviewed commit

# 3. Secrets
cp esphome/secrets.example.yaml esphome/secrets.yaml
#    edit esphome/secrets.yaml (see below)

# 4. Build and flash over USB-C (choose the serial port when asked)
esphome run esphome/nibe-gw.yaml
```

In this repository, `firmware/fetch-upstream.sh` runs steps 2–3 for you.

If the first build stops with *"Can not perform a '--user' install"*, run it as `PIP_USER=0 esphome run esphome/nibe-gw.yaml` (upstream note).

Linux: add yourself to the `dialout` group (`sudo usermod -aG dialout $USER`, then log in again) if the port is not accessible.

## secrets.yaml

```yaml
wifi_ssid: "your-network"
wifi_password: "your-wifi-password"
ap_password: "fallback-ap-password-8+chars"
# python3 -c "import base64,secrets;print(base64.b64encode(secrets.token_bytes(32)).decode())"
api_encryption_key: "...32 random bytes base64..."
ota_password: "choose-a-password"
ha_ip: "192.168.1.10"      # Home Assistant (fixed IP!)
dev_ip: "192.168.1.20"     # PC for testing, or same as ha_ip
device_name: "nibe-<serial-lowercase>-gw"
device_friendly_name: "NIBE F370"
```

!!! danger "Do not change"
    `tx_pin: GPIO17`, `rx_pin: GPIO18`, `dir_pin: GPIO21`, `baud_rate: 9600`, and the MODBUS40 `acknowledge`/`constants` block. These come from the Waveshare schematic and the NIBE protocol. They are not tuning knobs.

## Gate

- [ ] Build finished with `SUCCESS`
- [ ] Flash finished. The board reboots and its log shows `Connected to WiFi` with an IP
