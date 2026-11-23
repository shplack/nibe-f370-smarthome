# Technical write-up

## 1. The problem

NIBE's F-series (F370, F470, F730, F750, F1145–F1355, SMO, VVM) has **no Modbus TCP** and no open local API. NIBE's own route is the **MODBUS 40** accessory. It sits on the pump's internal RS‑485 *accessory bus* and turns it into a standard Modbus RTU slave. The newer S-series has Modbus TCP built in. This project replaces MODBUS 40 with a ~200 SEK ESP32 board.

## 2. The accessory bus

| Property | Value | Source |
|---|---|---|
| Physical layer | RS‑485, 2-wire (A/B), half duplex | NIBE MODBUS 40 IHB, *Connecting communication* |
| Pump terminal (F370) | AA3‑X4: 9 = GND, 10 = B, 11 = A, 12 = 12 V | NIBE MODBUS 40 IHB, F370/F470/F730/F750 diagram |
| Speed | 9600 baud, 8N1 | NIBE MODBUS 40 IHB; esphome-nibe |
| Cable | LiYY, EKKX or similar (twisted pair) | NIBE MODBUS 40 IHB |
| Role of the pump | **Bus master**. It polls each accessory address in turn | esphome-nibe / nibe library |

The pump sends telegrams to the "MODBUS 40" address. A real MODBUS 40 must acknowledge each one within a few milliseconds. If no accessory answers after MODBUS 40 is enabled in menu 5.2, the pump raises a communication alarm.

The NIBE proprietary framing (start byte `0x5C`, address, command, length, payload, XOR checksum) carries these commands:

- **Data/LOG telegrams**: the pump pushes up to 20 register values that a `LOG.SET` file selects.
- **Read request/response**: one register per request, answered on the pump's next poll. It takes about 1 s per register.
- **Write request/response**: one register per request.
- **Product info**: every ~15 s the pump announces its model string (e.g. `F370`) and **main software version**.
- **Accessory version request**: the gateway answers as a *MODBUS 40 v10* (`[0x0A, 0x00, 0x01]`).

## 3. The gateway

**Hardware:** Waveshare ESP32-S3-RS485-CAN

| Feature | Why it matters |
|---|---|
| ESP32-S3R8, 16 MB flash, Wi-Fi | Runs ESPHome comfortably |
| **Galvanically isolated** RS‑485 (digital isolator + isolated DC‑DC) | Breaks ground loops between pump and house network. This is why X4:9 GND stays open |
| SP3485 transceiver, TVS/ESD protection | Robust bus interface |
| 120 Ω termination **not fitted by default** (enabled by jumper) | The pump bus is short. Leave termination off, as upstream specifies |
| USB-C power/programming, or 7–36 V DC screw terminal | USB-C power keeps it independent of the pump's 12 V |

Pin mapping (from Waveshare's schematic, as documented upstream):

| ESP32-S3 | Signal | Function |
|---|---|---|
| GPIO17 | TXD1 → isolator → SP3485 DI | UART TX |
| GPIO18 | RXD1 ← isolator ← SP3485 RO | UART RX |
| GPIO21 | RS485_EN → SP3485 DE + /RE | Direction (high = transmit) |

**Firmware:** ESPHome with the external component [`elupus/esphome-nibe`](https://github.com/elupus/esphome-nibe) (`nibegw`). The upstream config `esphome/nibe-gw.yaml`:

- **acknowledges** MODBUS 40 telegrams locally, so the pump stays happy when Home Assistant restarts;
- **forwards** every telegram over UDP to allowed hosts (`ha_ip`, `dev_ip`) that sent a request in the last 2 minutes;
- receives **read** requests on UDP 9999 and **write** requests on UDP 10000;
- sets `power_save_mode: none` (Wi-Fi power save drops UDP) and `api.reboot_timeout: 0s` (the integration uses UDP, not the ESPHome API);
- decodes nothing. Decoding happens in Home Assistant.

## 4. Home Assistant side

[`beolink/HA-Nibe-Easyconf`](https://github.com/beolink/HA-Nibe-Easyconf) (HACS custom repository, domain `nibe_local_easyconf`, v1.15.4 reviewed) uses the [`nibe`](https://github.com/yozik04/nibe) library's `NibeGW` connection:

- discovers the gateway by mDNS (`_esphomelib._tcp`, name `nibe-*`) or DHCP;
- reads the **product message**, so there is no model to pick. The device page shows the pump's model and software version;
- reads only the default register set at setup. The rest of the 489-register F370 map becomes **disabled** entities;
- polls by priority: measurements every cycle, counters every 5th, settings every 10th. With ~1.1 s per read, the default one-minute cycle fits about 40 reads;
- **never polls registers that arrive via LOG.SET**.

Alternative: Home Assistant's core [`nibe_heatpump`](https://www.home-assistant.io/integrations/nibe_heatpump/) integration also supports NibeGW with the same ports. It works with this gateway too, but you have to pick the model and you get fewer F-series niceties.

## 5. LOG.SET

`LOG.SET` is a text file. You load it once from a USB stick in the display's USB menu. It tells the pump to push up to 20 registers (a 32-bit register takes 2 slots) about every 2.1 s. This makes the important values near real-time and frees the slow read channel. See [Install step 7](installation/07-logset.md).

## 6. Control philosophy

The F370 calculates its supply setpoint from the outdoor temperature and the heating curve (curve + offset, menu 1.9.1). It runs a degree-minute integral and decides about compressor and electric addition itself. Safe external levers, in order of preference:

1. **Heat offset S1** (register 47011, −10…+10) moves the curve. This is the main price lever.
2. **Hot water comfort mode** (47041: Economy/Normal/Luxury/Smart Control) and **Temporary Lux** (48132).
3. **Fan mode** (47260: Normal/1–4) for temporary forced ventilation. NIBE returns to normal after the set return time.
4. **External room temperature** (BT50 emulation, through the integration's climate entity). Only if you want room-temperature feedback.

Things this project will **not** touch: max/min supply limits for safety, compressor start/stop logic, frost protection, alarm reset automation, exhaust fan below NIBE's minimum airflow.

## 7. Limits and risks

- F370 support is **documented but not measured** upstream. Measurements were made on an F1255.
- The F370 map has **no degree-minute register** in the `nibe` library (see [Compatibility](compatibility.md#check-5-degree-minutes)).
- 32-bit values pushed by LOG.SET have been seen arriving corrupted on some firmware versions, so the provided LOG.SET files use only 16-bit registers.
- Writes change real heat pump settings and are stored in the controller's memory. Frequent writes (e.g. every 5 minutes for months) are not tested for flash wear. Change values hourly at most.
