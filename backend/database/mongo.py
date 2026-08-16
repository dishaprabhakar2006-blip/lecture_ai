import os
from pymongo import MongoClient
client=MongoClient(os.getenv("MONGODB_URL"))
db=client["lecture-ai"]
videos_collection=db["videos"]