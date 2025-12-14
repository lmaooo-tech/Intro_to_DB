import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Creates the alx_book_store database in MySQL.
    Uses IF NOT EXISTS to prevent errors if database already exists.
    """
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password'  # Change this to your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            cursor.close()
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # Properly close the database connection
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()
