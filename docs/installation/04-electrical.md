# 4. Electrical connection (qualified electrician)

!!! danger "Electrician only, pump isolated"
    Give this page to your electrician. The owner must not open the F370.

## Work order for the electrician

**Task:** connect a third-party RS‑485 accessory, electrically equivalent to NIBE MODBUS 40, to the F370 input board.

| | |
|---|---|
| Pump | NIBE F370 CU 3x400V, controller EB100 |
| Connection point | Input board **AA3**, terminal block **X4** |
| Reference | NIBE MODBUS 40 installer manual IHB 1822‑10, section *Connecting communication → F370, F470, F730, F750* |
| Cable | Twisted pair, LiYY / EKKX or similar (NIBE recommendation). Shield, if present, earthed **at one end only**, per local practice |

### Terminal mapping

| Waveshare RS‑485 terminal | F370 AA3‑X4 | NIBE function |
|---|---|---|
| **A+** | **X4:11** | A |
| **B‑** | **X4:10** | B |
| *(none)* | X4:9 | GND: **leave unconnected** |
| *(none)* | X4:12 | 12 V: **leave unconnected** |

Reasons:

- The Waveshare RS‑485 side is **galvanically isolated** and has no ground terminal. Joining GND would defeat the isolation and could create a ground loop.
- The gateway is powered by its own USB‑C supply. Do not load the pump's 12 V rail.
- Termination jumper **H2 on the pump**: leave it **as delivered (open)**. The **Waveshare 120 Ω jumper**: leave it **open** (default).

### Steps

1. Isolate the F370 at its supply and lock it off. Prove it dead.
2. Remove the front cover according to the F370 installer manual.
3. Locate AA3 and X4. Confirm the 9/10/11/12 numbering on the board print against the NIBE diagram.
4. Route the twisted pair through an existing low-voltage grommet. Keep it **segregated from mains and compressor wiring**.
5. Terminate A → X4:11 and B → X4:10 with ferrules. Make sure no strands are loose.
6. Mount the gateway in its insulated enclosure **outside** the pump. Connect A+/B‑ on the board. Plug in the USB‑C supply.
7. Refit covers. Restore power.
8. Confirm that the pump starts normally with **no new alarms**. (MODBUS 40 is not enabled yet, so the bus should be silent apart from the pump's own polling.)

## If A/B are swapped

You will see no valid telegrams and no RS‑485 green LED. NIBE also says: *"Check that A is connected to + and B to −."* Swapping is harmless at RS‑485 levels, but must be corrected **with the pump isolated**.

## Gate C

- [ ] Electrician confirms the connection and that the pump restarted without alarms
- [ ] Photo of the X4 terminals saved (privately) for the record
