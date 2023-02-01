from pymongo import MongoClient
from . import exporter


client = MongoClient(exporter.mongo_details)

db = client[exporter.database]

collection = db[exporter.collection]
