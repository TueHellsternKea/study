# Import
import mysql.connector
from mysql.connector import Error

# MySQL connection
def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       user='root',
                                       password='Naimo6868/?',
                                       database='northwind')
        if conn.is_connected():
            print('Connected to MySQL database')
            
            # SQL - SELECT * FROM categories
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM categories')

            row = cursor.fetchone()

            while row is not None:
                print(row)
                row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == '__main__':
    connect()