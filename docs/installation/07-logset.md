# 7. LOG.SET (push up to 20 values every ~2 s)

## Ready-made files for the F370

This repository contains two files generated with upstream `tools/make_logset.py` (nibe 2.26.0). Only 16-bit registers are used.

| File | Slots | Contents |
|---|---|---|
| [`logset/default/LOG.SET`](https://github.com/shplack/nibe-f370-smarthome/blob/main/logset/default/LOG.SET) | 11/20 | Upstream default selection for the F370: BT1, BT2, BT3, BT7, BT6, BT17, Calc. supply S1, compressor state, int. el. add. power, priority, alarm |
| [`logset/extended/LOG.SET`](https://github.com/shplack/nibe-f370-smarthome/blob/main/logset/extended/LOG.SET) | 18/20 | Default **plus** BT20 exhaust, BT21 vented air, int. el. add. state, fan speed current, BT50 room S1, BT16 evaporator, BT18 compressor temp |

Start with **default**. Change to extended once everything is stable.

## Regenerate (verify script arguments first)

The script's current arguments (checked at upstream `01f8f22`): `--model`, `--out` (the filename must be exactly `LOG.SET`), `--list`, and optional positional registers.

```bash
pip install nibe
git clone https://github.com/beolink/Nibe-F-series-ModbusAdapter.git
cd Nibe-F-series-ModbusAdapter
python tools/make_logset.py --help
python tools/make_logset.py --model F370 --list                 # preview
python tools/make_logset.py --model F370 --out /path/to/USB/LOG.SET
# custom selection:
python tools/make_logset.py --model F370 --out LOG.SET 40004 40008 40012 40013 40014 40025 40026 43009 43427 43084 43091 43086 45001
```

## Load it into the F370

The upstream procedure is written for an F1255 (menu 7.2 *loggning*). The F370 display has the same USB menu family, but **check the menu labels on your display**:

1. Copy the file to the **root** of a **FAT32** USB stick, named exactly `LOG.SET`. On macOS, run `dot_clean /Volumes/<stick>` before ejecting.
2. Insert the stick into the **display's USB port**. A USB menu (menu 7) appears.
3. Open the **logging** submenu (7.2 on F1255) and tick **activated**. If there is an option to *ignore LOG.SET*, leave it unticked.
4. Wait **15 seconds**, untick **activated**, then remove the stick.

The selection stays in the pump. To clear it, load a `LOG.SET` that has no register lines.

## Verify

- In Home Assistant the pushed entities update every ~2 s.
- Register **48889** *MODBUS40 Disable LOG.SET* should read *use LOG.SET*. Nibe Local Easyconf exposes it as a disabled entity named *LOG.SET-fil*.

!!! note "Unverified upstream"
    It is not known whether the selection survives a power cut. After an outage, if pushed values stop or look broken, load the file again.

## Gate F

- [ ] Pushed values update every ~2 s
- [ ] Remaining read polling has no timeouts
