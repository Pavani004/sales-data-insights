import mysql.connector

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="6304",  # Your MySQL password
            database="sales_data"
        )
        return conn
    except mysql.connector.Error as e:
        print("❌ MySQL Connection Failed:", e)
        return None
