# Project status

Update this page as each item is resolved. It is the single place that says how far the project has come.

## Known facts

| Item | Value | Source |
|---|---|---|
| Heat pump | NIBE F370, CU 3x400V | Rating plate |
| Country | SE | Menu 3.1 |
| Controller / product | EB100 | Menu 3.1 |
| Display version | 9721R3 | Menu 3.1. **Display** version only, not the main software version |
| Base version | 43 | Menu 3.1 |
| Input version | 38 | Menu 3.1 |
| Configuration changed | No | Menu 3.1 |
| Git identifier | 9959073 | Menu 3.1 |
| Serial number | On the rating plate / photo | Keep out of public repos (see note) |
| Home Assistant | **Home Assistant OS on a Raspberry Pi**, version newer than 2025.2 | Owner, 2026-11-23 |
| Flashing computer | Windows **and** Linux available. Linux CLI is the chosen route | Owner, 2026-11-23 |

!!! warning "Serial number"
    Upstream recommends naming the gateway `nibe-<serial>-gw`. That name ends up only in your local `secrets.yaml`, which git ignores. **Do not** put the serial in this public repository.

## Open questions (answer before wiring)

- [ ] **1. Waveshare ESP32-S3-RS485-CAN purchased?** Not yet (2026-11-23) → [Shopping list](shopping-list.md)
- [x] **2. Computer OS for flashing?** Linux (primary, ESPHome CLI) with Windows as fallback (Chrome/Edge + web.esphome.io) → [Flash](installation/02-flash.md)
- [x] **3. Home Assistant installation type?** Home Assistant OS on a Raspberry Pi, newer than 2025.2. This meets Nibe Local Easyconf's minimum. HA OS uses host networking, so UDP and mDNS work without extra setup → [Prepare](installation/01-prepare.md#identify-your-home-assistant-installation-type)
- [ ] **4. F370 main software version?** NIBE requires **> 3000** for MODBUS 40, and **≥ 5539** for MODBUS 40 v10 behaviour, which this gateway emulates → [Compatibility](compatibility.md#check-1-main-software-version)
- [ ] **5. Repository/firmware support for this exact F370?** Partly verified at desk level (see below). Final proof needs the pump's product message on the bus → [Compatibility](compatibility.md)

## Desk verification done for this project (2026-11-23)

| Check | Result |
|---|---|
| `beolink/Nibe-F-series-ModbusAdapter` lists F370 | ✅ Yes (README, commit `01f8f22`). Measured only on an F1255-16 |
| `beolink/HA-Nibe-Easyconf` handles F370 | ✅ Yes, classed as exhaust-air (`fseries.py`, v1.15.4) |
| `nibe` library has an F370 register map | ✅ `f370_f372_f470.json`, 489 registers (nibe 2.26.0) |
| NIBE MODBUS 40 manual lists F370 and its terminals | ✅ AA3‑X4:9‑12 (GND, B, A, 12V) |
| `make_logset.py --model F370` works | ✅ Generates 11 of 20 slots. Files are in `logset/` |
| `beolink/nibe-local` (old link) | ❌ 404. Use `beolink/HA-Nibe-Easyconf` |
| Degree minutes register for F370 | ⚠️ **Not in the F370 map** (43005/40940 missing). See [Compatibility](compatibility.md#check-5-degree-minutes) |

## Next actions

1. Order the Waveshare ESP32-S3-RS485-CAN, USB‑C data cable and 5 V supply.
2. While waiting: install HACS and Nibe Local Easyconf on the Pi, prepare the Linux PC, and run `esphome compile` ([This setup](installation/my-setup.md)).
3. Look for the main software version in menu 3.1 or myUplink.
4. Book the electrician once the bench test passes.

## Progress gates

- [ ] Gate A: questions 1–4 answered (2 and 3 done; 1 = buy board; 4 = software version)
- [ ] Gate B: gateway flashed, on Wi-Fi, visible in logs ([Bench test](installation/03-bench-test.md))
- [ ] Gate C: electrician connected the RS‑485 pair, pump powered back up without alarms
- [ ] Gate D: MODBUS 40 enabled, product message reports `F370` + software version
- [ ] Gate E: read-only values in HA match the pump display for 7 days
- [ ] Gate F: LOG.SET loaded and confirmed
- [ ] Gate G: first write control enabled (one at a time)
