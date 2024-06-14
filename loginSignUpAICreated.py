import sqlite3
from hashlib import sha256
 
# Constants for our database file and table name
DATABASE_FILE = 'users.db'
TABLE_NAME = 'users'
 
# Establishing a connection with the SQLite database
conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()
 
# Function to create the users table if it does not exist already
def create_users_table():
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )
    ''')
    conn.commit()
 
# Function to create a new user in the database
def create_user(username, password):
    password_hash = sha256(password.encode('utf-8')).hexdigest()  # Hashing the password
    try:
        cursor.execute(f"INSERT INTO {TABLE_NAME} (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
 
# Function to validate a login attempt
def check_login(username, password):
    password_hash = sha256(password.encode('utf-8')).hexdigest()
    cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE username=? AND password_hash=?", (username, password_hash))
    return cursor.fetchone() is not None
 
# Simple CLI to interact with the system
if __name__ == '__main__':
    create_users_table()
    while True:
        print("\nEasy-Log System")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            # Sign-Up logic
            username = input("Enter a new username: ")
            password = input("Enter a new password: ")
            if create_user(username, password):
                print("User created successfully.")
            else:
                print("User creation failed. Username might already be taken.")
        elif choice == '2':
            # Log-In logic
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if check_login(username, password):
                print("Login successful!")
            else:
                print("Login failed. Incorrect username or password.")
        elif choice == '3':
            print("Exiting Easy-Log System.")
            break
        else:
            print("Invalid choice, please try again.")
 
# Closing the database connection
conn.close()
