# LOG.SET files for the NIBE F370

Generated on 2026-11-23 with upstream `tools/make_logset.py`
(beolink/Nibe-F-series-ModbusAdapter `01f8f22`) and `nibe` 2.26.0.
All registers are 16-bit or smaller. The format is ASCII, TAB-separated, CRLF.

| Folder | Slots | Command |
|---|---|---|
| `default/` | 11/20 | `python tools/make_logset.py --model F370 --out LOG.SET` |
| `extended/` | 18/20 | `python tools/make_logset.py --model F370 --out LOG.SET 40004 40008 40012 40013 40014 40025 40026 43009 43427 43084 43091 43086 45001 43108 40033 40022 40020 40023` |

Copy **one** of them to the root of a FAT32 USB stick. The file must be named exactly
`LOG.SET`. Loading steps: [docs/installation/07-logset.md](../docs/installation/07-logset.md).

Edit the files only with the generator. Line endings and the header matter.
