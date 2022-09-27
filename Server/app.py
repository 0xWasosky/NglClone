from flask import Flask, redirect
from api import api


app = Flask(__name__)
app.register_blueprint(api)


@app.route("/")
def home():
    return redirect("/infos")


@app.route("/infos")
def infos():
    info = [
        {
            "path": "/api/v1/send-question",
            "method": "POST",
            "headers": "X-uncode: UNICODE",
            "json": "username: Wassoky, question: how are you?"
        },
        {
            "path": "/api/v1/get-question",
            "method": "POST",
            "headers": "null",
            "json": "username: Wassoky, key: mykey, index: 1"
        },
        {
            "path": "/api/v1/add-user",
            "method": "POST",
            "headers": "null",
            "json": "username: Mark, key: mykey2"
        }
    ]
    return info


if __name__ == "__main__":
    app.run("localhost")
