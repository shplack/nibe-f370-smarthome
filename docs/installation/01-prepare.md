# 1. Prepare

## Read the pump's service info

1. On the F370 display, open **menu 3.1 Service info**.
2. Write down every version line. You already have: display 9721R3, base 43, input 38, git 9959073.
3. There is no separate *software / programvara* line. The **Display version** (9721R3) is the main software version.
4. If myUplink is available, check *Software version* there as well.
5. Also check that **menu 5.2 System settings** opens on your unit. Hold **Back** for 7 seconds in the main menu to open the service menu (menu 5). Just look; **do not change anything yet**.

See [Compatibility check 1](../compatibility.md#check-1-main-software-version) for what to do if the version cannot be found.

## Identify your Home Assistant installation type

In Home Assistant go to **Settings → About** (or *Settings → System → Repairs → ⋮ → System information*) and read **Installation type**:

| Shown | Meaning | ESPHome | HACS |
|---|---|---|---|
| Home Assistant OS | Appliance (RPi, Green, Yellow, VM) | **ESPHome Device Builder add-on** (easiest) | HACS add-on/download script |
| Home Assistant Supervised | Debian + Supervisor | Same as OS | Same as OS |
| Home Assistant Container | Docker only, no add-ons | ESPHome CLI on a PC, or its own Docker container | Download script into `/config` |
| Home Assistant Core | Python venv | ESPHome CLI on a PC | Download script |

Record the result in [Project status](../status.md).

## Give Home Assistant a fixed IP

In your router, add a **DHCP reservation** for the Home Assistant host. The gateway only accepts requests from IPs listed in `secrets.yaml`.

If you run **Container**, make sure the container uses `network_mode: host`.

## Install HACS (if not already)

Follow <https://hacs.xyz/docs/use/>. HACS needs a GitHub account for the device-login step.

## Gather

- [ ] Wi-Fi SSID and password (2.4 GHz; the ESP32-S3 has no 5 GHz)
- [ ] Wi-Fi signal near the heat pump. Check it with a phone. Aim for better than −75 dBm
- [ ] Home Assistant IP: `192.168.x.y`
- [ ] Your PC's IP (for testing), or reuse the HA IP
- [ ] The pump's serial number (rating plate). It is only used in local `secrets.yaml`
