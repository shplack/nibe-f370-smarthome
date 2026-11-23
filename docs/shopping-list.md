# Shopping list

Prices are approximate (November 2026, SEK incl. VAT) and change often. Waveshare lists the board at **USD 18.99–19.99** on its own store. Shipping and import VAT to Sweden come on top.

!!! tip "Do not buy"
    - NIBE **MODBUS 40**: this project replaces it.
    - A separate USB‑RS485 adapter: the Waveshare board has an isolated RS‑485 port built in.

## Core: required (≈ 390–690 SEK)

| # | Item | Notes | Approx. SEK | Where |
|---|---|---|---|---|
| 1 | **Waveshare ESP32-S3-RS485-CAN** | Exactly this model. The upstream pin mapping (GPIO17/18/21) is specific to it | 220–350 | [Waveshare](https://www.waveshare.com/esp32-s3-rs485-can.htm) · [Mouser SE](https://www.mouser.se/ProductDetail/Waveshare/ESP32-S3-RS485-CAN) · [AliExpress (official Waveshare store, check seller)](https://www.aliexpress.com/w/wholesale-waveshare-esp32-s3-rs485-can.html) |
| 2 | **USB‑C data cable** | Must carry data, not just charge (for the first flash) | 50–100 | Any (Kjell & Co, Clas Ohlson, Elgiganten) |
| 3 | **USB power supply, 5 V ≥ 1 A, CE marked** | Powers the gateway permanently. A branded phone charger is fine | 0–150 | [Kjell & Co](https://www.kjell.com/se/sok?query=usb-c%20laddare) or reuse |
| 4 | **Twisted-pair cable, 2-core (or 2x2), shielded preferred** | NIBE recommends **LiYY, EKKX** or similar. Length = pump terminal → enclosure (keep it short, typically 1–3 m) | 50–150 | Electrical wholesaler (Ahlsell, Elektroskandia, Solar via your electrician) |
| 5 | **Small insulated enclosure (IP-rated, plastic)** | ~100×70×40 mm, with cable glands. Mount it *outside* the pump | 50–120 | Electrokit, Kjell, Biltema |
| 6 | **Ferrules (0.25–0.5 mm²) + cable glands** | For the screw terminals. The electrician usually has these | 20–50 | Electrician / Biltema |

## Optional: monitoring and optimisation phase

| Item | Purpose | Approx. SEK | Link |
|---|---|---|---|
| **Zigbee coordinator**: Home Assistant Connect ZBT‑2 | Official HA dongle, ZHA/Z2M | 350–450 | [home-assistant.io/connect/zbt-2](https://www.home-assistant.io/connect/zbt-2/) |
| *or* SONOFF Zigbee 3.0 USB Dongle Plus (ZBDongle‑E/‑P) | Budget coordinator | 250–350 | [ITEAD](https://itead.cc/product/sonoff-zigbee-3-0-usb-dongle-plus/) · [Z2M page](https://www.zigbee2mqtt.io/devices/ZBDongle-E.html) |
| USB 2.0 extension cable 0.5–1 m | Keeps the dongle away from USB3/SSD interference | 50 | Any |
| **Room sensors**: SONOFF SNZB‑02D (LCD) | Temperature/humidity per room | 150–200 each | [Z2M SNZB‑02D](https://www.zigbee2mqtt.io/devices/SNZB-02D.html) |
| *or* Aqara Temperature & Humidity Sensor (WSDCGQ11LM) | Small, reliable | 150–250 each | [Aqara](https://www.aqara.com/eu/product/temperature-humidity-sensor/) · [Z2M](https://www.zigbee2mqtt.io/devices/WSDCGQ11LM.html) |
| FAT32 USB stick (≤ 32 GB) | Loading LOG.SET / NIBE software update | 50–100 | Any |
| Energy meter / P1 reader (HAN port) | Whole-house kWh for the energy dashboard | 300–600 | e.g. [Home Assistant Glow](https://github.com/klaasnicolaas/home-assistant-glow) (DIY, LED pulse) or a HAN/P1 reader for your grid operator's meter |

## Not needed for this project

- RS‑485 termination resistor (leave the onboard jumper open)
- 12 V power supply (do not use the pump's X4:12)
- CAN wiring (the CAN port is unused)

## Budget summary

| Phase | Min | Max |
|---|---|---|
| Core gateway | ~390 | ~690 |
| Zigbee + 4 room sensors | ~850 | ~1 250 |
| Electrician (1 visit, typical) | not estimated: get a quote | |
