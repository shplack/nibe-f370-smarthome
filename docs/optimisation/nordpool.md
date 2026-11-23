# Nord Pool electricity prices (Sweden)

## Option A: core Nord Pool integration (recommended)

Home Assistant has included a **Nord Pool** integration since **2024.12**. It is local configuration and uses Nord Pool's public data.

1. **Settings → Devices & services → Add integration → Nord Pool**.
2. Choose your area: **SE1** (Luleå), **SE2** (Sundsvall), **SE3** (Stockholm) or **SE4** (Malmö). Your grid operator's invoice shows the area.
3. Currency **SEK**.

It provides current price and daily statistics sensors, plus a `nordpool.get_prices_for_date` action that returns 15-minute/hourly prices for today and tomorrow (tomorrow's prices are published around 13:00 CET).

Docs: <https://www.home-assistant.io/integrations/nordpool/>

## Option B: HACS `custom-components/nordpool`

The long-standing community integration. It exposes `today`/`tomorrow` attributes and lets you add VAT, energy tax and network fees in a template. Many community price-control blueprints expect it.

<https://github.com/custom-components/nordpool>

## Price level helper

The optimisation package defines `sensor.nibe_price_level` with three states: `cheap`, `normal` and `expensive`. It compares the current price with today's average:

- `cheap`: price ≤ 80 % of today's average **or** ≤ 0.30 SEK/kWh
- `expensive`: price ≥ 130 % of today's average **and** ≥ 1.00 SEK/kWh
- otherwise `normal`

Hysteresis: the heating automation only acts when the level is unchanged for 15 minutes.

Set the current price entity in the package (`sensor.nord_pool_se3_current_price` by default) and tune the thresholds in `input_number` helpers.

## Your real price

The spot price is only part of what you pay. Add *energiskatt* (energy tax), VAT, the supplier markup and the grid fee (*elnät*, possibly time-of-use or *effektavgift*). If your grid operator charges a **power tariff**, avoid stacking hot water + electric addition in the peak hours. Treat that as a constraint in the automations.
