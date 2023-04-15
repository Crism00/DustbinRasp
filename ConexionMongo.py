from pymongo import MongoClient
ca = certifi.where()


class Database:
    def __init__(self, database="test", collection="test"):

        self.mongo_client = MongoClient("mongodb+srv://admin:administrador@cluster0.fzaqu9v.mongodb.net/",
                                        serverSelectionTimeoutMS=3000, tlsCAFile=ca)
        self._db = self.mongo_client[database]
        self._collection = self._db[collection]


    def insert_many(self, data):
        self._collection.insert_many(data)

    def find(self, query):
        return self._collection.find(query)

    def set_collection(self, collection):
        self._collection = self._db[collection]

    def delete_data(self, collection: str):
        self._collection = self._db[collection]
        self._collection.drop()

    def set_database(self, database):
        self._db = self.mongo_client[database]
        
    def insertOne(self, data):
        self._collection.insert_one(data)