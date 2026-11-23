# 3. Bench test (before the electrician visits)

Power the board from USB‑C on your desk. **Nothing is connected to the RS‑485 terminal.**

## Checks

1. **Wi-Fi:** the router shows a client named `nibe-…-gw`. Its log shows `WiFi Connected` and an IP. Give it a DHCP reservation too.
2. **Logs:** `esphome logs esphome/nibe-gw.yaml` (CLI) or **Logs** in the Device Builder. Expect boot messages, `nibegw` set-up, and no crash loop.
3. **mDNS:** `ping nibe-<serial>-gw.local` resolves (macOS/Linux; on Windows use the IP).
4. **OTA:** run `esphome run esphome/nibe-gw.yaml` again and pick the network address. It should update over Wi-Fi. You will use this route later, when the board sits in its enclosure.
5. **Fallback AP:** optional. Turn off your Wi-Fi briefly and check that the board opens `NIBE F370 Fallback`.
6. **Signal at the pump:** carry the board (with a power bank) to where the enclosure will hang. Check the `Wi-Fi signal` sensor in the log. It should be better than −75 dBm.

With no bus connected the gateway sees no telegrams. That is expected.

## Optional: integration dry run

In Home Assistant you can already add the HACS integration ([step 6](06-home-assistant.md)). Setup will fail to find a product message. That proves only that the gateway answers on the network. Remove the entry again.

## Gate B

- [ ] Stable on Wi-Fi for 24 h without reboots (`Uptime` keeps increasing)
- [ ] OTA update works
- [ ] Signal at the installation spot is acceptable
