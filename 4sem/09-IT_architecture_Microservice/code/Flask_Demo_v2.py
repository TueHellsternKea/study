# Flask Demo

# Import
from flask import Flask
import platform

# NoSQL
import pymongo
from pymongo import MongoClient

# Flask App
app = Flask(__name__)

# Start point - Hello KEA
@app.route('/')
def hello():
    return 'Hello KEA!'

# Check the operation system of your computer
@app.route('/oscheck')
def oscheck():
    my_os = platform.system()
    return 'Your operation system is: ' + my_os

# NoSQL Data
@app.route('/nosqldata')
def nosqldata():
    # Connection string
    connstring = "mongodb+srv://hellstern:2Naimo6868/?@cluster0.huvwp.mongodb.net/?retryWrites=true&w=majority"
    cluster = MongoClient(connstring)
    db = cluster["company"]
    collection = db["customers"]
    #return 'Test NoSQL'
    return collection.find_one({ "firstname":"Kim" })

# NoSQL Data
@app.route('/mysqldata')
def mtsqldata():
    return 'Test MySQL'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)