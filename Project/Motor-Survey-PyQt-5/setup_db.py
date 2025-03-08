import os
import sqlite3
from hashlib import sha256

basedir = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(basedir, 'motor_survey.db')

def initialize_database():
    """Create database structure and default admin user"""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            # Create users table
            conn.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT NOT NULL,
                salt TEXT NOT NULL
            )''')
            
            # Create default admin user
            salt = os.urandom(16).hex()
            password = "admin123"  # Default password
            hashed_pw = sha256((password + salt).encode()).hexdigest()
            
            conn.execute('''INSERT OR IGNORE INTO users 
                          (username, password, salt)
                          VALUES (?, ?, ?)''',
                          ('admin', hashed_pw, salt))
            
            print("Database initialized successfully!")
            print("Default admin credentials:")
            print(f"Username: admin\nPassword: admin123")
            
    except Exception as e:
        print(f"Error initializing database: {str(e)}")
        exit(1)

if __name__ == '__main__':
    initialize_database()