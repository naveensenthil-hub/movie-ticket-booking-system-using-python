from src.database import connect


class Admin:

    def add_movie(self, title, genre, duration, price):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO movies(title, genre, duration, price)
        VALUES (?, ?, ?, ?)
        """, (title, genre, duration, price))

        conn.commit()
        conn.close()

        print("Movie added successfully!")

    def view_movies(self):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM movies")

        movies = cursor.fetchall()

        conn.close()

        return movies