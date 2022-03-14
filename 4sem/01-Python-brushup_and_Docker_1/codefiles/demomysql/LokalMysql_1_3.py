# MySQL Database connection with sqlalchemy
# Tue Hellstern

# Import
from sqlalchemy import create_engine, exc
import pandas as pd

# MySQL connection
def connect():
    db_conn = None
    try:
        # Connect to MySQL
        db_connection_str = 'mysql://root:Naimo6868/?@127.0.0.1:3306/northwind'
        db_conn = create_engine(db_connection_str)
        
        return db_conn

    except exc.SQLAlchemyError as e:
        print(e)

    finally:
        db_conn.dispose() # Close connection

# EmployeesSale
def getEmployeesSale():
    conn = connect()
    EmployeesSale = pd.read_sql('SELECT * FROM EmployeesSale', conn)
    return EmployeesSale

# CategorySale
def getCategorySale():
    conn = connect()
    CategorySale = pd.read_sql('SELECT * FROM CategorySale', conn)
    return CategorySale

# Top5Products
def getTop5Products():
    conn = connect()
    Top5Product = pd.read_sql('SELECT * FROM Top5Products', conn)
    return Top5Product

# Top5Customers
def getTop5Customers():
    conn = connect()
    Top5Customers = pd.read_sql('SELECT * FROM Top5Customers', conn)
    return Top5Customers

# Get all data
def getdata():
    print(getEmployeesSale())
    print(getCategorySale())
    print(getTop5Products())
    print(getTop5Customers())

if __name__ == '__main__':
    getdata()