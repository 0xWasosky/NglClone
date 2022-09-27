import requests


data = {
    "username" : "x",
    "key" : "x",
    "index" : 0
}

r = requests.post("http://localhost:5000/api/v1/get-question", json=data)
print(r.content.decode())