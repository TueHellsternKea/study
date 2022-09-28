# Modules
import pymongo
from pymongo import MongoClient

# Connection
# Connection string
connstring = "mongodb+srv://hellstern:<PASSWORD>@xxxx.yyyy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = MongoClient(connstring)

# Create database - company
db = cluster["company"]

# Create collection - clients
collection = db["customers"]

# Create a new document
collection.insert_one({"-id":101, "companyname":"Kea", "contact":"Tue Hellstern"})
collection.insert_one({"-id":101, "companyname":"CPH Business", "contact":"Ole Hansen"})
collection.insert_one({"-id":101, "companyname":"ITU", "contact":"Peter Jensen"})

# Find
print(collection.find_one({ "companyname":"Kea" }))