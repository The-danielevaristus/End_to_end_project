
import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo

from dotenv import load_dotenv
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging





from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
print(f"MONGODB_URI: {MONGODB_URI}")

ca=certifi.where()

class NetworkDataExtract():



    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) 
        
    def cv_to_json_converter(self, file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
        
    def push_data_to_mongodb(self, records, database, collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records


            self.mongo_client=pymongo.MongoClient(MONGODB_URI)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

if __name__=="__main__":
    FILE_PATH = os.path.join("NetworkData", "phisingData.csv")
    DATABASE="Daniel"
    COLLECTION="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.cv_to_json_converter(file_path=FILE_PATH)
    print(f"Number of records to be inserted: {len(records)}")
    num_records=networkobj.push_data_to_mongodb(records=records, database=DATABASE, collection=COLLECTION)
    print(f"Number of records inserted: {num_records}")
