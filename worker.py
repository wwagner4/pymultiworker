import random
import uuid
from time import sleep

from flask import Flask

wid = str(uuid.uuid4())[:4]
name = f"pymultiworker-{wid}"
app = Flask(name)


@app.route('/<cnt>')
def index(cnt: str):
    print(f"received request: {cnt}")
    n = random.randint(2, 5)
    for i in range(n):
        print(f"working {i} of {n}")
        sleep(0.5)
    return f"This is the result for {cnt}"


if __name__ == '__main__':
    print(f"started worker. name: {name} id: {wid}")
    app.run(debug=True, host="0.0.0.0", port=8080)
