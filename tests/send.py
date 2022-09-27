import requests


header = {"x-code" : "unicode"}
data = {
    "username" : "x",
    "question" : "How old are you?"
}

r = requests.post("http://localhost:5000/api/v1/send-question", headers=header, json=data)
print(r.content.decode())
