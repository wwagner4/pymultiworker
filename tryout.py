import asyncio
import random


async def mytask(tid: str):
    n = random.randint(1, 3)
    for i in range(n):
        print(f"task {tid} {i} of {n}")
        await asyncio.sleep(1)
    print(f"finished {tid} {n}")


async def async_mytasks():
    ids = [f"t-{i}" for i in range(100)]
    ts = [asyncio.create_task(mytask(tid)) for tid in ids]
    await asyncio.wait(ts)
    print("all finished")


if __name__ == '__main__':
    asyncio.run(async_mytasks())
