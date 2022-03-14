# MySQL

from sqlalchemy import create_engine, exc
import configparser

def conn_open():
    db_conn = None
    try:
        # Read config.ini file
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Connect to MySQL
        db_connection_str = config['mysqlini']['conn_string']
        db_conn = create_engine(db_connection_str)
        
        return db_conn

    except exc.SQLAlchemyError as e:
        print(e)

    finally:
        db_conn.dispose() # Close connection