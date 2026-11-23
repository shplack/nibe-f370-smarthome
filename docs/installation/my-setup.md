# This installation: HA OS on Raspberry Pi + Linux PC

This page is the short path for the confirmed setup. The generic pages still apply. This page tells you which options to pick.

| Decision | Choice | Why |
|---|---|---|
| Home Assistant | **Home Assistant OS on Raspberry Pi**, newer than 2025.2 | Meets Nibe Local Easyconf's minimum (2025.2). HA OS uses host networking, so UDP 9999/10000 and mDNS discovery work without configuration |
| Firmware build + first flash | **Linux PC, ESPHome CLI** | Compiling ESP-IDF firmware on a Pi is slow (often 15–30+ min) and memory-hungry. On a PC it takes a few minutes |
| Fallback flashing | **Windows**, Chrome/Edge + <https://web.esphome.io> | Use it if the Linux USB port causes trouble |
| Later updates | OTA over Wi-Fi from the Linux PC | Same `esphome run` command |
| ESPHome add-on on the Pi | Optional | Only needed if you want to view gateway logs or edit YAML from the HA UI |
| HACS | Required (if not already installed) | Nibe Local Easyconf is a HACS custom repository |

## Step-by-step

### 0. Buy the board

The board is **not bought yet**. Order the **Waveshare ESP32-S3-RS485-CAN** plus a USB‑C *data* cable and a 5 V USB supply ([Shopping list](../shopping-list.md)). Check that the listing title says exactly `ESP32-S3-RS485-CAN`. Waveshare sells several similar ESP32-S3 RS485 boards with **different pinouts**.

While you wait for delivery, do steps 1–3.

### 1. Home Assistant (Pi)

1. Give the Pi a **DHCP reservation** in the router, then write down its IP. That address goes into `ha_ip`.
2. Check the version: **Settings → About**. It must be 2025.2 or newer. Yours already is.
3. Install HACS if it is missing: <https://hacs.xyz/docs/use/>.
4. Install **Nibe Local Easyconf** now ([step 6](06-home-assistant.md#install)), then restart. Don't add the device yet; there is nothing to find until the gateway is running.
5. Optional: if you want the gateway's logs in the HA UI, install the **ESPHome Device Builder** add-on. You don't have to build with it.

### 2. Find the main software version (pump, no tools)

Check menu 3.1 and myUplink ([Compatibility check 1](../compatibility.md#check-1-main-software-version)). If you can't find it, `verify_gateway.py` reads it later in step 5.

### 3. Prepare the Linux PC

```bash
sudo apt install python3-venv git            # Debian/Ubuntu; use your distro's equivalent
python3 -m venv ~/esphome-venv
source ~/esphome-venv/bin/activate
pip install esphome nibe
sudo usermod -aG dialout $USER               # then log out and back in

git clone https://github.com/shplack/nibe-f370-smarthome.git
cd nibe-f370-smarthome
./firmware/fetch-upstream.sh                 # pinned upstream config + secrets.yaml with random API key
nano firmware/upstream/esphome/secrets.yaml
```

In `secrets.yaml` set:

- `wifi_ssid` and `wifi_password`. Must be a 2.4 GHz network.
- `ap_password` and `ota_password`.
- `ha_ip`: the Pi's reserved IP.
- `dev_ip`: the Linux PC's IP. Give it a reservation too, or reuse `ha_ip`.
- `device_name: "nibe-<serial-lowercase>-gw"`
- `device_friendly_name: "NIBE F370"`

You can compile **before the board arrives**. This catches config errors early:

```bash
esphome compile firmware/upstream/esphome/nibe-gw.yaml
```

### 4. When the board arrives: flash and bench test

```bash
source ~/esphome-venv/bin/activate
# plug the board in by USB-C; it shows up as /dev/ttyACM0 (native USB)
esphome run firmware/upstream/esphome/nibe-gw.yaml      # choose /dev/ttyACM0
```

If the port does not appear, hold **BOOT**, plug in USB (or tap RESET), then release BOOT and try again.

Then follow [Bench test](03-bench-test.md). Leave it running for 24 h before the electrician visits.

**Windows fallback:** in WSL or the Linux PC, run `esphome compile …`. Copy `.esphome/build/<name>/.pioenvs/<name>/firmware.factory.bin` to Windows. On Windows, open <https://web.esphome.io> in Chrome/Edge → **Connect** → **Install** → pick the file.

### 5. Electrician, then MODBUS 40, then verify

1. [Electrical connection](04-electrical.md): hand the page to the electrician.
2. [Enable MODBUS 40](05-enable-modbus40.md) in menu 5.2.
3. From the Linux PC (`dev_ip`):

    ```bash
    source ~/esphome-venv/bin/activate
    python tools/verify_gateway.py --gateway nibe-<serial>-gw.local
    python tools/verify_gateway.py --gateway nibe-<serial>-gw.local --read 43005   # degree minutes probe
    ```

    Record the model and software version in [Project status](../status.md).

    !!! note
        Run `verify_gateway.py` **before** adding the device in Home Assistant, or at least not from the Pi. The script listens on UDP 9999 on the PC, so it doesn't clash with HA.

4. In Home Assistant the gateway should show up under **Discovered**. Add it and keep everything read-only ([step 6](06-home-assistant.md)).

### 6. Raspberry Pi specifics

- **SD card wear:** the recorder writes every LOG.SET value about every 2 s. On an SD card, consider booting from SSD. Or exclude the fast-changing NIBE sensors from the recorder, or keep only `recorder: purge_keep_days: 10`.
- **Zigbee later:** plug the coordinator into a USB **2.0** port on a **0.5–1 m extension cable**. USB 3 ports and SSDs on a Pi interfere badly with 2.4 GHz.
- **Backups:** take a full HA backup before installing HACS integrations and before enabling any write automations.
