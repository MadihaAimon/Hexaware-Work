import mysql.connector
from mysql.connector import Error
from datetime import datetime


def create_connection():
    try:
        connect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root",
            port='3306',
            database="petpals"
        )
        return connect
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None
def display_pet_listings():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM pets")
            pets = cursor.fetchall()

            print("Available Pets:")
            for pet in pets:
                print(f"{pet[1]} - Age: {pet[2]}, Breed: {pet[3]}")

        except Error as e:
            print(f"Error retrieving pet listings: {e}")
        finally:
            connection.close()
display_pet_listings()

donation_counter = 10
def generate_donation_number():
    global donation_counter
    donation_counter += 1
    return donation_counter

def record_cash_donation():
    connection = create_connection()
    if connection:
        try:
            donation_number=generate_donation_number()
            donor_name = input("Enter donor name: ")
            amount = float(input("Enter donation amount: "))
            donation_date = datetime.now().strftime("%Y-%m-%d")

            cursor = connection.cursor()
            cursor.execute("INSERT INTO donations (donationid, donorname, donationamount, donationdate) VALUES (%s, %s, %s, %s)",
                           (donation_number,donor_name, amount, donation_date))
            connection.commit()

            print("Donation recorded successfully!")

        except (Error, ValueError) as e:
            print(f"Error recording donation: {e}")
        finally:
            connection.close()
record_cash_donation() 