# List records
# Modules
import pymongo

# Connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Find first ID
x = mycol.find_one()
print(x)

# Find all
for x in mycol.find():
    print(x)

# "Select" columns
# No id
for x in mycol.find({},{ "_id": 0, "firstname": 1, "lastname": 1 }):
    print(x)

# Exclude id and lastname
for x in mycol.find({},{ "_id": 0, "lastname": 0 }):
    print(x)

