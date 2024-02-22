from pymongo import MongoClient
from dotenv import load_dotenv
import os

class Database:
    uri = os.getenv("MONGODB_URI")
    
    def __init__(self):
        self.client = MongoClient(self.uri)
        self.db = self.client["app"]
    
    def get_collection(self, name):
        return self.db[name]