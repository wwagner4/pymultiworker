from time import sleep

import requests


def main():
    cnt = 0
    while True:
        rs = f"http://172.17.0.2:8080/{cnt}"
        print(f"sending {rs}")
        r = requests.get(rs)
        print(f"result: {r}")
        cnt += 1
        sleep(1)


if __name__ == '__main__':
    main()
