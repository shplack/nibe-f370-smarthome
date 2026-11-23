# Safety

!!! danger "Read before touching anything"
    - The NIBE F370 contains **hazardous mains voltage (3x400V)** and stored heat. Its internal electric heater can be several kW.
    - **Do not open, wire or modify a powered heat pump.**
    - NIBE's MODBUS 40 manual (IHB 1822‑10) says: *"All electrical connections must be carried out by an authorised electrician … The climate unit must not be powered when installing MODBUS 40."* The same applies to any device that replaces it.
    - In Sweden, work on fixed installations is regulated (Elsäkerhetsverket, *auktoriserad elinstallatör*). Use an authorised installer.

## What the owner may do

- Read menus on the display (menu 3.1 service info, menu 1–4).
- Flash and bench test the ESP32 on a desk, powered by USB-C only.
- Configure Home Assistant.
- Insert a USB stick into the display's USB port to load `LOG.SET` (no tools, no cover removal).

## What the electrician does

- Isolates the pump at the supply and locks it off. Verifies it is dead.
- Routes the RS‑485 twisted pair through a proper cable gland/grommet, **segregated from mains conductors** in the cabinet.
- Terminates on AA3‑X4:11 (A) and X4:10 (B). **Leaves X4:9 (GND) and X4:12 (12V) unconnected.**
- Makes sure the ESP32 board and its USB supply sit **outside** the pump cabinet in an insulated enclosure.
- Restores covers, powers up and checks for alarms.

## Rules this project follows

1. NIBE frost protection, compressor protection, high-pressure and temperature limits, legionella (periodic hot water), alarms and **minimum ventilation** are never overridden.
2. Monitoring is read-only until values have been verified for at least a week.
3. Write controls are added one at a time, with bounded ranges and a safe fallback when Home Assistant or the gateway is offline.
4. The X4:12 12V output on the pump is **never** used to power the gateway. The project powers it separately over USB-C.
