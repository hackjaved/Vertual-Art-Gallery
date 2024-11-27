'''# In util/DBConnection.py
import sqlite3  # or your specific database library

class DBConnection:
    @staticmethod
    def getConnection():
        try:
            connection = sqlite3.connect('VirtualArtGallery.db')  # Replace with your database connection logic
            return connection
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None
'''
'''
# In util/DBConnection.py
import mysql.connector  # Make sure to use the correct MySQL library

class DBConnection:
    @staticmethod
    def getConnection():
        try:
            connection = mysql.connector.connect(
                host='localhost',            # e.g., 'localhost'
                #user='your_user',            # your database user
                #assword='your_password',     # your database password
                database='VirtualArtGallery'      # your specific database
            )
            return connection
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None'''

'''import pyodbc
from util.PropertyUtil import PropertyUtil

class DBConnection:

    @staticmethod
    def getConnection():
        try:
            connection_string=PropertyUtil.getPropertyString()
            connection=pyodbc.connect(connection_string)
            print("Connected successfully")
            return connection
        except Exception as e:
            print(str(e) + '--Database is not connected--')
            return None
'''            '''
import pyodbc

# SQL Server connection using Windows Authentication
def create_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=RUSHMITHA\\SQLEXPRESS01;'
            'DATABASE=VirtualArtGallery;'
            'Trusted_Connection=yes;'
        )
        print("Connection successful!")
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example of using the connection
conn = create_connection()

if conn is not None:
    cursor = conn.cursor()
    # You can execute your SQL queries here
    # For example: cursor.execute("SELECT * FROM Users WHERE ID = ?", user_id)
else:
    print("Failed to connect to the database.")
'''
class DBConnection:
    def __init__(self):
        self.conn = None

    def create_connection(self):
        try:
            import pyodbc
            self.conn = pyodbc.connect(
                r'DRIVER={ODBC Driver 17 for SQL Server};'
                r'SERVER=MUBEENA\SQLEXPRESS;'
                r'DATABASE=VirtualArtGallery;'
                r'Trusted_Connection=yes;'
            )
            print("Connection successful!")
        except Exception as e:
            print(f"Connection failed: {e}")
            self.conn = None

    def get_connection(self):
        if self.conn is None:
            self.create_connection()
        return self.conn
