# Modules
import pymongo

# Connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Find - Simpel - lastname
myquery = { "lastname": "Hansen" }
mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

# Find all there starts with H
myquery = { "lastname": { "$gt": "H" } }
mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)