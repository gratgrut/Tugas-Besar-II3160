from pymongo import MongoClient
from database import settings

client = MongoClient(settings.mongodb_uri, settings.port)
# db = client[heart_disease_api]
