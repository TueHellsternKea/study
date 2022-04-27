# Delete
# Modules
import pymongo

# Connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


# Delete by id/name - Fist one - Only one
myquery = { "firstname": "Tue" }
mycol.delete_one(myquery)

myquery = { "lastname": "Hansen" }
mycol.delete_one(myquery)

# Delete by id/name - Many
myquery = { "lastname": "Rasmussen" }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")

# Delete - start with K
myquery = { "firstname": {"$regex": "^K"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")

# Delete All Documents
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

# Delete/Drop collection
#mycol.drop()