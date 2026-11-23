# 6. Home Assistant integration (read-only)

!!! note "Repository name"
    The integration formerly referred to as `beolink/nibe-local` is published as **`beolink/HA-Nibe-Easyconf`** (domain `nibe_local_easyconf`). The old URL returns 404.

## Install

1. **HACS → ⋮ → Custom repositories**, add `https://github.com/beolink/HA-Nibe-Easyconf` as type **Integration**.
2. Search for **Nibe Local Easyconf**, then click **Download**.
3. **Restart Home Assistant** (Settings → System → Restart).
4. Requirement: Home Assistant **2025.2 or newer**.

## Add the pump

- The gateway is usually **discovered** through mDNS. Look for *Discovered* in *Settings → Devices & services* and click **Add**.
- Otherwise: **Add integration → Nibe Local Easyconf → F-series through a NibeGW gateway**, then enter the gateway's IP.

The integration reads the product message (model `F370` + software version). Then it reads its default registers, which takes under a minute, and enables those that report values.

!!! warning "Allowed sources"
    If setup times out, check that Home Assistant's IP equals `ha_ip` in the gateway's `secrets.yaml`. The gateway log says so when it drops a request.

## Keep it read-only for now

The integration also creates write entities (numbers/selects/switches for offsets, hot water mode, fan mode…). Until Gate E has passed:

1. Open the device page, then each **Configuration/Controls** entity, and **disable** it. Or simply do not use them.
2. Do **not** create automations that call `number.set_value` / `select.select_option` on NIBE entities.
3. Optional: install the read-only helper package from this repository (`homeassistant/packages/nibe_f370_monitoring.yaml`). See [Monitoring](../usage/monitoring.md).

## Verify the values

Compare HA with the display over a few days:

| HA entity (approx. name) | Display location |
|---|---|
| BT1 Outdoor temperature | Menu 3.1 / home screen |
| BT2 Supply temp S1 | Menu 3.1 |
| BT3 Return temp | Menu 3.1 |
| BT6 HW load / BT7 HW top | Menu 3.1 / hot water info |
| BT20 Exhaust / BT21 Vented air | Menu 3.1 |
| Compressor state, Priority | Menu 3.1 *status*, home screen |
| Int. el. add. power | Menu 3.1 |
| Alarm | Display alarm indicator |

## Gate E

- [ ] Values match the display within sensor resolution for 7 days
- [ ] No pump alarms, no gateway reboots
- [ ] Integration shows no repeated timeouts in *Settings → System → Logs*
