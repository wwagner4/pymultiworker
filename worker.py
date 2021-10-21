import random
import uuid
from time import sleep

from flask import Flask

wid = str(uuid.uuid4())[:4]
name = f"w-{wid}"
app = Flask(name)


@app.route('/<cnt>')
def index(cnt: str):
    n = random.randint(1, 7)
    # delay a random duration to avoid 'print' overlapping
    sleep(random.random() * 0.1)
    print(f"received: /{cnt} n:{n}")
    for i in range(1, n + 1):
        sleep(0.5)
        print(f"working /{cnt} - {i} / {n}")
    return {
        "cnt": cnt,
        "worker": app.name
    }


if __name__ == '__main__':
    print(f"started worker. name: {name} id: {wid}")
    app.run(debug=False, host="0.0.0.0", port=8080)
