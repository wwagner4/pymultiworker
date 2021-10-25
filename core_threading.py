import logging
import os
import sys
import time

import requests
from concurrent.futures import ThreadPoolExecutor

e_host = os.getenv("HOST", "localhost")
e_port = int(os.getenv("PORT", "5000"))
e_loglevel = os.getenv("LOGLEVEL", "INFO")
e_blocksize = int(os.getenv("BLOCKSIZE", "3"))


def do_works(n: int):
    ids = map(lambda i: str(i), range(n))
    with ThreadPoolExecutor(max_workers=e_blocksize) as executor:
        return executor.map(do_work, ids)


# noinspection HttpUrlsUsage
def do_work(call_id: str):
    rs = f"http://{e_host}:{e_port}/{call_id}"
    logging.info(f"sending {rs}")
    r = requests.get(rs)
    logging.info(f"result for {rs}: {r.reason} {r.json()}")


def run_work_block():
    start = time.time()
    do_works(e_blocksize)
    stop = time.time()
    dur = stop - start
    dur1 = float(dur) / e_blocksize
    logging.info(f"took {dur:.2f} seconds for {e_blocksize} calls")
    logging.info(f"took {dur1:.2f} seconds for 1 call")


def run_work_blocks():
    block_cnt = 1
    while True:
        run_work_block()
        logging.info(f"-- finished running work block {block_cnt} --------------------------------------")
        block_cnt += 1


def main(error_cnt: int):
    try:
        run_work_blocks()
    except requests.exceptions.ConnectionError as e:
        if error_cnt > 10:
            raise e
        else:
            logging.info(f"Caught {type(e)}. Error count: {error_cnt}")
            time.sleep(5)
            main(error_cnt + 1)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=e_loglevel)
    main(0)
