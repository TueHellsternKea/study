# Update
# Modules
import pymongo

# Connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Update One - Only fist one
myquery = { "lastname": "Hellstern" }
newvalues = { "$set": { "lastname": "My new lastname" } }
mycol.update_one(myquery, newvalues)

# Print all after update:
for x in mycol.find():
  print(x)

# Update Many
myquery = { "city": "Odense"  }
newvalues = { "$set": { "city": "Odense C" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")

# Print all after update:
for x in mycol.find():
  print(x)