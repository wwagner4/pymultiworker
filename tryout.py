import asyncio
import logging
import random
import sys
from time import sleep


def run_async():
    async def mytask(tid: str):
        n = random.randint(1, 3)
        for i in range(n):
            logging.info(f"task {tid} {i} of {n}")
            await asyncio.sleep(1)
        logging.info(f"finished {tid} {n}")

    async def async_mytasks():
        ids = [f"t-{i}" for i in range(100)]
        ts = [asyncio.create_task(mytask(tid)) for tid in ids]
        await asyncio.wait(ts)
        logging.info("all finished")

    asyncio.run(async_mytasks())


def call_worker():
    import requests

    logging.info("call worker")
    rs = f"http://172.17.0.2:8080/1"
    logging.info(f"sending {rs}")
    r = requests.get(rs)
    r1 = r.json()["result"]
    logging.info(f"result for {rs}: {r.reason} {r1}")


def run_concurrent():
    from concurrent.futures import ThreadPoolExecutor

    def square(n):
        print(f"Started square({n})")
        st = 0.5 + random.random() * 2
        sleep(st)
        print(f"Almost finished square({n})")
        return n * n

    values = range(20)
    with ThreadPoolExecutor(max_workers=15) as executor:
        results = executor.map(square, values)

    print(list(results))


def main():
    # run_async()
    # call_worker()
    run_concurrent()


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level='INFO')
    main()
