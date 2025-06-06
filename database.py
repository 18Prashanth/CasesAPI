from pymongo import MongoClient

# Replace <username>, <password>, and <dbname> with actual values
url = "mongodb+srv://18gowda2002:YOf78stVbwBuJPnX@cluster0.unbniln.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(url)

# Access the database
db = client["mydatabase"]

# Access or create a collection
collection = db["users"]

print("Connected to MongoDB Atlas!")

sample_user = {
    "name": "Prashanth",
    "email": "prashanth@example.com",
    "age": 24
}

inserted_id = collection.insert_one(sample_user).inserted_id
print(f"User inserted with ID: {inserted_id}")