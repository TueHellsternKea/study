# Python & MySQL

## Create Connection
Start by creating a connection to the database.

Use the username and password from your MySQL database:

    import mysql.connector

    mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
    )

## Create demo database
Use this SQL script for creating demo database:

    create database sensedata;

    create table hatdata (
        id int not null AUTO_INCREMENT,
        createdate datetime,
        temp double,
        primary key (id))

## Insert Into Table
To insert data into MySQL table, use the *INSERT INTO* statement.

Install the MySQL Python connector with:

    pip install mysql-connector-python

<div style="page-break-after: always;"></div>

Create a Python file with this content:

    # Imports
    import mysql.connector
    import ssl
    import datetime
    from sense_hat import SenseHat
    from time import sleep

    # Database connector
    mydb = mysql.connector.connect(
    host="localhost",
    user="pi",
    password="xxxxx",
    database="sensedata")

    # Sense
    sense = SenseHat()

    # Database
    mycursor = mydb.cursor()

    while True:
            # Date
            createdate = datetime.datetime.now()

            # Temp data
            temp = sense.get_temperature()

            # Get data
            sql = "INSERT INTO hatdata (createdate, temp) VALUES (%s, %s)"
            val = (createdate, temp)

            # Insert data
            mycursor.execute(sql, val)
            mydb.commit()

            # Pause before next insert
            sleep(0.5)

## Workbench
Open Workbench and check if the data is inserted.

    select * from hatdata;