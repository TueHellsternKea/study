# Flask
Flask is a Python framework for creating web applications.

## Install
You need to install some modules:

    pip3 install flask
    pip3 install mysql-connector-python
    pip3 install flask-mysql



## Folders

    mkdir webapp
    cd webapp

## Python file
Create a new Python file, **app.py**, inside the *webapp* folder.

    nano app.pyt

**Insert this code:**

    from flask import Flask
    from sense_hat import SenseHat
    
    # Sense Hat
    sense = SenseHat()

    # Flask
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Temp: ' + str(round(sense.get_temperature(),2))

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')

Save the file and run it.

Open http://<Raspberry_Pi_IP_Adresse>:5000 on your computer - not the Raspberry PI
