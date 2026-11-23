# Installation overview

!!! tip "Confirmed setup"
    Home Assistant OS on a Raspberry Pi, with a Linux PC for flashing (Windows as fallback). Follow the short path in [This setup](my-setup.md).

The installation is a sequence of **gated** steps. Do not start a step until the previous gate has passed.

| Step | Who | Pump powered? | Gate to pass |
|---|---|---|---|
| [1. Prepare](01-prepare.md) | Owner | Yes (read menus only) | Software version known, HA type known, HA has fixed IP |
| [2. Build & flash gateway](02-flash.md) | Owner | n/a | ESPHome build succeeds, board flashed |
| [3. Bench test](03-bench-test.md) | Owner | n/a | Gateway on Wi-Fi, logs visible, mDNS name resolves |
| [4. Electrical connection](04-electrical.md) | **Electrician** | **No, isolated** | A/B on X4:11/X4:10, GND open, pump restarts without alarms |
| [5. Enable MODBUS 40](05-enable-modbus40.md) | Owner | Yes | RS‑485 LEDs blink, no communication alarm, product message = F370 |
| [6. Home Assistant](06-home-assistant.md) | Owner | Yes | Read-only values match the display |
| [7. LOG.SET](07-logset.md) | Owner | Yes | Pushed values arrive every ~2 s |

Estimated time, not counting the electrician: 2–4 hours.

## Pinned upstream versions

This documentation was checked against:

| Project | Version / commit |
|---|---|
| beolink/Nibe-F-series-ModbusAdapter | `01f8f22314367ec8005ea21d12f5b5075e6cbbf0` (2026-09-15) |
| beolink/HA-Nibe-Easyconf | v1.15.4, `3412eda9f5dc0e7ffa9f8b8f2171718e63e58487` (2026-11-19) |
| yozik04/nibe | 2.26.0 |
| elupus/esphome-nibe | fetched at build time by ESPHome (`github://elupus/esphome-nibe`) |

Before following any step, check upstream for changes. `firmware/fetch-upstream.sh` checks out the pinned commit by default, or `main` if you pass `--latest`.
