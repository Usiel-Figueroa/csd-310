# Usiel Figueroa
# Module 6.3 Assignment: Bonus
# CSD310-A311 Database Development and Use
# November 18, 2024

import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the configuration using environment variables
config = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("PASSWORD"),
    "host": os.getenv("HOST"),
    "database": os.getenv("DATABASE"),
    "raise_on_warnings": os.getenv("RAISE_ON_WARNINGS", "True") == "True"  # Convert to bool if needed
}

try:
    # Attempt to connect to the database
    connection = mysql.connector.connect(**config)
    print("Connection successful!")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    # Close the connection if it was established
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed.")
