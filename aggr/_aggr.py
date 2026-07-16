import pandas as pd

data = {
    'order_id': ['O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8'],
    'city':     ['Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi', 'Mumbai', 'Delhi', 'Bangalore'],
    'category': ['Tech', 'Furniture', 'Furniture', 'Office', 'Office', 'Tech', 'Tech', 'Tech'],
    'sales':    [15000, 8000, 12000, 3000, 5500, 25000, 32000, 18000],
    'profit':   [3000, -500, 1500, 200, 800, 5000, 7000, 2500],
    'status':   ['Completed', 'Completed', 'Cancelled', 'Completed', 'Completed', 'Completed', 'Completed', 'Cancelled']
}
df = pd.DataFrame(data)

# Task 1: Filter to Completed and non-Furniture
filtered = df[(df['status'] == 'Completed') & (~df['category'].isin(['Furniture']))]  # TODO: combine two conditions with & and ~isin

# Task 2: Named aggregation grouped by city
result = filtered.groupby('city').agg(
        total_sales = ('sales','sum'),
        avg_profit  = ('profit','mean'),
        order_count = ('order_id','count')
        )
print(result)

# Task 3: Add city_avg_sales to original df
df['city_avg_sales'] = df.groupby('city')['sales'].transform('mean')
# TODO: use groupby + transform('mean')

# Task 4: Fill NaN and print first 3 rows
df['city_avg_sales'] = df['city_avg_sales'].fillna(df['city_avg_sales'].mean())  # TODO
print(df.head(3))
