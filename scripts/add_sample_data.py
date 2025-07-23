import mysql.connector
from db_config import get_connection

# Sample Data
customers = [
    (2, 'Ravi', 'ravi@example.com', 'Delhi'),
    (3, 'Sneha', 'sneha@example.com', 'Bangalore'),
    (4, 'Aarav', 'aarav@example.com', 'Mumbai')
]

products = [
    (2, 'Pen', 10),
    (3, 'Pencil', 5),
    (4, 'Eraser', 7)
]

sales = [
    (2, 2, 2, 5, '2025-07-23'),  # Ravi bought 5 Pens
    (3, 3, 3, 10, '2025-07-23'), # Sneha bought 10 Pencils
    (4, 4, 4, 3, '2025-07-24')   # Aarav bought 3 Erasers
]

def insert_data():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Insert into customers
        cursor.executemany("""
            INSERT INTO customers (customer_id, name, email, location)
            VALUES (%s, %s, %s, %s)
        """, customers)

        # Insert into products
        cursor.executemany("""
            INSERT INTO products (product_id, name, price)
            VALUES (%s, %s, %s)
        """, products)

        # Insert into sales
        cursor.executemany("""
            INSERT INTO sales (sale_id, customer_id, product_id, quantity, sale_date)
            VALUES (%s, %s, %s, %s, %s)
        """, sales)

        conn.commit()
        print("✅ Sample data inserted successfully.")

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    insert_data()
