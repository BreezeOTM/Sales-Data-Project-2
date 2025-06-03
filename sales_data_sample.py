import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("C:/Users/Keanu/Downloads/sales_data_sample.db")

# SQL query
query = """
SELECT 
    "CUSTOMER NAME" AS CUSTOMER,
    COUNTRY,
    SUM(CAST(REPLACE(SALES, '$', '') AS FLOAT)) AS TOTAL_SALES
FROM 
    sales_data_sample
GROUP BY 
    "CUSTOMER NAME", COUNTRY
ORDER BY 
    TOTAL_SALES DESC
LIMIT 20;
"""

# Run query and get data
df = pd.read_sql_query(query, conn)

# Plotting
plt.figure(figsize=(12,6))
plt.bar(df['CUSTOMER'], df['TOTAL_SALES'], color='teal')
plt.xlabel('Customer Name')
plt.ylabel('Total Sales ($)')
plt.title('Top 20 Customers by Total Sales')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

# Close connection
conn.close()
