# NIBE F370 Local Smart Home Integration

A DIY, local-only, open-source integration of a **NIBE F370** exhaust-air heat
pump with **Home Assistant**. It uses a ~200 SEK ESP32 RS‑485 gateway instead of
NIBE's MODBUS 40 accessory. Built for a Swedish installation (SE, CU 3x400V,
EB100 controller) with Nord Pool price optimisation.

📖 **Documentation site:** published to GitHub Pages from [`docs/`](docs/)
(see [Publishing](#publishing-the-site)).

> [!WARNING]
> The F370 contains hazardous mains voltage. Opening the pump, wiring the
> RS‑485 pair, and routing the cable are jobs for a **qualified electrician
> with the pump isolated**. Nothing in this repository changes that.

## How it fits together

```
NIBE F370 (EB100)                ESP32-S3-RS485-CAN                 Home Assistant
AA3-X4:11 (A) ──── twisted ────► RS485 A+   (isolated)  ── Wi-Fi ──► Nibe Local Easyconf
AA3-X4:10 (B) ──── pair    ────► RS485 B-               UDP 9999/10000   (HACS)
AA3-X4:9  GND  (not connected)    ESPHome + esphome-nibe "nibegw"       Nord Pool, Zigbee, ...
                                  emulates MODBUS 40 v10
```

## Repository layout

| Path | Contents |
|---|---|
| [`docs/`](docs/) | The documentation site (MkDocs Material): technical write‑up, shopping list, installation, usage, optimisation, sources |
| [`firmware/`](firmware/) | Pinned fetch script and notes for the upstream ESPHome gateway configuration |
| [`logset/`](logset/) | Pre‑generated `LOG.SET` files for the F370 (default and extended selections) |
| [`homeassistant/`](homeassistant/) | Home Assistant packages: read‑only monitoring helpers and *disabled* price‑optimisation drafts |
| [`tools/`](tools/) | `verify_gateway.py`: read‑only bus test that prints the pump's model and **main software version** |
| [`.github/workflows/`](.github/workflows/) | Pages build/deploy on doc changes, PR build check, weekly link check |

## Quick start

1. Read [Pre‑installation compatibility checks](docs/compatibility.md) and
   answer the five open questions in [Project status](docs/status.md).
2. Buy the parts in the [shopping list](docs/shopping-list.md).
3. Follow [Installation](docs/installation/index.md) step by step.

## Upstream projects (do the real work)

- Gateway config: <https://github.com/beolink/Nibe-F-series-ModbusAdapter> (reviewed at `01f8f22`)
- HA integration: <https://github.com/beolink/HA-Nibe-Easyconf> (reviewed at v1.15.4, `3412eda`)
  — note: the older `beolink/nibe-local` URL returns 404; this is its current name.
- Firmware component: <https://github.com/elupus/esphome-nibe>
- Protocol library: <https://github.com/yozik04/nibe> (reviewed at 2.26.0)

## Publishing the site

1. Push this repository to GitHub (branch `main`).
2. **Settings → Pages → Build and deployment → Source: GitHub Actions.**
3. Edit `site_url`/`repo_url` in [`mkdocs.yml`](mkdocs.yml) to match your account.
4. Any push to `main` that touches `docs/`, `mkdocs.yml` or `requirements-docs.txt`
   rebuilds and redeploys the site automatically.

Local preview:

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements-docs.txt
mkdocs serve
```

## Licence

Documentation and scripts: MIT (see [LICENSE](LICENSE)). Upstream projects keep
their own licences (Apache‑2.0 for the ModbusAdapter; see each repository).
This project is not affiliated with or endorsed by NIBE.
