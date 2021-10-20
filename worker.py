import uuid

from flask import Flask

wid = str(uuid.uuid4())[:4]
name = f"pymultiworker-{wid}"
app = Flask(name)


@app.route('/<cnt>')
def index(cnt: str):
    print(f"received request: {cnt}")
    return f"Hello, World! {cnt}"


if __name__ == '__main__':
    print(f"started worker. name: {name} id: {wid}")
    app.run(debug=True, host="0.0.0.0", port=8080)
