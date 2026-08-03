import pandas as pd

sample_data = {
    'applicant_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'city': ['Chennai', 'Mumbai', 'Bangalore', 'Delhi', 'Chennai',
             'Mumbai', 'Bangalore', 'Delhi', 'Chennai', 'Mumbai'],
    'education': ['B.Tech', '12th', 'M.Tech', 'PhD', '12th',
                  'B.Tech', 'PhD', 'M.Tech', 'M.Tech', '12th'],
    'income': [45000, 22000, 61000, 72000, 18000, 39000, 85000, 54000, 47000, 21000],
    'approved': [1, 0, 1, 1, 0, 0, 1, 1, 1, 0],
}

def solve(df):
    # Step 1: separate the target column 'approved' into y; keep the rest as x
    # TODO: your code here
    y = df['approved']
    x = df.drop(columns=['approved'])

    # Step 2: ordinal-encode the 'education' column using the ranking
    # 12th=0, B.Tech=1, M.Tech=2, PhD=3
    # TODO: your code here
    education_map = {'12th':0,'B.Tech':1,'M.Tech':2,'PhD':3}
    x['education'] = x['education'].map(education_map)

    # Step 3: one-hot encode the 'city' column, dropping one baseline
    # category (city_Bangalore) to avoid the dummy variable trap
    # TODO: your code here
    x = pd.get_dummies(x, columns=['city'])
    x = x.drop(columns=['city_Bangalore'])

    # Step 4: produce a sequential 80/20 train/test split
    # (first 8 rows train, last 2 rows test)
    # TODO: your code here
    x_train, x_test = x.iloc[:8],x.iloc[8:]
    y_train, y_test = y.iloc[:8],y.iloc[8:]

    return x_train,x_test,y_train,y_test

if __name__ == "__main__":
    df = pd.DataFrame(sample_data)
    x_train, x_test, y_train, y_test = solve(df)
    print("X_train:\n", x_train)
    print("\nX_test:\n", x_test)
    print("\ny_train:\n", y_train)
    print("\ny_test:\n", y_test)
