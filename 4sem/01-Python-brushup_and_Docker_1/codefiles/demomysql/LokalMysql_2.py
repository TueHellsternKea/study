# Import
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

# Connect to MySQL database
def connect():

    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config) # ** defining db_config to "capture" all keywords

        if conn.is_connected():
            print('Connection established')
            
            # SQL - SELECT * FROM categories
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM categories')

            row = cursor.fetchone()

            while row is not None:
                print(row)
                row = cursor.fetchone()

        else:
            print('Connection failed')

    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed')


if __name__ == '__main__':
    connect()