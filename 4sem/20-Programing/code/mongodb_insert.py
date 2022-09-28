# Modules
import pymongo

# Connection
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#myclient = pymongo.MongoClient("mongodb+srv://hellstern:XXXXXX@cluster0.huvwp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Insert one customer
mydict = { "firstname": "Tue", "lastname": "Hellstern", "city": "Snekkersten" }
x = mycol.insert_one(mydict)

# Print _id - one customer
print(x.inserted_id)

# Insert multiply customers
mylist = [
  { "firstname": "Lis", "lastname": "Hansen", "city": "København"},
  { "firstname": "Ole", "lastname": "Hansen", "city": "København"},
  { "firstname": "Peter", "lastname": "Larsen", "city": "Roskilde"},
  { "firstname": "Lis", "lastname": "Rasmussen", "city": "Odense"},
  { "firstname": "Kim", "lastname": "Rasmussen", "city": "Odense"},
  { "firstname": "Pia", "lastname": "Rasmussen", "city": "Odense"},
  { "firstname": "Karsten", "lastname": "Petersen", "city": "Helsingør"},
  { "firstname": "Klaus", "lastname": "Olsen", "city": "København"}
]

x = mycol.insert_many(mylist)

# Print list of _id
print(x.inserted_ids)