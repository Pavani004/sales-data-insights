# 📊 Sales Data Management and Insights System (Python + MySQL)
This is a comprehensive data engineering project built with:
- **Backend**: Python + Pandas + PyMySQL
- **Database**: MySQL
- **Visualization**: Matplotlib + Seaborn
- **Analytics**: SQL-based insights with automated reporting

---

## ✨ Features
- ✅ Automated CSV data ingestion and processing
- ✅ ETL (Extract-Transform-Load) operations
- ✅ Normalized database schema with foreign key relationships
- ✅ Advanced SQL analytics for business insights
- ✅ Interactive data visualizations and charts
- ✅ Real-time sales trend analysis and KPI reporting

---

## 🛠️ Tech Stack
| Layer         | Technology                  |
|---------------|-----------------------------|
| Backend       | Python 3.x                  |
| Database      | MySQL                       |
| Data Processing| Pandas, NumPy              |
| Visualization | Matplotlib, Seaborn         |
| DB Connectivity| PyMySQL, mysql-connector   |
| Environment   | VS Code, Jupyter Notebook   |

---

## 📁 Folder Structure
```
sales-data-insights/
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── sales.csv
├── scripts/
│   ├── __pycache__/
│   ├── add_sample_data.py
│   ├── analysis_queries.py
│   ├── db_connect.py
│   ├── load_data.py
│   └── visualize.py
├── sql/
│   ├── create_tables.sql
│   └── insert_data.sql
├── requirements.txt
├── sales_data_insights.py
└── README.md
```

---

## 🚀 Getting Started

### 1. Database Setup (MySQL)
- Create database and import schema:
```bash
mysql -u root -p
CREATE DATABASE sales_db;
USE sales_db;
SOURCE sql/create_tables.sql;
```

### 2. Python Environment Setup
```bash
# Clone repository
git clone https://github.com/yourusername/sales-data-insights.git
cd sales-data-insights

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Database Connection
Update credentials in `scripts/db_connect.py`:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username', 
    'password': 'your_password',
    'database': 'sales_db'
}
```

### 4. Load Sample Data & Run Analysis
```bash
# Load CSV data into MySQL
python scripts/load_data.py

# Run main analysis
python sales_data_insights.py
```

Visit generated charts in `/output` folder

---

## ✅ Key Analytics Features

### 📊 Revenue Analytics
- **Total Revenue**: Aggregate sales across all transactions
- **Monthly Trends**: Time-series analysis with seasonal patterns
- **Product Performance**: Best-selling items by quantity and revenue

### 👥 Customer Insights  
- **Top Customers**: Most active buyers by transaction volume
- **Geographic Analysis**: Sales distribution by location
- **Purchase Patterns**: Customer behavior and loyalty metrics

### 📈 Visual Reports
- **Line Charts**: Monthly revenue trends over time
- **Bar Charts**: Top 5 products by sales volume
- **Pie Charts**: Revenue distribution by product categories
- **Heatmaps**: Customer activity and seasonal patterns

---

## 📋 Database Schema

```sql
-- Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10,2) NOT NULL
);

-- Customers Table  
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    location VARCHAR(100)
);

-- Sales Table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    customer_id INT, 
    quantity INT NOT NULL,
    sale_date DATE NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

---

## 🔍 Sample SQL Queries

### Top Revenue Generating Products
```sql
SELECT p.name, SUM(s.quantity * p.price) as total_revenue
FROM sales s 
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_id 
ORDER BY total_revenue DESC 
LIMIT 5;
```

### Monthly Sales Trend
```sql
SELECT DATE_FORMAT(sale_date, '%Y-%m') as month,
       COUNT(*) as transactions,
       SUM(s.quantity * p.price) as monthly_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id  
GROUP BY month
ORDER BY month;
```

---

## 📌 Dependencies
```txt
pandas>=1.3.0
pymysql>=1.0.2
matplotlib>=3.5.0
seaborn>=0.11.0
numpy>=1.21.0
mysql-connector-python>=8.0.0
```

---

## License
MIT
