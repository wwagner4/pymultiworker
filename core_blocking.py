import time

import requests


def do_works(n: int):
    [do_work(cnt) for cnt in range(n)]


def do_work(cnt):
    rs = f"http://172.17.0.2:8080/{cnt}"
    print(f"sending {rs}")
    r = requests.get(rs)
    print(f"result for {rs}: {r.reason} {r.json()}")


def run_work_block():
    n = 10
    start = time.time()
    do_works(n)
    stop = time.time()
    dur = stop - start
    dur1 = float(dur) / n
    print(f"took {dur:.2f} seconds for {n} calls")
    print(f"took {dur1:.2f} seconds for 1 call")


if __name__ == '__main__':
    while True:
        run_work_block()
        print("-- Finished work block ------------------------------------------")
        time.sleep(10)
