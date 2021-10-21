import logging
import os
import random
import sys
import uuid
from time import sleep

from flask import Flask

wid = str(uuid.uuid4())[:4]
name = f"w-{wid}"
app = Flask(name)

e_host = os.getenv("HOST", "0.0.0.0")
e_port = int(os.getenv("PORT", "5000"))
e_loglevel = os.getenv("LOGLEVEL", "INFO")


@app.route('/<cnt>')
def index(cnt: str):
    n = random.randint(1, 7)
    sleep(random.random() * 0.1)
    logging.info(f"{wid} -- received: /{cnt} n:{n}")
    for i in range(1, n + 1):
        sleep(0.5)
        logging.info(f"{wid} -- working /{cnt} - {i} / {n}")
    return {
        "cnt": cnt,
        "worker": app.name
    }


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=e_loglevel)
    logging.info(f"{wid} -- started worker. name: {name}")
    app.run(debug=False, host=e_host, port=e_port)
