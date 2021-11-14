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
    user="b33cdae453531f",
    password = "6a5d5f6d",
    database="heroku_edda316505ad5d8"
    )
        return conn
    except Error as e:
        print(e)
    return None



