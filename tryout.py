import asyncio
import random


def run_async():
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

    asyncio.run(async_mytasks())


def call_worker():
    import requests

    print("call worker")
    rs = f"http://172.17.0.2:8080/1"
    print(f"sending {rs}")
    r = requests.get(rs)
    r1 = r.json()["result"]
    print(f"result for {rs}: {r.reason} {r1}")


def main():
    # run_async()
    call_worker()


if __name__ == '__main__':
    main()
