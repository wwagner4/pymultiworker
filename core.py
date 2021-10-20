from time import sleep

import requests


def main():
    cnt = 0
    while True:
        do_work(cnt)
        cnt += 1
        sleep(1)


def do_work(cnt):
    rs = f"http://172.17.0.2:8080/{cnt}"
    print(f"sending {rs}")
    r = requests.get(rs)
    print(f"result for {rs}: {r.reason} {r.text}")


if __name__ == '__main__':
    main()
