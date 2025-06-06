from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
# Replace <username>, <password>, and <dbname> with actual values
uri = os.getenv("MONGODB_URI")
client = MongoClient(uri)

# Access the database
db = client["sumxioDb"]

# Access or create a collection
collection = db["cases"]


sample_user = {
    "name": "Prashanth",
    "email": "prashanth@example.com",
    "age": 24
}

inserted_id = collection.insert_one(sample_user).inserted_id
print(f"User inserted with ID: {inserted_id}")