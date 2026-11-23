# Sources

Checked on 2026-11-23. Version-specific facts are pinned in [Installation overview](installation/index.md#pinned-upstream-versions).

## Hardware

- Waveshare ESP32-S3-RS485-CAN: product page (isolated RS‑485/CAN, 7–36 V input, USB‑C, TVS, USD 18.99–19.99): <https://www.waveshare.com/esp32-s3-rs485-can.htm>
- Waveshare wiki (ESP32-S3R8, 16 MB flash, 120 Ω termination fitted via jumper, not connected by default): <https://www.waveshare.com/wiki/ESP32-S3-RS485-CAN>
- Mouser listing: <https://www.mouser.se/ProductDetail/Waveshare/ESP32-S3-RS485-CAN>

## NIBE

- NIBE MODBUS 40 installer manual IHB 1822‑10 (compatible products include F370; F370/F470/F730/F750 terminal diagram AA3‑X4:9‑12 = GND, B, A, 12V; 9600 8N1; software > 3000, ≥ 5539 for v10; menu 5.2; LiYY/EKKX cable; authorised electrician, unit unpowered): <https://professional.nibe.eu/document/Installer%20manual%20(IHB)/031725-10.pdf>
- NIBE FAQ LOG.SET (SE): <https://headless.nibe.eu/download/18.9a97aba184a9b5f272c5c/1669796068500/DOH%2014-262-36%20FAQ%20LogSet%201722-3.pdf>
- NIBE F370 product page: <https://www.nibe.eu/sv-se/produkter/varmepumpar/franluftsvarmepumpar/f370>
- NIBE serial-number format FAQ: <https://www.nibe.eu/sv-se/support/vanliga-fragor/faq-items/vad-betyder-siffrorna-i-serienumret-pa-en-nibe-produkt>
- myUplink: <https://myuplink.com>

## Software

- beolink/Nibe-F-series-ModbusAdapter (gateway YAML, wiring, LOG.SET generator): <https://github.com/beolink/Nibe-F-series-ModbusAdapter>
- LOG.SET documentation: <https://github.com/beolink/Nibe-F-series-ModbusAdapter/blob/main/docs/logset.md>
- beolink/HA-Nibe-Easyconf (Home Assistant integration): <https://github.com/beolink/HA-Nibe-Easyconf>
- elupus/esphome-nibe (`nibegw` ESPHome component): <https://github.com/elupus/esphome-nibe>
- yozik04/nibe (Python library, register maps): <https://github.com/yozik04/nibe>
- Home Assistant core NIBE integration (NibeGW): <https://www.home-assistant.io/integrations/nibe_heatpump/>
- Telegram timing discussion: <https://github.com/elupus/esphome-nibe/issues/56>
- LOG.SET capture: <https://github.com/yozik04/nibe-mqtt/issues/15>
- Independent LOG.SET generator: <https://github.com/per42/nibe-log-set>
- ESPHome install: <https://esphome.io/guides/installing_esphome/> · Web flasher: <https://web.esphome.io/>
- ESPHome Device Builder add-on: <https://github.com/esphome/home-assistant-addon>
- HACS: <https://hacs.xyz/docs/use/>

## Home Assistant

- Installation types: <https://www.home-assistant.io/installation/>
- Nord Pool: <https://www.home-assistant.io/integrations/nordpool/> · HACS alternative: <https://github.com/custom-components/nordpool>
- ZHA: <https://www.home-assistant.io/integrations/zha/> · Zigbee2MQTT: <https://www.zigbee2mqtt.io/>
- Connect ZBT‑2: <https://www.home-assistant.io/connect/zbt-2/>
- SONOFF dongle: <https://itead.cc/product/sonoff-zigbee-3-0-usb-dongle-plus/> · SNZB‑02D: <https://www.zigbee2mqtt.io/devices/SNZB-02D.html>
- Aqara sensor: <https://www.aqara.com/eu/product/temperature-humidity-sensor/>
- Packages: <https://www.home-assistant.io/docs/configuration/packages/>
- Template: <https://www.home-assistant.io/integrations/template/> · Integral: <https://www.home-assistant.io/integrations/integration/> · Utility meter: <https://www.home-assistant.io/integrations/utility_meter/>
- Forecast.Solar: <https://www.home-assistant.io/integrations/forecast_solar/>
- Home Assistant Glow: <https://github.com/klaasnicolaas/home-assistant-glow> · battery_sim: <https://github.com/hif2k1/battery_sim>

## GitHub Pages

- Publishing source (GitHub Actions): <https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site>
- Actions: <https://github.com/actions/upload-pages-artifact>, <https://github.com/actions/deploy-pages>, <https://github.com/actions/configure-pages>
- MkDocs Material: <https://squidfunk.github.io/mkdocs-material/publishing-your-site/>
- Link checker: <https://github.com/lycheeverse/lychee-action>
