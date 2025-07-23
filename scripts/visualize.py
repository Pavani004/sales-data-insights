import pandas as pd
import matplotlib.pyplot as plt
from db_connect import create_connection

def plot_sales_trend():
    conn = create_connection()
    query = """
        SELECT DATE(date) as date, SUM(p.price * s.quantity) as revenue
        FROM sales s
        JOIN products p ON s.product_id = p.product_id
        GROUP BY date
        ORDER BY date
    """
    df = pd.read_sql(query, conn)
    conn.close()

    plt.figure(figsize=(8,5))
    plt.plot(df['date'], df['revenue'], marker='o')
    plt.title("Daily Sales Revenue Trend")
    plt.xlabel("Date")
    plt.ylabel("Revenue (₹)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("daily_sales_trend.png")
    plt.show()

if __name__ == "__main__":
    plot_sales_trend()
