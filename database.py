#import connector for sql
import mysql.connector
import firebase_admin
    
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


def create_firebase_connection():
    cred_obj = firebase_admin.credentials.Certificate('nea-database-b96f8-firebase-adminsdk-mo1sn-a344a5de3b.json')
    default_app = firebase_admin.initialize_app(cred_object, {
	'databaseURL':'https://nea-database-b96f8-default-rtdb.asia-southeast1.firebasedatabase.app/'
	})
