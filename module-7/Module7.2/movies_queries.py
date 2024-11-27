# Usiel Figueroa
# Module 7.2 Assignment: Movies: Tables Queries
# CSD310-A311 Database Development and Use
# November 26, 2024
# Resources: Forta, B. (n.d.). Sams Teach Yourself SQL in 10 Minutes, Fifth Edition. Retrieved from https://platform.virdocs.com/read/1347763/21/#/4/2/10/14/2/2,/1:0,/1:0
# ChatGPT

import mysql.connector

# Configuration for database connection
config = {
    'user': 'movies_user',
    'password': 'popcorn',
    'host': '127.0.0.1',
    'database': 'movies',
    'raise_on_warnings': True
}

try:
    # Connect to the database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("Connection successful! Running queries...\n")

    # --- 1. Select all fields from the Studio table ---
    print("-- DISPLAYING Studio RECORDS --")
    query1 = "SELECT * FROM Studio;"
    cursor.execute(query1)
    studios = cursor.fetchall()
    for studio in studios:
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}")
        print()  # Add blank line for formatting


    # --- 2. Select all fields from the Genre table ---
    print("-- DISPLAYING Genre RECORDS --")
    query2 = "SELECT * FROM Genre;"
    cursor.execute(query2)
    genres = cursor.fetchall()
    for genre in genres:
        print(f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}")
        print()  # Add blank line for formatting


    # --- 3. Select movie names for movies with runtime less than 2 hours ---
    print("-- DISPLAYING Short Film RECORDS --")
    query3 = "SELECT film_name, film_runtime FROM Film WHERE film_runtime < 120;"
    cursor.execute(query3)
    short_films = cursor.fetchall()
    for film in short_films:
        print(f"Film Name: {film[0]}")
        print(f"Runtime: {film[1]}")
        print()


    # --- 4. Select film names and directors grouped by director, ordered by director ---
    print("-- DISPLAYING Director RECORDS in Order --")
    query4 = """
        SELECT film_director, GROUP_CONCAT(film_name ORDER BY film_name ASC SEPARATOR ', ') AS Films
        FROM Film
        GROUP BY film_director
        ORDER BY film_director ASC;
    """
    cursor.execute(query4)
    director_movies = cursor.fetchall()
    for row in director_movies:
        films = row[1].split(', ')  # Split films into individual names
        for film in films:
            print(f"Film Name: {film}")
            print(f"Director: {row[0]}")
            print()  # Add blank line for formatting


except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Ensure the connection is closed
    if db.is_connected():
        cursor.close()
        db.close()
        print("Connection closed.")





