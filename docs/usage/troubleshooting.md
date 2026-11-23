# Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Communication alarm right after enabling MODBUS 40 | Gateway off/rebooting, A/B swapped, wrong terminals | Untick MODBUS 40. Check the gateway log. Have the electrician check polarity |
| Blue LED blinks, green does not | Gateway receives but does not answer: wrong `dir_pin`, firmware not running `nibegw` | Re-flash the unmodified upstream YAML |
| No LEDs at all | No telegrams: MODBUS 40 not enabled, broken wire | Check menu 5.2. Electrician checks the wiring |
| HA setup times out | HA IP not in `ha_ip`/`dev_ip`; Docker without host networking; firewall blocks UDP 9999/10000 | Fix `secrets.yaml` and re-flash OTA; use `network_mode: host` |
| Gateway reboots every 15 min | `api.reboot_timeout` changed back from 0s | Restore upstream value |
| Values stop now and then | Wi-Fi power save on, weak signal | Keep `power_save_mode: none`; move the enclosure / add an AP |
| 32-bit counters show garbage | Known upstream issue in pushes | Keep 32-bit registers out of LOG.SET |
| Pushed values stop after a power cut | LOG.SET selection lost (unverified) | Reload LOG.SET |
| Pump shows a strange accessory/version | MODBUS 40 v10 emulation | Expected |
| Product message says something other than F370 | Model detection issue | Report upstream with the log |

## Collecting logs

- Gateway: `esphome logs esphome/nibe-gw.yaml`
- Home Assistant: in `configuration.yaml`

```yaml
logger:
  default: warning
  logs:
    custom_components.nibe_local_easyconf: debug
    nibe: debug
```

- Diagnostics: device page → ⋮ → *Download diagnostics* (check for the serial number before posting publicly).

## Rolling back

1. Untick MODBUS 40 in menu 5.2. The pump is then exactly as before.
2. Optional: ask the electrician to remove the pair (pump isolated).
