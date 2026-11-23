# Compatibility checks (F370 / EB100)

Complete every check before the electrician opens the pump. Each check lists the evidence and how to close it.

## Check 1: main software version

**Why:** the NIBE MODBUS 40 manual states:

> *"The climate unit's software must be the latest recommended version or have a version number greater than 3000."*
> *"The climate unit's software must be software version 5539 … or later in order for it to work with v.10 in MODBUS 40."*

The gateway introduces itself as a **MODBUS 40 v10**, so aim for **≥ 5539**.

**What we know:** menu 3.1 shows *Display version 9721R3*, *Base version 43*, *Input version 38*. 9721R3 belongs to the display firmware and is **not** the main controller software number used in that requirement. The F-series display line (the display's "version" field) often uses a 4-digit+R format. Treat it as unverified.

**How to close it (in order of effort):**

1. **Menu 3.1 on the display.** Scroll the whole list. Some F370 builds show *software version* or *programvara* separately from display/base/input.
2. **myUplink / NIBE Uplink** (if the pump was ever connected): *System → Software* shows the installed version and whether an update exists.
3. **Ask the installer/NIBE support** with the serial number.
4. **On the bus, after installation:** the pump's product message contains the main software version. Run [`tools/verify_gateway.py`](https://github.com/YOUR-GITHUB-USER/nibe-f370-smarthome/blob/main/tools/verify_gateway.py) or read the Nibe Local Easyconf device page. Use this as the final confirmation.

**If it is ≤ 5539 or unknown:** update the pump from a USB stick with NIBE's latest F370 software before relying on the gateway. NIBE distributes it through myUplink/NIBE Uplink (*Software*) or your installer. The update uses the same display USB port, under menu 7.1. Follow NIBE's instructions for your exact model.

!!! note "Base 43 / Input 38"
    These are the base board and input board (AA3) firmware revisions. They show the controller's board generation. They do not replace the main software number.

## Check 2: F370 support in the gateway project

| Evidence | Status |
|---|---|
| `Nibe-F-series-ModbusAdapter` README: "F-series here means … F370/F470 …" | ✅ Listed |
| Same README: "Built and measured on an F1255‑16 CU" | ⚠️ F370 not measured |
| `nibe-gw.yaml` contains nothing model-specific (UART + MODBUS 40 emulation) | ✅ Same firmware for all F models |
| NIBE MODBUS 40 manual: F370 uses the **same AA3‑X4 terminal block** as F730/F750 | ✅ Wiring maps directly |

**Verdict:** the firmware should work unchanged. The only model-specific parts are the wiring position (verified from NIBE's manual) and the register map (Check 3).

## Check 3: register map

The `nibe` library (2.26.0) ships `f370_f372_f470.json` with 489 registers. Everything in the read-only monitoring list exists in it:

| Value | Register | Present |
|---|---|---|
| BT1 Outdoor | 40004 | ✅ |
| BT2 Supply S1 | 40008 | ✅ |
| BT3 Return | 40012 | ✅ |
| BT6 HW load | 40014 | ✅ |
| BT7 HW top | 40013 | ✅ |
| BT20 Exhaust air | 40025 | ✅ |
| BT21 Vented (extract) air | 40026 | ✅ |
| Compressor state | 43427 | ✅ |
| Int. el. add. power / state | 43084 / 43091 | ✅ |
| Priority | 43086 | ✅ |
| Alarm | 45001 | ✅ |
| Degree minutes | 43005 / 40940 | ❌ **Not in F370 map** |

## Check 4: Home Assistant integration

`HA-Nibe-Easyconf` v1.15.4 includes F370 in `EXHAUST_AIR = {"F370","F372","F470","F730","F750"}` and has statistics mappings for it. It requires `nibe>=2.24`. Your Home Assistant must be **≥ 2025.2** (from `hacs.json`).

**Close it:** after installing, check *Settings → Devices → NIBE F370* shows model `F370` and a software version.

## Check 5: degree minutes

On F1155/F1255/F730/F750 the library knows *Degree Minutes (16 bit)* at 43005. The F370 map does not include it, probably because NIBE's published F370 register export leaves it out. Possible ways forward:

1. After installation, try to read **43005** manually (e.g. `verify_gateway.py --read 43005`). F-series pumps answer reads of registers outside the published map, so a plausible value (−60 … −1000 in winter) is a good sign. Compare it with the display (menu 3.1 / *Gradminuter*).
2. If it works, add it to the extended `LOG.SET` and report it upstream (`yozik04/nibe`).
3. If it does not, use compressor state + supply vs. calculated supply as a proxy.

## Check 6: home network

- The gateway and Home Assistant must be on the same L2 network/VLAN for mDNS discovery. Unicast UDP 9999/10000 must flow both ways.
- Home Assistant needs a **fixed IP** (DHCP reservation), because the gateway's allow-list uses it.
- If Home Assistant runs in **Docker**, use `network_mode: host`. Otherwise UDP replies and mDNS do not arrive.

## Sign-off

- [ ] Check 1 software ≥ 5539 (or > 3000 confirmed working)
- [ ] Check 2/3 desk review accepted
- [ ] Check 4 HA ≥ 2025.2, HACS installed
- [ ] Check 6 HA static IP, host networking
