import asyncio
import logging
import os
import sys
import time

import aiohttp

e_host = os.getenv("HOST", "172.17.0.2")
e_port = int(os.getenv("PORT", "5000"))
e_loglevel = os.getenv("LOGLEVEL", "INFO")


async def do_works(n: int):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(do_work(str(call_id), session)) for call_id in range(n)]
        rs = await asyncio.wait(tasks)
        logging.info("finished all")
        for i, r in enumerate(rs[0]):
            logging.info(f"result {i} - {r.result()}")


# noinspection HttpUrlsUsage
async def do_work(call_id: str, session) -> dict:
    rs = f"http://{e_host}:{e_port}/{call_id}"
    logging.info(f"sending {rs}")
    async with session.get(rs) as resp:
        reason = resp.reason
        response_dict = await resp.json()
        logging.info(f"result for {rs}: {reason} {response_dict}")
        return response_dict


def run_work_block():
    n = 10
    start = time.time()
    asyncio.run(do_works(n))
    stop = time.time()
    dur = stop - start
    dur1 = float(dur) / n
    logging.info(f"took {dur:.2f} seconds for {n} calls")
    logging.info(f"took {dur1:.2f} seconds for 1 call")


def main():
    block_cnt = 1
    while True:
        run_work_block()
        logging.info(f"-- finished running work block {block_cnt} --------------------------------------")
        block_cnt += 1
        time.sleep(10)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=e_loglevel)
    main()
