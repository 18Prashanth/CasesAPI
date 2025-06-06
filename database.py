from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
import pymongo
from pymongo.server_api import ServerApi

load_dotenv()
uri = os.getenv("MONGO_URI")
db_name = os.getenv("DATABASE_NAME")

client = AsyncIOMotorClient("mongodb://localhost:27017")

db = client[db_name]
