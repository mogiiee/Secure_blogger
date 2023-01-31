from dotenv import load_dotenv, find_dotenv
import os

mongo_details = os.environ.get("MONGO_CREDENTIALS")
collection = os.environ.get("COLLECTION_NAME")
database = os.environ.get("DB_NAME")
