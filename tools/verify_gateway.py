#!/usr/bin/env python3
"""Read-only check of a NibeGW gateway on a NIBE F370.

Waits for the pump's product message (model + MAIN software version) and then
reads a few registers. It never writes anything.

Run it from the machine whose IP is listed as `dev_ip` (or `ha_ip`) in the
gateway's secrets.yaml. Stop Home Assistant's integration first if it runs on
the same host: both would want local UDP port 9999.

    pip install nibe
    python tools/verify_gateway.py --gateway 192.168.1.50
    python tools/verify_gateway.py --gateway 192.168.1.50 --read 43005   # try degree minutes
"""

from __future__ import annotations

import argparse
import asyncio
import sys

from nibe.coil import Coil
from nibe.connection.nibegw import NibeGW
from nibe.exceptions import NibeException
from nibe.heatpump import HeatPump, Model

DEFAULT_REGISTERS = [40004, 40008, 40012, 40013, 40014, 40025, 40026, 43009, 43427, 43086, 45001, 43001]
MIN_SOFTWARE_FOR_V10 = 5539
MIN_SOFTWARE = 3000


async def main(args: argparse.Namespace) -> int:
    heatpump = HeatPump(Model.F370)
    await heatpump.initialize()
    conn = NibeGW(
        heatpump,
        remote_ip=args.gateway,
        remote_read_port=args.read_port,
        remote_write_port=args.write_port,
        listening_port=args.listen_port,
    )
    await conn.start()
    rc = 0
    try:
        print(f"Waiting up to 20 s for the product message from {args.gateway} ...")
        try:
            info = await conn.read_product_info()
            print(f"Product: {info.model}  software version: {info.firmware_version}")
            if "F370" not in info.model.upper():
                print("WARNING: pump does not identify as F370", file=sys.stderr)
                rc = 1
            if info.firmware_version <= MIN_SOFTWARE:
                print(f"WARNING: software <= {MIN_SOFTWARE}: NIBE says MODBUS 40 needs an update", file=sys.stderr)
                rc = 1
            elif info.firmware_version < MIN_SOFTWARE_FOR_V10:
                print(f"NOTE: software < {MIN_SOFTWARE_FOR_V10}: MODBUS 40 v10 features may not work; consider updating")
        except NibeException as exc:
            print(f"No product message: {exc}", file=sys.stderr)
            print("Check: MODBUS 40 enabled in 5.2? this host's IP in the gateway allow-list? wiring?", file=sys.stderr)
            return 2

        for address in args.read or DEFAULT_REGISTERS:
            try:
                coil = heatpump.get_coil_by_address(address)
            except NibeException:
                # Not in the published F370 map (e.g. 43005 degree minutes): probe it as raw s16.
                coil = Coil(address, f"unmapped-{address}", f"Unmapped {address} (raw s16)", "s16", 1)
            try:
                data = await conn.read_coil(coil)
                unit = coil.unit or ""
                print(f"{address:>5} {coil.title:<40} = {data.value} {unit}")
            except NibeException as exc:
                print(f"{address:>5} {coil.title:<40} : read failed ({exc})")
                rc = 1
    finally:
        await conn.stop()
    return rc


def parse() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--gateway", required=True, help="IP or hostname of the ESP32 gateway")
    p.add_argument("--read", type=int, nargs="*", help="register addresses to read (default: core set)")
    p.add_argument("--read-port", type=int, default=9999)
    p.add_argument("--write-port", type=int, default=10000)
    p.add_argument("--listen-port", type=int, default=9999, help="local UDP port the gateway sends to")
    return p.parse_args()


if __name__ == "__main__":
    sys.exit(asyncio.run(main(parse())))
