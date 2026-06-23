import pandas as pd
import numpy as np

def clean_orders(df):
    # Step 1: Record original shape
    original_shape = df.shape

    # Step 2: Drop columns with >= 70% missing 
    threshold = (df.isnull().sum() / len(df)) * 100
    n = 70
    df.dropna(thresh = len(df) * (1 - n/100),axis =1, inplace = True)
    
    # Step 3: Remove fully duplicate rows 
    dp = df.duplicated().sum()
    df.drop_duplicates(inplace=True)

    # Step 4: Impute CustomerAge with median 
    ms = df['CustomerAge'].isnull().sum()
    median = df.loc[df['CustomerAge']<100, 'CustomerAge'].median()
    df.loc[df.CustomerAge > 100, 'CustomerAge'] = median
    df['CustomerAge'].fillna(median,inplace = True)
    
    # Step 5: Impute Region with mode 
    ms_md = df['Region'].isnull().sum()
    mode_ = df['Region'].mode()[0]
    df["Region"].fillna(mode_,inplace = True)

    # Step 6: Impute OrderValue with median 
    ms = df['OrderValue'].isnull().sum()
    median_O = df['OrderValue'].median()
    df["OrderValue"].fillna(median_O,inplace = True)
    
    # Step 7: Print summary 
     print("Orginal Shape : ",original_shape)
    for col in threshold[threshold >= n].index:
        print(f"Dropped column '{col}': {threshold[col]:.2f}% missing (>= {n}% threshold)")
    print(f"field \"CustomerAge\"({ms} missing) with median : {median}") 
    print(f"field \"Region\"({ms_md} missing) with mode : {mode_}") 
    print(f"field \"OrderValue\"({ms} missing) with median : {median_O}") 
    print("Final Shape : ", df.shape)
    return df

if __name__ == "__main__":
    data = {
        'OrderID':     [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1002],
        'CustomerAge': [25.0, None, 34.0, None, 45.0, 28.0, 900.0, None],
        'Region':      ['North', 'South', None, 'East', 'South', None, 'North', 'South'],
        'OrderValue':  [150.0, 200.0, 180.0, None, 210.0, 175.0, 190.0, 200.0],
        'PromoCode':   [None, None, None, None, None, None, None, None],
    }
    df = pd.DataFrame(data)
    clean_orders(df)
