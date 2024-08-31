import pandas as pd

# Assuming salesdata.csv is already available in the working directory
sales_data = pd.read_csv('salesdata.csv')

"""
Lab1: Write a Pandas program to create a Pivot table and find the total sale amount region-wise, manager-wise, and sales man-wise.
"""

# Pivot table to calculate total sale amount region-wise, manager-wise, and salesman-wise
pivot_lab1 = pd.pivot_table(sales_data, values='Sale Amount', index=[
                            'Region', 'Manager', 'SalesMan'], aggfunc='sum')

print("Lab1: Total Sale Amount Region-Wise, Manager-Wise, Sales Man-Wise")
print(pivot_lab1)
print()

"""
Lab2: Write a Pandas program to create a Pivot table and find the item-wise units sold.
"""

# Pivot table to calculate item-wise total units sold
pivot_lab2 = pd.pivot_table(
    sales_data, values='Units Sold', index='Item', aggfunc='sum')

print("Lab2: Item-Wise Units Sold")
print(pivot_lab2)
print()

"""
Lab3: Write a Pandas program to create a Pivot table and find the region-wise, item-wise units sold.
"""

# Pivot table to calculate region-wise, item-wise total units sold
pivot_lab3 = pd.pivot_table(sales_data, values='Units Sold', index=[
                            'Region', 'Item'], aggfunc='sum')

print("Lab3: Region-Wise, Item-Wise Units Sold")
print(pivot_lab3)
print()

"""
Lab4: Write a Pandas program to create a Pivot table and count the manager-wise sales and find the mean value of sale amount.
"""

# Pivot table to count manager-wise sales and calculate mean sale amount
pivot_lab4 = pd.pivot_table(
    sales_data, values='Sale Amount', index='Manager', aggfunc=['count', 'mean'])

print("Lab4: Manager-Wise Sales Count and Mean Sale Amount")
print(pivot_lab4)
