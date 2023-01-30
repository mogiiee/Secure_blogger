from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
from . import exporter

load_dotenv(find_dotenv())

client = MongoClient(exporter.mongo_details)

database = exporter.database

db = client.database

collection = db.exporter.collection
