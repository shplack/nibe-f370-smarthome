# Ventilation and humidity

The F370 is an **exhaust-air** heat pump. Ventilation is both its heat source and the house's required air exchange (BBR in Sweden requires ≥ 0.35 l/s·m²).

## Do

- Use **Fan Mode** (47260) 1–4 as a *temporary* boost when bathroom humidity rises fast (showers). NIBE returns to normal after the configured *fan return time* (47271–47274).
- Trigger: bathroom humidity rises ≥ 8 %RH in 10 min, or exceeds 75 %RH. End: back below 60 %RH, or after 60 min, then set *Normal*.

## Don't

- Don't lower **Exhaust fan speed normal** (47265) below the commissioned value. That reduces air exchange and compressor capacity, and can cause moisture problems.
- Don't stop ventilation to "save energy". Without exhaust air the F370 cannot run its compressor and falls back on electric heating.

## Monitor

- BT20 exhaust air and BT21 vented air. A small difference with the compressor running can point to a **dirty filter** or a frozen evaporator.
- Filter reminder: NIBE handles it (47275).
