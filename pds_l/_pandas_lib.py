
import pandas as pd
import numpy as np

data = {
    'OrderID':     [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1002],
    'CustomerAge': [25.0, np.nan, 34.0, np.nan, 45.0, 28.0, 900.0, np.nan],
    'Region':      ['North', 'South', np.nan, 'East', 'South', np.nan, 'North', 'South'],
    'OrderValue':  [150.0, 200.0, 180.0, np.nan, 210.0, 175.0, 190.0, 200.0],
    'PromoCode':   [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
}
df = pd.DataFrame(data)

median = df.loc[df['CustomerAge']<100, 'CustomerAge'].median()
df.loc[df.CustomerAge > 100, 'CustomerAge'] = np.nan
df["CustomerAge"].fillna(median,inplace=True)

print(df)

mode_ = df['Region'].mode()[0]
df["Region"].fillna(mode_,inplace = True)

print(df)
