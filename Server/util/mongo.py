# Python version: Python 3.10.6

from pymongo import MongoClient  # pip install pymongo


client = MongoClient("mongodb://localhost:27017")  # Local host -> mongo db
db_name = client.nglcopy
collection = db_name.question


class mongodb:
    def __init__(self) -> None:
        pass

    def add_user(self, username_add: str = None, key_add: str = None) -> dict:
        self.username_add = username_add
        self.key_add = key_add

        if collection.find_one({"username": self.username_add}, {"_id": 0, "username": 1}):
            return {"Error": "Chose another username!"}
        else:
            collection.insert_one(
                {"username": self.username_add, "key": self.key_add, "questions": []})
            return {"Success": f"{self.username_add} added"}

    def send_question(self, username_send: str = None, question: str = None):
        self.username_send = username_send
        self.question = question

        try:
            collection.update_many({"username": self.username_send}, {
                               "$push": {"questions": self.question}})
            return {"Success": f"sent: {self.question}"}
        except:
            return {"Error" : "retry"}

    def get_question(self, username_get: str = None, key_get: str = None, index: int = None):
        self.username_get = username_get
        self.key_get = key_get
        self.index = index

        try:
            return collection.find_one({"username": self.username_get, "key": self.key_get}, {"_id":  0, "questions": 1})["questions"][self.index]
        except:
            return {"Error": f"question not found index: {self.index}"}
