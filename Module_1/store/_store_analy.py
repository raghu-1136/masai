import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


data = {
    "order_id": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    "sales":[250.00,80.00,620.00,35.00,90.00,410.00,45.00,150.00,900.00,60.00],
    "profit":[45.00,-12.00,120.00,10.00,-30.00,60.00,8.00,-25.00,180.00,15.00],
    "discount":[0.10,0.40,0.05,0.00,0.50,0.15,0.00,0.45,0.10,0.05],
    "quantity":[3,2,5,1,4,2,1,3,6,2],
    "category":["Technology","Furniture","Technology","Office Supplies","Furniture","Technology","Office Supplies","Furniture","Technology","Office Supplies"]
}

def load_data():
    # TODO: build a DataFrame from the inlined sample rows
    return pd.DataFrame(data)

def summarize_sales(df):
    # TODO: compute mean, median, and determine right/left skew
    
   
    fig, ax = plt.subplots(figsize=(20, 7))
    fig.suptitle('Step 6 — Histogram: Distribution Shape', fontsize=13, fontweight='bold')

# ── sales Distribution ────────────────────────────────────────────
    ax.hist(df['sales'], bins=50, color='steelblue', edgecolor='white', alpha=0.85)
    ax.axvline(df['sales'].median(), color='red', lw=2, ls='--',
                    label=f"Median  ${df['sales'].median():.0f}  ← typical order")
    ax.axvline(df['sales'].mean(),   color='orange', lw=2, ls='--',
                    label=f"Mean    ${df['sales'].mean():.0f}  ← pulled up by big orders")
    ax.set_xlabel('Order sales ($)')
    ax.set_ylabel('Number of Orders')
    ax.legend(fontsize=9)

    print(f"Mean of sales : {df["sales"].mean()}")
    print(f"Median of sales : {df["sales"].median()}")

    if df['sales'].median() < df['sales'].mean():
        ax.set_title(f'sales Distribution (right-skewed: most orders are small, a few are huge)',
                     fontsize=11)
        print("sales is right-skewed, mean > median")
    else:
        ax.set_title(f'sales Distribution (left-skewed: most orders are large, a few are small)',
                     fontsize=11)
        print("sales is left-skewed, median > mean") 

# Annotation pointing to the long right tail
    plt.tight_layout()
    plt.show(block=True)

def count_losses(df):
    # TODO: count rows where profit < 0
    loss = (df['profit']< 0).sum()
    print(f"loss making Orders (profit < 0) ={loss}")

def discount_profit_correlation(df):
    # TODO: compute Pearson correlation between discount and profit
    numeric_cols = ['sales', 'profit', 'discount', 'quantity']

    corr_matrix = df[numeric_cols].corr()

    plt.figure(figsize=(6,5))

    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap='coolwarm',
        fmt=".2f"
    )

    plt.title("Correlation Matrix")

    plt.show()

    corr = df[['discount', 'profit']].corr().loc['discount', 'profit']

    if corr < 0:
        print(f"The Discount-Profit correlation is negative ({corr:.2f}), higher discounts lead to lower profit")
    else:
        print(f"The Discount-Profit correlation is positive ({corr:.2f}), higher discounts lead to higher profit")


if __name__ == "__main__":
    df = load_data()
    summarize_sales(df)
    count_losses(df)
    discount_profit_correlation(df)
