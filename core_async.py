import asyncio
import time

import aiohttp


async def do_works(n: int):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(do_work(cnt, session)) for cnt in range(n)]
        await asyncio.wait(tasks)
        print("finished all")


async def do_work(cnt, session):
    rs = f"http://172.17.0.2:8080/{cnt}"
    print(f"sending {rs}")
    async with session.get(rs) as resp:
        reason = resp.reason
        r = await resp.json()
        print(f"result for {rs}: {reason} {r}")


def main():
    n = 10
    start = time.time()
    asyncio.run(do_works(n))
    stop = time.time()
    dur = stop - start
    dur1 = float(dur) / n
    print(f"took {dur:.2f} seconds for {n} calls")
    print(f"took {dur1:.2f} seconds for 1 call")


if __name__ == '__main__':
    main()
