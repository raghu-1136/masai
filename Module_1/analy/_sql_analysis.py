import sqlite3
import pandas as pd

data = {
    "order_id": ["O1","O2","O3","O4","O5","O6","O7","O8","O9","O10"],
    "city": ["Bangalore","Bangalore","Delhi","Delhi","Mumbai","Mumbai",
              "Bangalore","Delhi","Mumbai","Chennai"],
    "category": ["Furniture","Technology","Furniture","Office Supplies",
                  "Technology","Furniture","Office Supplies","Technology",
                  "Office Supplies","Technology"],
    "sales": [12000,18000,9000,6000,15000,7000,5000,11000,4000,8000],
    "profit": [1800,3600,900,1200,2700,700,1000,2200,800,1600]
}
df = pd.DataFrame(data)

# Step 1: Build a multi-value pivot table aggregating sales and profit by city and category
pivot = pivot_table(
        df,
        values=('profit','sales')  ,
        index ='city'  ,
        columns='category' ,
        aggfunc='sum' ,
        fill_value= 0
        )
# Step 2: Flatten the multi-level column headers into underscore-joined strings
flat_cols = ["_".join(col).strip() for col in pivot.columns.tolist()]
pivot.columns = flat_cols
print(pivot)
# Step 3: Load data into SQLite and query cities with total sales > 25000
conn = sqlite3.connect(":memory:")
df.to_sql("orders",conn, if_exists="replace",index=False)
def sql(query):
    return pd.read_sql_query(query,conn)

print(sql("""SELECT city , SUM(sales) as total_sales
    FROM orders 
    GROUP BY city
    HAVING SUM(sales) > 25000
    ORDER BY total_sales DESC"""))
