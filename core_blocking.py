import logging
import os
import sys
import time

import requests

e_host = os.getenv("HOST", "172.17.0.2")
e_port = int(os.getenv("PORT", "5000"))
e_loglevel = os.getenv("LOGLEVEL", "INFO")


def do_works(n: int):
    [do_work(cnt) for cnt in range(n)]


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


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=e_loglevel)
    while True:
        run_work_block()
        logging.info("-- Finished work block ------------------------------------------")
        time.sleep(10)
