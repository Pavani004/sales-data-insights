import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import os

# ------------------ DB Connection ------------------
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="6304",
        database="sales_data"
    )
    cursor = conn.cursor()
    print("✅ Connected to MySQL database")
except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
    exit()

# ------------------ Table Creation (if not exists) ------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    price FLOAT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    sale_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
""")
conn.commit()
print("✅ Tables verified/created")

# ------------------ Load CSVs ------------------
try:
    customers_df = pd.read_csv("data/customers.csv")
    products_df = pd.read_csv("data/products.csv")
    sales_df = pd.read_csv("data/sales.csv")
    print("✅ CSVs loaded")
except Exception as e:
    print(f"❌ CSV Load Error: {e}")
    exit()

# ------------------ Clear Old Data ------------------
cursor.execute("DELETE FROM sales")
cursor.execute("DELETE FROM customers")
cursor.execute("DELETE FROM products")
conn.commit()
print("🧹 Old data cleared")

# ------------------ Insert Data ------------------
for _, row in customers_df.iterrows():
    cursor.execute(
        "INSERT INTO customers (customer_id, name, location) VALUES (%s, %s, %s)",
        (row['customer_id'], row['name'], row['location'])
    )

for _, row in products_df.iterrows():
    cursor.execute(
        "INSERT INTO products (product_id, name, price) VALUES (%s, %s, %s)",
        (row['product_id'], row['name'], row['price'])
    )

for _, row in sales_df.iterrows():
    cursor.execute(
        "INSERT INTO sales (sale_id, customer_id, product_id, quantity, sale_date) VALUES (%s, %s, %s, %s, %s)",
        (row['sale_id'], row['customer_id'], row['product_id'], row['quantity'], row['sale_date'])
    )

conn.commit()
print("✅ Data inserted into database")

# ------------------ Perform Analysis ------------------
query = """
SELECT
    s.sale_id,
    c.name AS customer_name,
    c.location,
    p.name AS product_name,
    p.price,
    s.quantity,
    s.sale_date,
    (p.price * s.quantity) AS total_sale
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id;
"""

df = pd.read_sql(query, conn)

# ------------------ Analysis Outputs ------------------
print("\n📦 SALES DATA")
print(df)

print("\n📈 Total Sales by Product:")
print(df.groupby('product_name')['total_sale'].sum())

print("\n👥 Total Sales by Customer:")
print(df.groupby('customer_name')['total_sale'].sum())

print("\n📅 Sales Summary by Date:")
print(df.groupby('sale_date')['total_sale'].sum())

# ------------------ Visualization ------------------
plt.figure(figsize=(8,5))
df.groupby("product_name")["total_sale"].sum().plot(kind="bar", color='skyblue', edgecolor='black')
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# ------------------ Close Connection ------------------
cursor.close()
conn.close()
print("✅ Connection closed")
