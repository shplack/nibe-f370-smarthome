# Firmware

This project does **not** fork the gateway firmware. It uses the upstream
ESPHome configuration unchanged:

- <https://github.com/beolink/Nibe-F-series-ModbusAdapter/blob/main/esphome/nibe-gw.yaml>
- reviewed at commit `01f8f22314367ec8005ea21d12f5b5075e6cbbf0`

```bash
./firmware/fetch-upstream.sh          # pinned commit, creates secrets.yaml
./firmware/fetch-upstream.sh --latest # upstream main
esphome run firmware/upstream/esphome/nibe-gw.yaml
```

`firmware/upstream/` and every `secrets.yaml` are git-ignored, so Wi-Fi
credentials and the pump's serial number are never committed.

The only F370-specific value is `device_friendly_name: "NIBE F370"`.
Everything else (GPIO17 TX, GPIO18 RX, GPIO21 direction, 9600 baud, UDP 9999/10000,
MODBUS40 acknowledge + version constant) is identical for every F-series model.
