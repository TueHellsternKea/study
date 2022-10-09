# FastAPi

# Getting startede
This is a simple example of how to get FastAPI working

## Install FastAPI
You need to install FastAPI

    pip3 install fastapi

## Install Uvicorn
You will also need Uvicorn to run the server

    pip3 install uvicorn

This will install Uvicorn with minimal (*pure Python*) dependencies.

## Simpel main.py
Let's create the simpels possible implementation of FastAPI. Create this Python file - **main.py**:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hi Kea students"}
```
## Run the server
To run the server, use this command in the samen foldes as your main.py file

    uvicorn main:app --reload

![](./image/uvicorn-1.jpg)

The **--reload** flag tells Uvicorn to reload the server whenever new code is added to the application. Next, open your browser and navigate to http://127.0.0.1:8000, where you’ll see a JSON response.

![](./image/uvicorn-2.jpg)

# Using MySQL and FastAPI
Let's build a simpel API to create a entry (customer) in your MySQL database and get all the data from this.

## SQLAlchemy
First you need a way to connect to MySQL in Python, for this I will be using SQLAlchemy.

SQLAlchemy is a Python SQL toolkit and Object Relational Mapper that gives you the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and *Pythonic* domain language.

To install SQLAlchemy use:

    pip3 install sqlalchemy


## MySQL Database
We need a data and a simpel table for this example. You can use this SQL kode for creating the database and the table.

```sql
CREATE DATABASE keacustomers;
USE keacustomers;

CREATE TABLE customers(
    id INT(6) AUTO_INCREMENT PRIMARY KEY,
    cust_name VARCHAR(50),
    cust_email VARCHAR(50),
    cust_mobil VARCHAR(50)
);

INSERT INTO customers(cust_name, cust_email, cust_mobil)
VALUES(
    'Tue Hellstern',
    'tueh@kea.dk',
    '+45 12345678'
);
```

You can download the SQL file: [keacustomers.sql](./codefiles/keacustomers.sql)


# Opgave til den 24-10-2022
Til den 24-10-2022 skal i lave denne opgave 


# Links
- [fastapi.tiangolo.com](https://vfastapi.tiangolo.com/)
- [github.com/tiangolo/fastapi](https://github.com/tiangolo/fastapi)
- [www.uvicorn.org](https://www.uvicorn.org/)