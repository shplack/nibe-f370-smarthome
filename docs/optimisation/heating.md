# Heating optimisation

**Lever:** Heat Offset S1 (register 47011). It is the same as menu 1.9.1 *offset* and moves the whole heating curve.

| Price level | Offset | Condition |
|---|---|---|
| cheap | **+1** | House mean below max comfort (default 22.0 °C) |
| normal | **0** | — |
| expensive | **−1** (cold: −1 only if BT1 > −10 °C) | House mean above min comfort (20.5 °C), no electric addition running |

The defaults are conservative. Each offset step changes room temperature by roughly 0.5–1 °C over several hours, depending on the house.

## Rules

- Writes at most once per 60 minutes (`mode: single` + condition on last change time).
- Restores **0** when:
    - the price sensor is unavailable for 30 min
    - Home Assistant starts
    - the gateway/integration entity is unavailable
    - electric addition runs during a set-back
- Never more than ±2.

## Enable

1. Find the Heat Offset S1 **number** entity in Nibe Local Easyconf and **enable** it.
2. Set `nibe_offset_entity` in the package substitutions (top of file).
3. Enable the automations `NIBE: price-based heat offset` and `NIBE: watchdog reset to defaults`.
4. Watch for a week: room temperature, compressor run time, electric addition.

## Evaluate

Compare daily kWh × price with a week at offset 0 at similar outdoor temperatures. Exhaust-air pumps have a small thermal "battery" (the house itself). The savings are real but modest, often a few percent of the heating cost.
