# Import
from mysql.connector import MySQLConnection, Error, read_db_config
# from python_mysql_dbconfig import read_db_config

# Connect to MySQL database
def connect():

    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established')
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