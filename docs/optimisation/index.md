# Optimisation principles

Start this only after **Gate E** (7 days of verified read-only data).

1. **NIBE keeps control of safety.** Frost protection, compressor protection, pressure/temperature limits, periodic hot water (legionella), alarms and minimum ventilation stay native. Automations only move comfort setpoints within bounded ranges.
2. **Few, slow, bounded writes.** Change a value at most once per hour. Clamp every write: heat offset −3…+2 and hot water Economy/Normal/Luxury. Never touch the heating curve, min/max supply or alarm reset automatically.
3. **Fail-safe default.** If Home Assistant, the price feed or the gateway is down, a watchdog automation sets the offset back to 0 and the hot water mode back to Normal. NIBE then runs as if nothing were connected.
4. **One lever at a time.** Enable one optimisation, watch it for a week, then add the next.
5. **Avoid the immersion heater.** On an F370 the expensive event is the internal electric addition (up to several kW), not the compressor. Price shifting that causes electric addition costs money. Monitor `binary_sensor.nibe_f370_electric_addition_active`.
6. **Exhaust air pumps have limited capacity.** The F370 compressor's output depends on the exhaust airflow. Large negative offsets in cold weather are recovered slowly and may trigger electric addition. Keep pre-heat/set-back modest (±1–2 steps).

## Implementation order

| # | Feature | Page | Write registers used |
|---|---|---|---|
| 1 | Nord Pool price feed | [Nord Pool](nordpool.md) | none |
| 2 | Zigbee room sensors | [Room sensors](room-sensors.md) | none |
| 3 | Room monitoring dashboard | [Room sensors](room-sensors.md) | none |
| 4 | Price-aware heating offset | [Heating](heating.md) | 47011 |
| 5 | Price-aware hot water | [Hot water](hot-water.md) | 47041, 48132 |
| 6 | Humidity-driven ventilation boost | [Ventilation](ventilation.md) | 47260 |
| 7 | Solar/battery | [Solar & battery](solar-battery.md) | 47011/48132 or SG Ready |
| 8 | Energy dashboard | [Energy](energy.md) | none |

All automation drafts are in `homeassistant/packages/nibe_f370_optimisation.yaml`. They ship with `initial_state: false`, so nothing runs until you turn it on.

!!! tip "NIBE Smart Price Adaption"
    The F370 map includes *Smart Price Adaption* registers (44896–44908). NIBE's own price control normally depends on myUplink. This project keeps price logic in Home Assistant for transparency and local operation. Do not run both at the same time.
