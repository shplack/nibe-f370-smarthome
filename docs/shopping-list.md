# Shopping list

Prices are approximate (November 2026, SEK incl. VAT) and change often. Waveshare lists the board at **USD 18.99–19.99** on its own store. Shipping and import VAT to Sweden come on top.

!!! tip "Do not buy"
    - NIBE **MODBUS 40**: this project replaces it.
    - A separate USB‑RS485 adapter: the Waveshare board has an isolated RS‑485 port built in.

## Core: required (≈ 340–670 SEK)

| # | Item | Notes | Approx. SEK | Where |
|---|---|---|---|---|
| 1 | **Waveshare ESP32-S3-RS485-CAN** | Exactly this model, **not** the `-U` (SMA antenna) variant. Ships in a DIN-rail case, 91.6 × 58.7 × 23.3 mm. The upstream pin mapping (GPIO17/18/21) is specific to it | 220–350 | [Waveshare](https://www.waveshare.com/esp32-s3-rs485-can.htm) · [Mouser SE](https://www.mouser.se/ProductDetail/Waveshare/ESP32-S3-RS485-CAN) · [AliExpress (official Waveshare store, check seller)](https://www.aliexpress.com/w/wholesale-waveshare-esp32-s3-rs485-can.html) |
| 2 | **Twisted-pair cable, 2-core (or 2x2), shielded preferred** | NIBE recommends **LiYY, EKKX** or similar. Length = pump terminal → enclosure (keep it short, typically 1–3 m) | 50–150 | Electrical wholesaler (Ahlsell, Elektroskandia, Solar via your electrician) |
| 3 | **Small insulated enclosure (IP-rated, plastic)** | Small IP65 DIN-rail enclosure (4–6 modules) fits the board's rail case. Or a junction box with inner size ≥ 100×65×35 mm and 2 cable glands. Mount it *outside* the pump | 50–120 | Electrokit, Kjell, Biltema |
| 4 | **Ferrules (0.25–0.5 mm²) + cable glands** | For the screw terminals. The electrician usually has these | 20–50 | Electrician / Biltema |

## Already owned (owner, 2026-11-23)

- Home Assistant OS on a Raspberry Pi, with Zigbee already set up (coordinator and sensors)
- FAT32 USB stick for LOG.SET
- USB‑C cable that carries **data** (needed for the first flash; charge-only cables don't work)
- USB power supply: owner sources it. It must be **5 V ≥ 1 A, CE marked** (a branded phone charger is fine). It powers the gateway permanently

## Optional

| Item | Purpose | Approx. SEK | Link |
|---|---|---|---|
| Energy meter / P1 reader (HAN port) | Whole-house kWh for the energy dashboard | 300–600 | e.g. [Home Assistant Glow](https://github.com/klaasnicolaas/home-assistant-glow) (DIY, LED pulse) or a HAN/P1 reader for your grid operator's meter |

## Not needed for this project

- RS‑485 termination resistor (leave the onboard jumper open)
- 12 V power supply (do not use the pump's X4:12)
- CAN wiring (the CAN port is unused)

## Budget summary

| Phase | Min | Max |
|---|---|---|
| Core gateway | ~340 | ~670 |
| Electrician (1 visit, typical) | not estimated: get a quote | |
