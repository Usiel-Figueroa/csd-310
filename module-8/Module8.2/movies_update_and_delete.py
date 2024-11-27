# Usiel Figueroa
# Module 8.2 Assignment: Movies: Update & Delete
# CSD310-A311 Database Development and Use
# November 27, 2024
# Source Forta, B. (n.d.). Sams Teach Yourself SQL in 10 Minutes, Fifth Edition. Retrieved from https://platform.virdocs.com/read/1347763/23/#/4/2/8/20/12/6,/1:2176,/1:2176


import mysql.connector

try:
    conn = mysql.connector.connect(
        user='movies_user',
        password='popcorn',
        host='localhost',
        database='movies'
    )
    print("Connection successful!")

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Function to display films
    def show_films(cursor, title):
        query = """
        SELECT film_name AS Name, 
               film_director AS Director, 
               genre_name AS Genre, 
               studio_name AS 'Studio Name' 
        FROM film 
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
        """
        cursor.execute(query)
        films = cursor.fetchall()

        print(f"\n-- {title} --")
        for film in films:
            print(f"Film Name: {film[0]}\nDirector: {film[1]}\nGenre Name: {film[2]}\nStudio Name: {film[3]}\n")

    # 1. Show films before any modifications
    show_films(cursor, "DISPLAYING FILMS")

    # 2. Insert a new movie into the film table (adjust the release date if needed)
    # Alter column size for `film_releaseDate` (if not done already)
    alter_query = """
    ALTER TABLE film MODIFY film_releaseDate VARCHAR(10);
    """
    cursor.execute(alter_query)

    # Insert a new movie (ensure film_releaseDate matches the updated format)
    insert_query = """
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
    VALUES ('X-Men', '2000-07-14', 104, 'Bryan Singer', 1, 1);
    """
    cursor.execute(insert_query)
    conn.commit()

    # Show films after insert
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # 3. Update a film (e.g., changing Alien to Horror)
    update_query = """
    UPDATE film
    SET film_name = 'Alien', genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
    WHERE film_name = 'Alien';
    """
    cursor.execute(update_query)
    conn.commit()

    # Show films after update
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # 4. Delete a movie (e.g., Gladiator)
    delete_query = """
    DELETE FROM film WHERE film_name = 'Gladiator';
    """
    cursor.execute(delete_query)
    conn.commit()

    # Show films after delete
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Ensure the connection is closed properly
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Connection closed.")




