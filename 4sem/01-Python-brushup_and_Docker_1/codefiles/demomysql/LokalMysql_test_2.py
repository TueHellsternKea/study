from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

import pandas as pd
from sqlalchemy import create_engine

def query_with_fetchall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM CategorySale')
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)

        CategorySale = pd.read_sql('SELECT * FROM CategorySale', conn)
        print(CategorySale)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    query_with_fetchall()