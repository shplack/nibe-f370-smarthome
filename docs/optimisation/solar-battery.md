# Solar and battery (if available)

## Solar

- Bring the inverter into Home Assistant locally (e.g. SolarEdge/Fronius/Huawei/SMA Modbus integrations) **or** use a forecast such as [Forecast.Solar](https://www.home-assistant.io/integrations/forecast_solar/).
- When **export > 1.5 kW for 10 min**: start `Temporary Lux` (hot water), then raise heat offset +1 (bounded, same rules as [Heating](heating.md)).
- Alternative: NIBE **SG Ready** (48282/48284 registers, or the physical AUX inputs). It tells the pump "cheap energy available". Physical SG Ready needs relay wiring by the electrician, so the register route via the gateway is preferred here.

## Battery

- Avoid charging the battery from the grid at the same time as the heat pump's Lux/pre-heat in a cheap window if your grid operator has a **power tariff**.
- Priority suggestion: house load → hot water (cheapest storage) → battery → export.

## Simulation

If you're considering a battery, [`battery_sim`](https://github.com/hif2k1/battery_sim) simulates it against your real HA energy data.
