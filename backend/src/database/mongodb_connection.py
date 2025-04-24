from pymongo import MongoClient
from src.config import Config

class MongoDBClient:
    def __init__(self):
        self.config = Config()
        mongo_uri = self.config.get_mongodb_url()
        self.client = MongoClient(mongo_uri)
        self.db = self.client[self.config.get_mongodb_db_name()]
        self.collection_name = self.config.get_mongodb_collection_name()

    def insert_chat_log(self, chat_data):
        collection = self.db[self.collection_name]
        collection.insert_one(chat_data)

    def find_chat_logs(self, query):
        collection = self.db[self.collection_name]
        return collection.find(query)

    def close(self):
        self.client.close()
