from db_connect import create_connection

def run_analysis():
    conn = create_connection()
    cursor = conn.cursor()

    print("1. Total Revenue:")
    cursor.execute("""
        SELECT SUM(p.price * s.quantity) AS total_revenue
        FROM sales s
        JOIN products p ON s.product_id = p.product_id
    """)
    print(cursor.fetchone()[0])

    print("\n2. Top Selling Products:")
    cursor.execute("""
        SELECT p.name, SUM(s.quantity) AS total_sold
        FROM sales s
        JOIN products p ON s.product_id = p.product_id
        GROUP BY p.name
        ORDER BY total_sold DESC
        LIMIT 5
    """)
    for row in cursor.fetchall():
        print(row)

    print("\n3. Monthly Sales Trend:")
    cursor.execute("""
        SELECT MONTH(date) AS month, SUM(quantity * price) AS revenue
        FROM sales
        JOIN products ON sales.product_id = products.product_id
        GROUP BY MONTH(date)
    """)
    for row in cursor.fetchall():
        print(f"Month {row[0]}: ₹{row[1]}")

    conn.close()

if __name__ == "__main__":
    run_analysis()
