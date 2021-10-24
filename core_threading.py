import logging
import os
import sys
import time

import requests
from concurrent.futures import ThreadPoolExecutor

e_host = os.getenv("HOST", "localhost")
e_port = int(os.getenv("PORT", "5000"))
e_loglevel = os.getenv("LOGLEVEL", "INFO")


def do_works(n: int):
    ids = range(n)
    with ThreadPoolExecutor(max_workers=5) as executor:
        return executor.map(do_work, ids)


# noinspection HttpUrlsUsage
def do_work(cnt):
    rs = f"http://{e_host}:{e_port}/{cnt}"
    logging.info(f"sending {rs}")
    r = requests.get(rs)
    logging.info(f"result for {rs}: {r.reason} {r.json()}")


def run_work_block():
    n = 10
    start = time.time()
    do_works(n)
    stop = time.time()
    dur = stop - start
    dur1 = float(dur) / n
    logging.info(f"took {dur:.2f} seconds for {n} calls")
    logging.info(f"took {dur1:.2f} seconds for 1 call")


def run_work_blocks():
    while True:
        run_work_block()
        logging.info("-- Finished work block ------------------------------------------")
        time.sleep(10)


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
