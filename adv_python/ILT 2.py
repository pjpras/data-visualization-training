'''
1. Suppose you have a dataset containing daily temperature readings for a city, and you

want to identify days with extreme temperature conditions. Find days where the

temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees

Celsius (cold day).

Input:

temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
'''
import numpy as np
import pandas as pd
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

print("Hot Days:")
print("Day   temperatures")
for i in range(len(temperatures)):
    if temperatures[i] > 35:
        print(f"{i+1}     {temperatures[i]}")
print("\nCold Days:")
print("Day   temperatures")
for i in range(len(temperatures)):
    if temperatures[i] < 5:
        print(f"{i+1}     {temperatures[i]}")
        
        
'''
2. Suppose you have a dataset containing monthly sales data for a company, and you

want to split this data into quarterly reports for analysis and reporting purposes.

Input:

monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
'''
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
quarterly_sales = monthly_sales.reshape(4, 3)

for i in range(len(quarterly_sales)):
    print(f"Quarter {i+1} Sales (in thousands of dollars):\n{quarterly_sales[i]}")
    

'''
3. Suppose you have a dataset containing customer data, and you want to split this data

into two groups: one group for customers who made a purchase in the last 30 days and

another group for customers who haven't made a purchase in the last 30 days.

Input:

customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])

last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
'''
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
print("Active Customers (Last Purchase) <= 30 days ago")
print(customer_ids[last_purchase_days_ago <= 30])

print("Inactive Customers (Last Purchase) > 30 days ago")
print(customer_ids[last_purchase_days_ago > 30])


'''
4.Suppose you have two sets of employee data—one containing information about

full-time employees and another containing information about part-time employees. You

want to combine this data to create a comprehensive employee dataset for HR analysis.
'''
# Employee data for full-time employees
full_time_employees = np.array([
[101, 'John Doe', 'Full-Time', 55000],
[102, 'Jane Smith', 'Full-Time', 60000],
[103, 'Mike Johnson', 'Full-Time', 52000]
])
# Employee data for part-time employees
part_time_employees = np.array([
[201, 'Alice Brown', 'Part-Time', 25000],
[202, 'Bob Wilson', 'Part-Time', 28000],
[203, 'Emily Davis', 'Part-Time', 22000]
])

print('Combined Employee Data:')
for employee in full_time_employees:
    print(f'Employee ID: {employee[0]}, Name: {employee[1]}, Type: {employee[2]}, Salary: {employee[3]}')
for employee in part_time_employees:
    print(f'Employee ID: {employee[0]}, Name: {employee[1]}, Type: {employee[2]}, Salary: {employee[3]}')


#Assignment:

'''
1. How to find the mean of every NumPy array in the given list?

Input:

list = [

np.array([3, 2, 8, 9]),

np.array([4, 12, 34, 25, 78]),

np.array([23, 12, 67])

]
'''
list1 = [
np.array([3, 2, 8, 9]),
np.array([4, 12, 34, 25, 78]),
np.array([23, 12, 67])
]
mean  = [np.mean(i) for i in list1]
print('Mean of Each array\n',mean)


'''
2. Compute the median of the flattened NumPy array

Input: x_odd = np.array([1, 2, 3, 4, 5, 6, 7])
'''
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])
print('Printing the Original array:\n',x_odd)
print('Median of the array that contain odd no of elements\n',np.median(x_odd))


'''
3.Compute the standard deviation of the NumPy array

Input: arr = [20, 2, 7, 1, 34]
'''
arr = [20, 2, 7, 1, 34]
print('arr :',arr)  
print('std of arr :',np.std(arr))


'''
4.Suppose you have a CSV file named 'house_prices.csv' with price information, and

you want to perform the following operations:

● 1.Read the data from the CSV file into a NumPy array.

● 2.Calculate the average of house prices.

● 3.Identify house price above the average.

● 4.Save the list of high prices to a new CSV file.

Note: Download 'house_prices.csv' file from LMS
'''
import pandas as pd

data = pd.read_csv('house_prices.csv')
house_prices = data['price'].values

average_price = np.mean(house_prices)

high_prices = house_prices[house_prices > average_price]

high_prices_df = pd.DataFrame(high_prices, columns=['price'])
high_prices_df.to_csv('high_prices.csv', index=False)

