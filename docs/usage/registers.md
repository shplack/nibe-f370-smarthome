# Register reference (F370)

Extracted from `nibe` 2.26.0, `f370_f372_f470.json` (489 registers). **W** = writable. The value shown = raw ÷ factor.

## Read-only measurements

| Reg | Size | Factor | Unit | Title |
|---|---|---|---|---|
| 40004 | s16 | 10 | °C | BT1 Outdoor Temperature |
| 40008 | s16 | 10 | °C | BT2 Supply temp S1 |
| 40012 | s16 | 10 | °C | EB100-EP14-BT3 Return temp |
| 40013 | s16 | 10 | °C | BT7 HW Top |
| 40014 | s16 | 10 | °C | BT6 HW Load |
| 40020 | s16 | 10 | °C | EB100-BT16 Evaporator temp |
| 40022 | s16 | 10 | °C | EB100-EP14-BT17 Suction |
| 40023 | s16 | 10 | °C | EB100-BT18 Compressor temp. |
| 40025 | s16 | 10 | °C | BT20 Exhaust air temp. 1 |
| 40026 | s16 | 10 | °C | BT21 Vented air temp. 1 |
| 40033 | s16 | 10 | °C | BT50 Room Temp S1 (if a room sensor is fitted) |
| 40079/81/83 | u32 | 10 | A | EB100-BE3/BE2/BE1 Current (only with current sensors) |
| 41027 | s16 | — | % | Humidity average (only with a humidity sensor) |
| 43001 | u16 | 1 | | Software version |
| 43009 | s16 | 10 | °C | Calc. Supply S1 |
| 43084 | s16 | 100 | kW | Int. el.add. Power |
| 43091 | u8 | 1 | | Int. el.add. State |
| 43086 | u8 | 1 | | Prio (10 Off, 20 Hot Water, 30 Heat, 40 Pool, 50 Transfer, 60 Cooling) |
| 43108 | u8 | 1 | % | Fan speed current |
| 43416 | s32 | 1 | | Compressor starts |
| 43420 | s32 | 1 | h | Tot. op.time compressor |
| 43424 | s32 | 1 | h | Tot. HW op.time compressor |
| 43427 | u8 | 1 | | Compressor State EP14 |
| 44331 | u8 | 1 | | Software release |
| 45001 | s16 | 1 | | Alarm |
| 44874 | u8 | 1 | | State SG Ready |

## Writable settings (use only after Gate E)

| Reg | Range | Title | Use in this project |
|---|---|---|---|
| 47011 | −10…10 | **Heat Offset S1** (W) | Primary price lever |
| 47007 | 0…15 | Heat Curve S1 (W) | **Do not automate.** Set once by hand |
| 47041 | 0 Economy, 1 Normal, 2 Luxury, 4 Smart Control | **Hot water comfort mode** (W) | Price lever |
| 48132 | 0 Off, 1 3h, 2 6h, 3 12h, 4 One-time | **Temporary Lux** (W) | Pre-heat in cheap hours |
| 47260 | 0 Normal, 1–4 | **Fan Mode** (W) | Humidity boost |
| 47265 / 47264… | % | Exhaust fan speed normal / 1–4 (W) | **Set by hand only.** Never below commissioning value |
| 47394 | 0/1 | Use room sensor S1 (W) | Optional |
| 47398 | 5.0…30.0 | Room sensor setpoint S1 (W) | Optional |
| 47387 | 0/1 | HW production (W) | **Do not automate** |
| 48282/48284 | | SG Ready heating / hot water (W) | Alternative to offsets |
| 48852 | 0/1 | Modbus40 Word Swap | Leave alone |
| 45171 | | Alarm Reset (W) | **Never automate** |

## Missing from the F370 map

- 43005 *Degree Minutes (16 bit)* and 40940 *Degree Minutes (32 bit)*. See [Compatibility check 5](../compatibility.md#check-5-degree-minutes).
