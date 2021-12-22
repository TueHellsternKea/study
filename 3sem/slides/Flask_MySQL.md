---
title: Flask & MySQL - 17-09
theme: gaia
_class: lead
paginate: true
marp: true
backgroundColor: #fff
size: 4K
@auto-scaling true
footer: 'Tue Hellstern - 2021'
html: true
---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# Agenda<!-- fit -->

- Flask and MySQL
- Scrumwise
- Sprint 2 review
- Sprint 3 planning

---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# Flask & MySQL<!-- fit -->
Flask is a web framework that provides libraries to build lightweight web applications in python. It is developed by Armin Ronacher who leads an international group of python enthusiasts (POCCO). It is based on WSGI toolkit and jinja2 template engine. Flask is considered as a micro framework.

---

![bg right:43% 140%](https://github.com/officegeek/image/raw/main/flask.png)
## Installing FLASK
The first thing to do is to install Flask on your Raspberry Pi. Go to Terminal and enter:

    sudo apt-get install python3-flask

---

# Create 2 sub-folders: 

- **static** *for CSS files*
- **templates** *for HTML files*

The final folder *tree* will be:

    /flaskdemo
        /static
        /templates

---

# Python WebServer Application
Create the Python *WebServer* with Flask.

- Create a file (*app.py*) in the *flaskdemo* folder
- Insert this code
  
```python
    from flask import Flask

    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return 'Hello 3. semester'
    
    if __name__ == '__main__':
        app.run(debug=True, port=5000, host='0.0.0.0')
```
You use port **5000** and it can be accessed from all ip addresses - **host='0.0.0.0'**

---

![bg right:41% 80%](https://github.com/officegeek/image/raw/main/FlaskFlowDemo_1.png)

# Run the application - app.py

    python3 app.py

Point your browser to the IP address of the Raspberry PI and port *5000*

    http://raspberryip_ip:5000

---

![bg right:50% 150%](https://github.com/officegeek/image/raw/main/pingpong.jpg)
# Sense Hat Data
## Show the data from the Sense Hat in a webpage

- senesdata.py
- index.html
- style.css
- database.html
---

# index.html
Create a file named **index.html**, save it in the **/templates** folder.

```html
<!DOCTYPE html>
   <head>
      <title>{{ time }}</title>
      <link rel="stylesheet" href="../static/style.css/">
   </head>
   <body>
      <h1>Sense Hat Output</h1>
      <h2>The temperatur is: {{ temperatur }}</h2>
      <h2>The pressure is: {{ pressure }}</h2>
      <h2>The humidity is: {{ humidity }}</h2>
   </body>
</html>
```
Anything in *double curly* braces within the HTML template is interpreted as a **variable** that would be passed to it from the Python script via the **render_template** function.

---

# senesdata.py - 1. route

```python
from flask import Flask, render_template
import datetime
from sense_hat import SenseHat
import mysql.connector

# Sense data
sense = SenseHat()

# Flask
app = Flask(__name__)
    
@app.route("/")
def templetdata():
    now = datetime.datetime.now()
    timeString = now.strftime("%d-%m-%Y %H:%M")
    temperaturString = round(sense.get_temperature(),1)
    pressureString = round(sense.get_pressure(),1)
    humidityString = round(sense.get_humidity(),1)

    templateData = {
        'time': timeString,
        'temperatur': temperaturString,
        'pressure': pressureString,
        'humidity': humidityString
    }
    return render_template('index.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
```    

---

# style.css
```css
body {
    background: grey;
}

h1, h2 {
    color:white;
}

p {
    color:white;
}
```

---

![bg 95%](https://github.com/officegeek/image/raw/main/FlaskFlow_1.png)

---

# senesdata.py - 2. route

```python
@app.route("/database")
def databasedata():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="pi",
            password="Your_Password",
            database="sensedata"
        )
        
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM hatdata")
        data = mycursor.fetchall()

        return render_template("database.html", data=data)

    except Exception as e:
        return (str(e))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
```
---

# database.html
```html
<!DOCTYPE html>
   <head>
      <title>Database</title>
      <link rel="stylesheet" href="../static/style.css/">
   </head>

   <body>
        <h1>Database info</h1>
        <br>
        <table border="1" cellpadding="5" cellspacing="5">
            {% for row in data %}
                <tr>
                {% for d in row %}
                    <td>{{ d }}</td>
                {% endfor %}
                </tr>
            {% endfor %}
        </table>
   </body>
</html>
```
---

![bg 95%](https://github.com/officegeek/image/raw/main/FlaskFlow_2.png)

---

![bg 85%](https://github.com/officegeek/image/raw/main/FlaskFlowDemo_2.png)
![bg 85%](https://github.com/officegeek/image/raw/main/FlaskFlowDemo_3.png)

---

![bg right:50% 95%](https://github.com/officegeek/image/raw/main/scrumwise_1.png)
# Scrumwise


https://www.scrumwise.com/scrum/#/overview/project/group-1/id-199424-3369-1


---

# 2021-37: Uge 37

- Sprint Retrospective
- **SCRUM** - *Tirsdag 14-09*
    - Sprint Review
    - Sprint Planning
- **IT** - *Fredag 17-09*
    - SCRUM Backlog
    - IT emne - *Hardware - computerkomponenter*

---

# 2021-38: Uge 38 - Afslutning

- Sprint Retrospective
- **SCRUM** - *Tirsdag 21-09*
    - Sprint Review
- **IT** - *Fredag 24-09 - Kl. 08:30 til 12:30*
    - Præsentation
    - IT emne - *Operating systems*


---

# Aflevering
- Kode
- IT-emner
- PowerPoint