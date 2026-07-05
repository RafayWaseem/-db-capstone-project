import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        db_password = os.getenv("DB_PASSWORD")

        # Establish the connection
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=db_password,
            database="LittleLemonDM"
        )

        if connection.is_connected():
            print("Successfully connected to the database")

            # Create a cursor object
            cursor = connection.cursor()

            return connection, cursor

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None, None
    
