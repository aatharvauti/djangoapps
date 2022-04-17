# https://console.clever-cloud.com/

from dotenv import load_dotenv
import os

load_dotenv()
# VENV Importing
host = os.getenv('HOST')
db = os.getenv('DB')
user = os.getenv('USER')
port = os.getenv('PORT')
password = os.getenv('PASSWORD')
uri = os.getenv('URI')

# pip install mysql-connector-python
import mysql.connector


class DBHelper:

    def __init__(self):
        # Create Connection
        self.mydb = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db
        )
    
    def __del__(self):
        # Close Connection
        self.mydb.close()

    def execute_select_query(self, query, params):
        
        # Create cursor 
        mycursor = self.mydb.cursor(dictionary=True)

        # Fire Query
        mycursor.execute(query, params)

        # Extract result
        myresult = mycursor.fetchall()

        return myresult
