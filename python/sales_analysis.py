import pandas as pd

df = pd.read_csv("../data/Sample - Superstore.csv", encoding="latin1")

print("=" * 50)
print("BUSINESS SUMMARY")
print("=" * 50)

print(f"Total Sales: ${df['Sales'].sum():,.2f}")
print(f"Total Profit: ${df['Profit'].sum():,.2f}")
print(f"Total Orders: {df['Order ID'].nunique()}")
print(f"Total Customers: {df['Customer ID'].nunique()}")

print("\nTOP CATEGORIES BY SALES")
print(df.groupby('Category')['Sales'].sum().sort_values(ascending=False))

print("\nSALES BY REGION")
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))

print("\nTOP 10 PRODUCTS BY SALES")
print(df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10))
import matplotlib.pyplot as plt

category_sales = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind='bar')

plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')

plt.tight_layout()
plt.savefig('../screenshots/category_sales.png')

plt.show()
profit_by_category = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(8,5))
profit_by_category.plot(kind='bar')

plt.title('Profit by Category')
plt.xlabel('Category')
plt.ylabel('Profit')

plt.tight_layout()
plt.savefig('../screenshots/profit_by_category.png')

plt.show()
# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Monthly Sales Trend
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()

import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
monthly_sales.plot()

plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')

plt.tight_layout()
plt.savefig('../screenshots/monthly_sales_trend.png')
plt.show()
print("\nTOP 10 CUSTOMERS BY SALES")

top_customers = df.groupby('Customer Name')['Sales'].sum()\
                  .sort_values(ascending=False)\
                  .head(10)

print(top_customers)
print("\nAVERAGE PROFIT BY DISCOUNT")

discount_profit = df.groupby('Discount')['Profit'].mean()

print(discount_profit)