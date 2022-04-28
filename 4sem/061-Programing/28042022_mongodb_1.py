# Modules
import pymongo

# MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Database
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Insert one customer
mydict = { "firstname": "Tue", "lastname": "Hellstern", "city": "Snekkersten", "land": "Danmark" }
x = mycol.insert_one(mydict)

# Print _id - one customer
print(x.inserted_id)

# Flere
# Insert multiply customers
mylist = [
  { "firstname": "Lis", "lastname": "Hansen", "city": "København"},
  { "firstname": "Ole", "lastname": "Hansen", "city": "København", "land": "Danmark" },
  { "firstname": "Peter", "lastname": "Larsen", "city": "Roskilde"},
  { "firstname": "Lis", "lastname": "Rasmussen", "city": "Odense"},
  { "firstname": "Kim", "lastname": "Rasmussen", "city": "Odense", "land": "UK" },
  { "firstname": "Pia", "lastname": "Rasmussen", "city": "Odense"},
  { "firstname": "Karsten", "lastname": "Petersen", "city": "Helsingør"},
  { "firstname": "Klaus", "lastname": "Olsen", "city": "København"}
]

x = mycol.insert_many(mylist)

# Print list of _id
print(x.inserted_ids)