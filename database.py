#import connector for sql
import mysql.connector
    
#function for DB connection
def create_connection():
    """ create a database connection to the mySQL database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = mydb = mysql.connector.connect(
    host="us-cdbr-east-04.cleardb.com",
    user="bd157bd1e2a8d8",
    password = "1b8272d0",
    database="heroku_e9e0293aeac706c"
    )
        return conn
    except Error as e:
        print(e)
    return None



