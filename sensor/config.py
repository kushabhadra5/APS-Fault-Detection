#Import required dependencies and packages
import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")

#Connecting to MongoDB load the data:
client = pymongo.MongoClient()