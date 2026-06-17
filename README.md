# movie-ticket-booking-system-using-python
# Hi, I'm Naveen S! 👋
A Python and MySQL-based Movie Ticket Booking System that enables users to browse movies, view show timings, select seats, and book tickets efficiently. The system provides a seamless booking experience while securely storing user and booking information in a MySQL database.
🚀 Features
- User Registration and Login
- Browse Available Movies
- View Show Timings
- Seat Selection and Ticket Booking
- Booking Confirmation
- Ticket Cancellation
- Booking History Management
- Admin Management for Movies and Shows
- Secure MySQL Database Integration

🛠️ Tech Stack

- Python
- MySQL
- MySQL Connector
- SQL
- Tkinter (GUI) / Console Interface

📋 System Modules

User Module
- User Registration
- User Login
- Profile Management

Movie Module
- Display Available Movies
- Show Movie Details
- Show Timings

Booking Module
- Select Movie
- Choose Seats
- Confirm Booking
- Generate Booking Details

Admin Module
- Add Movies
- Update Movie Information
- Delete Movies
- Manage Show Timings

🗄️ Database

The project uses MySQL to manage:

- User Information
- Movie Details
- Show Timings
- Booking Records
- Seat Availability

 ⚙️ Installation
1. Clone the repository

bash
git clone https://github.com/your-username/movie-ticket-booking-system.git

2. Navigate to the project directory

bash
cd movie-ticket-booking-system

3. Install required packages

bash
pip install mysql-connector-python

4. Create a MySQL database
sql
CREATE DATABASE movie_booking;

5. Import the database file
bash
mysql -u root -p movie_booking < database.sql

7. Configure MySQL credentials in the project files.

8. Run the application
bash
python main.py

📂 Project Structure
text
Movie-Ticket-Booking-System
│
├── main.py
├── login.py
├── booking.py
├── admin.py
├── database.py
├── database.sql
├── requirements.txt
└── README.md


⭐ If you found this project useful, consider giving it a star on GitHub.
