import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
df = pd.read_excel("customer_revenue_analysis.xlsx")

# Show data
print(df.head())

# Total spending per customer
customer_spending = df.groupby("customer_name")["amount"].sum()
print("\nCustomer Spending:\n", customer_spending)

# Top customers
top_customers = customer_spending.sort_values(ascending=False)
print("\nTop Customers:\n", top_customers)

# Revenue by city
city_revenue = df.groupby("city")["amount"].sum()

# Plot graph
city_revenue.plot(kind="bar")
plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.show()