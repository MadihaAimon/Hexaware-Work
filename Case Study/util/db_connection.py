import mysql.connector


def get_connection():
    # Read the properties from the file
       try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root",
            port='3306',
            database=" virtualartgallery"
        )
        return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None
