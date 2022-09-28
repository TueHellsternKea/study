#pip3 install "pymongo[srv]"

# Modules
import pymongo
from pymongo import MongoClient

# Connection
# Connection string
connstring = "mongodb+srv://hellstern:<password>@cluster0.huvwp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

cluster = MongoClient(connstring)

