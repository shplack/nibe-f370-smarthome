# NIBE F370 Local Smart Home

Use Home Assistant to monitor and later optimise a **NIBE F370** exhaust-air heat pump. Everything runs locally with open-source software and a DIY ESP32 RS‑485 gateway. You do **not** need NIBE's MODBUS 40 accessory, myUplink or a cloud account.

!!! danger "Mains voltage"
    The F370 is a 3x400V appliance. Any work inside the cabinet, including the low-voltage RS‑485 pair, must be done by a **qualified electrician with the pump isolated**. Read [Safety](safety.md) first.

## What you get

- **Read-only monitoring first:** outdoor (BT1), supply (BT2), return (BT3), hot water (BT6/BT7), exhaust and extract air (BT20/BT21), compressor state, electric additional heat, priority, alarms.
- **Then optimisation:** Nord Pool (SE1–SE4) price-aware heating and hot water, Zigbee room sensors, humidity-driven ventilation, solar/battery hooks and an energy dashboard. All of it stays **disabled until the readings are verified**.
- **NIBE stays in charge** of frost protection, compressor protection, alarms and minimum ventilation. Home Assistant only changes comfort setpoints and offsets.

## Architecture

```
┌──────────────── NIBE F370 ───────────────┐      ┌── Waveshare ESP32-S3-RS485-CAN ──┐      ┌──── Home Assistant ─────┐
│ EB100 controller                         │      │ ESPHome + esphome-nibe (nibegw) │      │ Nibe Local Easyconf     │
│ AA3-X4:11 (A) ───────────────────────────┼─────►│ RS485 A+   isolated transceiver │ UDP  │  (HACS custom repo)     │
│ AA3-X4:10 (B) ───────────────────────────┼─────►│ RS485 B-   emulates MODBUS 40   │─────►│ Nord Pool, Zigbee,      │
│ AA3-X4:9  GND   (left unconnected)       │      │ powered by USB-C 5 V            │ 9999 │ automations, dashboard  │
│ Menu 5.2: MODBUS 40 = on                 │      │                                 │10000 │                         │
└──────────────────────────────────────────┘      └─────────────────────────────────┘      └─────────────────────────┘
```

## Where to start

1. [Project status](status.md): the open questions to answer before buying or wiring.
2. [Technical write-up](technical.md): how the bus, the gateway and the integration work.
3. [Compatibility checks](compatibility.md): what has been verified for the F370 and what has not.
4. [Shopping list](shopping-list.md): about 390–690 SEK.
5. [Installation](installation/index.md): eight gated steps. Do not skip the gates.

!!! info "Not affiliated with NIBE"
    This is a community project. It does not change any NIBE safety function. Using a third-party device on the accessory bus is at your own risk, and could matter for warranty or service discussions with your installer.
