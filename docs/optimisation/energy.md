# Energy dashboard

The F-series keeps no electricity counter unless an energy meter accessory (EME/BE current sensors) is fitted. Options:

1. **Whole-house meter:** a HAN/P1 reader on the grid operator's meter, or [Home Assistant Glow](https://github.com/klaasnicolaas/home-assistant-glow) (LED pulse). Add it as *Grid consumption* in **Settings → Dashboards → Energy**.
2. **Electric addition estimate:** integrate `Int. el.add. Power` (kW) with the [Integral](https://www.home-assistant.io/integrations/integration/) helper. This gives kWh for the immersion heater. Use it to see what optimisation costs or saves.
3. **Heat pump estimate:** Nibe Local Easyconf can derive a COP-like statistic for the F-series. See its README section *counting what the F-series does not measure*.
4. **Dedicated meter:** a DIN-rail kWh meter in the heat pump's supply (electrician), read over Modbus/pulse. This gives the most accurate heat pump consumption.

Add [Utility meter](https://www.home-assistant.io/integrations/utility_meter/) helpers for daily/monthly totals, and link the Nord Pool price sensor as the cost entity in the energy dashboard.
