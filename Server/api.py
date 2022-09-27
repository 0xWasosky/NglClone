# file api - python api -  Python version: Python 3.10.6
import hashlib
from socket import herror
from flask import Blueprint, request  # pip install flask
from util.mongo import mongodb


api = Blueprint("api", __name__)
mongo = mongodb()


@api.route("/api/v1/send-question", methods=["POST"])
def send():
    header = request.headers.get("x-code")
    if header == "unicode": pass
    else:
        return {"Error" : 401}

    json = request.get_json()
    mongo.send_question(json["username"], json["question"])

    return {"Success": f"sent: {json['question']}"}


@api.route("/api/v1/get-question", methods=["POST"])
def get():
    json = request.get_json()
    question = mongo.get_question(json["username"], json["key"], json["index"])
    
    return {"Success": question}


@api.route("/api/v1/add-user", methods=["POST"])
def add():
    json = request.get_json()
    mongo.add_user(json["username"], hashlib.sha256(
        json["key"].encode()).hexdigest())
    
    return  {"Success": f"{json['username']} added"}

