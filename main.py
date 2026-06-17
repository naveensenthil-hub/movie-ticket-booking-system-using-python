from src import database
from src.admin import Admin
from src.user import User
from src.booking import Booking


def main():
    database.create_tables()

    admin1 = Admin()
    user1 = User()
    booking1 = Booking()

    while True:
        print("\n--- Movie Ticket Booking System ---")
        print("1. Admin - Add Movie")
        print("2. Admin - View Movies")
        print("3. User - Register")
        print("4. User - Login & Book Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            duration = int(input("Enter duration in minutes: "))
            price = float(input("Enter ticket price: "))

            admin1.add_movie(title, genre, duration, price)

        elif choice == '2':
            movies = admin1.view_movies()

            print("\nMovies List")
            for movie in movies:
                print(movie)

        elif choice == '3':
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")

            user1.register(username, email, password)

        elif choice == '4':
            email = input("Enter email: ")
            password = input("Enter password: ")

            logged_user = user1.login(email, password)
            if logged_user:
                print(f"Welcome {logged_user[1]}")

                movies = admin1.view_movies()

                print("\nAvailable Movies")
                for movie in movies:
                    print(movie)

                movie_id = int(input("Enter movie ID: "))
                seats = int(input("Enter number of seats: "))

                booking1.create_booking(logged_user[0], movie_id, seats)

                print("\nYour Bookings")
                bookings = booking1.view_bookings(logged_user[0])

                for booking in bookings:
                    print(booking)

            else:
                print("Invalid login credentials")

        elif choice == '5':
            print("Exiting system")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()