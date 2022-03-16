from sqlalchemy import create_engine
import pandas as pd

db_connection_str = 'mysql://root:Naimo6868/?@127.0.0.1:3306/northwind'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM EmployeesSale', con=db_connection)

print(df)
