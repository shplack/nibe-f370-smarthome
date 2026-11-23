# 5. Enable MODBUS 40 in the pump

1. In the main menu, hold **Back** for **7 seconds**. This opens the service menu (menu 5).
2. Go to **5.2 System settings** and tick **MODBUS 40**. Confirm.
3. Leave the service menu.

## What you should see within a minute

| Sign | Meaning |
|---|---|
| Waveshare RS‑485 LED **blue** blinking | Telegrams from the pump |
| Waveshare RS‑485 LED **green** blinking | The gateway answering (acknowledge) |
| **No** communication alarm on the display | The pump accepts the "MODBUS 40" |
| Gateway log shows traffic for MODBUS40 | Firmware is decoding frames |

## Confirm model and software version

From the PC listed as `dev_ip`:

```bash
pip install nibe
python tools/verify_gateway.py --gateway <gateway-ip>
```

Expected output:

```
Product: F370  software version: NNNN
40004 BT1 Outdoor Temperature = ...
```

Record the **software version** in [Project status](../status.md). This closes compatibility question 4. If it is **≤ 5539**, plan a NIBE software update (see [Compatibility](../compatibility.md#check-1-main-software-version)).

## If a communication alarm appears

1. Untick MODBUS 40 in 5.2. The alarm should clear (or acknowledge it).
2. Check the gateway log: is it powered, on Wi-Fi, and has it booted without errors?
3. Check A/B polarity (electrician, pump isolated).
4. See [Troubleshooting](../usage/troubleshooting.md).

## Gate D

- [ ] No alarms for 24 h with MODBUS 40 enabled
- [ ] Product message reports `F370` and a software version
