# Room sensors (Zigbee)

## Coordinator

| Option | Notes |
|---|---|
| **Home Assistant Connect ZBT‑2** | Official, works with ZHA out of the box |
| SONOFF ZBDongle‑E / ‑P | Cheap. Supported by ZHA and Zigbee2MQTT |

Use a **USB extension cable** and keep the dongle away from USB 3 ports, SSDs and the Wi-Fi router.

## ZHA or Zigbee2MQTT?

- **ZHA** (built in): simplest. Pick it unless you have a reason not to. <https://www.home-assistant.io/integrations/zha/>
- **Zigbee2MQTT**: wider device support and more detail, but needs an MQTT broker (Mosquitto add-on) and the Z2M add-on/container. <https://www.zigbee2mqtt.io/>

## Sensors

- SONOFF **SNZB‑02D** (LCD display, temperature + humidity)
- Aqara **WSDCGQ11LM** (temperature + humidity + pressure)

Put one in every main room, plus one in the bathroom for humidity. Mount them 1.5 m high, away from radiators, sunlight and outside walls.

## Use in this project

1. **Monitoring:** a template `sensor.house_mean_temperature` (average of living spaces) in `nibe_f370_optimisation.yaml`.
2. **Comfort guard:** price set-back is blocked if the mean temperature is below `input_number.nibe_min_comfort_temp` (default 20.5 °C).
3. **Optional BT50 emulation:** Nibe Local Easyconf offers a climate entity that can feed an external room temperature to the pump (room sensor factor). It is powerful but changes how the curve behaves. Try it only after the offset strategy works, and read the integration's README first.
