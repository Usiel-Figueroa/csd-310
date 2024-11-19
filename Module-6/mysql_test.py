# Usiel Figueroa
# Module 6.2 Assignment: Movies: Setup
# CSD310-A311 Database Development and Use
# November 12, 2024

import mysql.connector

config = {
    'user': 'movies_user',
    'password': 'popcorn',
    'host': '127.0.0.1',
    'database': 'movies',
    'raise_on_warnings': True
}

try:
    db = mysql.connector.connect(**config)
    if db.is_connected():
        print("Connection successful!")
    db.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")
