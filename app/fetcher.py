import os
import pandas as pd
from pymongo import MongoClient

class MongoFetcher:
    def __init__(self):
        # Connect using environment variable
        mongo_uri = os.getenv("MONGO_URI")
        self.client = MongoClient(mongo_uri)
        self.db = self.client["IranMalDB"]
        self.collection = self.db["tweets"]

    def fetch_all(self):
        # Fetch all records and return as DataFrame
        data = list(self.collection.find())
        df = pd.DataFrame(data)
        df.rename(columns={"text": "original_text"}, inplace=True)
        return df
