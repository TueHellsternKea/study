# Using MongoDB at your local computer
This code is using the local installed MongoDB database.

# Creating a Database
You create a database in MongoDB with:

- Creating a MongoClient object
- Specify the connection URL with the correct ip address - This demo uses *localhost*
- Name of the database you want to create

MongoDB will create the database if it does not exist, and make a connection to it.

```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
```

*There has to be data/post in the database for it to show up in a listing!*

# Insert
You can insert data one post ad the time or as an array

**One post**
```python
# Insert one customer
mydict = { "firstname": "Tue", "lastname": "Hellstern", "city": "Snekkersten" }
x = mycol.insert_one(mydict)

# Print _id - one customer
print(x.inserted_id)
```

**Multiply posts**
```python
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
```

# Lists posts
You can list the post by different parameters

```python
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
```
# Update
You can update an exiting post

```python
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
```

# Delete
You can delete post by:

```python
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
mycol.drop()
```