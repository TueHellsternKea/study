# Flask Demo

# Import
from flask import Flask
import platform

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
    return 'Test NoSQL'

# NoSQL Data
@app.route('/mysqldata')
def mtsqldata():
    return 'Test MySQL'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)