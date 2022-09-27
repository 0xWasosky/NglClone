import requests


data = {
    "username" : "x",
    "key" : "x"
}

r = requests.post("http://localhost:5000/api/v1/add-user", json=data)
print(r.content.decode())
