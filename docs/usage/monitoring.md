# Monitoring

## Core entities

Nibe Local Easyconf names entities from NIBE's register titles. Exact entity IDs depend on your device name. Search *Settings → Entities* for the register title.

| Signal | Register | Unit | Notes |
|---|---|---|---|
| BT1 Outdoor temperature | 40004 | °C | Drives the heating curve |
| BT2 Supply temp S1 | 40008 | °C | Flow to radiators/floor |
| Calc. supply S1 | 43009 | °C | What the curve asks for. Compare with BT2 |
| BT3 Return temp | 40012 | °C | |
| BT7 HW top | 40013 | °C | Usable hot water |
| BT6 HW load | 40014 | °C | Charging sensor |
| BT20 Exhaust air | 40025 | °C | Air leaving rooms |
| BT21 Vented air | 40026 | °C | Air after the evaporator. BT20−BT21 shows heat recovery |
| Compressor state EP14 | 43427 | enum | |
| Int. el. add. power | 43084 | kW | Electric immersion heater. **Expensive** |
| Int. el. add. state | 43091 | enum | |
| Prio | 43086 | enum | Off / Hot Water / Heat / … |
| Alarm | 45001 | code | 0 = no alarm |
| Fan speed current | 43108 | % | |

## Helper package (read-only)

`homeassistant/packages/nibe_f370_monitoring.yaml` adds:

- `binary_sensor.nibe_f370_alarm_active` (alarm ≠ 0)
- `binary_sensor.nibe_f370_electric_addition_active` (int. el. add. power > 0)
- `sensor.nibe_f370_supply_deviation` (BT2 − calculated supply)
- `sensor.nibe_f370_air_heat_recovery` (BT20 − BT21)
- persistent notifications when the alarm turns on, or when electric addition runs for more than 30 min

Enable packages in `configuration.yaml`:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

Copy the file to `/config/packages/`. **Edit the `entity_id`s at the top of the file** to match your entities, then restart.

## Suggested dashboard card

```yaml
type: entities
title: NIBE F370
entities:
  - entity: sensor.REPLACE_bt1_outdoor_temperature
  - entity: sensor.REPLACE_bt2_supply_temp_s1
  - entity: sensor.REPLACE_calc_supply_s1
  - entity: sensor.REPLACE_bt7_hw_top
  - entity: sensor.REPLACE_prio
  - entity: binary_sensor.nibe_f370_electric_addition_active
  - entity: binary_sensor.nibe_f370_alarm_active
```
