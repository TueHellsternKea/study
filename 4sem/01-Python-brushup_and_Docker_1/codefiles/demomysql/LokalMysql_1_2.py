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
            
        # SQL
        df = pd.read_sql('SELECT * FROM EmployeesSale', db_conn)
        print(df)

    except exc.SQLAlchemyError as e:
        print(e)

    finally:
        db_conn.dispose() # Close connection

if __name__ == '__main__':
    connect()