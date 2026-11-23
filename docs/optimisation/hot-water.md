# Hot water optimisation

The F370 has a built-in ~180 l water heater. Hot water is a good thermal store: heat it in cheap hours and coast through expensive ones.

**Levers**

- Hot water comfort mode (47041): Economy / Normal / Luxury / Smart Control
- Temporary Lux (48132): 3h / 6h / 12h / one-time increase

## Strategy

| Time | Action |
|---|---|
| Cheapest 2–3 h of the night (or the solar surplus window) | `Temporary Lux = One-time increase` |
| Expensive hours | Comfort mode = **Economy** |
| Otherwise | Comfort mode = **Normal** |

Guards:

- Never stay in Economy if **BT7 HW top < 40 °C** during waking hours.
- Do not touch periodic hot water (legionella). NIBE manages it.
- Avoid Lux when NIBE is already in *Prio: Heat* on a cold day with electric addition running.
- If your grid operator has a power tariff, avoid starting Lux in the peak window.
