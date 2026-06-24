import pandas as pd

raw_data = {
    'order_id':   [101, 102, 103, 104, 105, 101, 106, 104],
    'item':       ['Orange', 'Banana', 'orange', ' Orange ', 'Mango',
                   'Orange', 'Banana', 'Mango'],
    'price':      ['12.5', '8.0', '12.5', '12.5', 'N/A', '12.5', '8.0', 'error'],
    'notes':      [None, None, None, 'bulk', None, None, None, None],
    'status':     ['ordered', 'ordered', 'shipped', 'ordered',
                   'packed', 'delivered', 'shipped', 'delivered'],
    'event_time': ['2026-01-01', '2026-01-02', '2026-01-01', '2026-01-03',
                   '2026-01-04', '2026-01-05', '2026-01-06', '2026-01-07'],
    'sale_date':  ['2026-01-01', '2026-01-02', '2026-01-01', '2026-01-03',
                   '2026-01-04', '2026-01-05', '2026-01-06', '2026-01-07']
}

df = pd.DataFrame(raw_data)

# Step 1: Drop the notes column
# TODO: drop the column whose null rate exceeds the 30% threshold
threshold = (df.isnull().sum() / len(df)) * 100
n = 30
df.dropna(thresh = len(df) * (1- n/100),axis = 1, inplace =True)
# Step 2: Normalise item and drop near-duplicates
# TODO: lowercase + strip into item_clean, then drop_duplicates on item_clean

df['item'] = df['item'].astype(str).str.strip().str.lower()

df['item_clean'] = df['item'].astype(str).str.strip().str.lower()
df['item_clean'] = df['item_clean'].drop_duplicates()

# Step 3: Convert price to numeric and fill NaN with -1
# TODO: use pd.to_numeric with errors='coerce', then fillna(-1)

df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['price'].fillna(-1, inplace=True)

# Step 4: Convert date strings to datetime
# TODO: convert event_time and sale_date using pd.to_datetime

df['sale_date'] = pd.to_datetime(df['sale_date'])
df['event_time'] = pd.to_datetime(df['event_time'])

# Step 5: Resolve key duplicates (keep latest status per order_id)
# TODO: sort by event_time ascending, then keep='last' per order_id

df.sort_values('event_time', inplace = True)
df.drop_duplicates(subset = 'order_id', keep ='last', inplace = True)

df.sort_values('order_id', inplace = True)
# Task 6: Pandas equivalent of SELECT * WHERE price > 10 ORDER BY price DESC LIMIT 3
# TODO: implement
result_6 = df[df["price"] > 10].sort_values("price", ascending=False).head(3)
# Task 7: Pandas equivalent of SELECT COUNT(*)
result_7 = len(df)  # TODO: implement

print(df)
print("\n")
print("Task 6:", result_6)
print("\n")
print("Task 7:", result_7)
