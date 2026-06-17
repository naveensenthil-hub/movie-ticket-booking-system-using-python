from src.database import connect


class Booking:

    def create_booking(self, user_id, movie_id, seats):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO bookings(user_id, movie_id, seats)
        VALUES (?, ?, ?)
        """, (user_id, movie_id, seats))

        conn.commit()
        conn.close()

        print("Booking successful!")

    def view_bookings(self, user_id):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM bookings
        WHERE user_id=?
        """, (user_id,))

        bookings = cursor.fetchall()
        conn.close()
        return bookings