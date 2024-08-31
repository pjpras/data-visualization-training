import pandas as pd

"""
Lab1: Suppose you are a teacher, and you want to analyze the exam scores of your students in a particular subject. 
You have recorded the scores of your students for a recent exam, and you want to represent this data using a Pandas Series.
"""

students = ['Alice', 'Bob', 'Charlie', 'David',
            'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]
exam_scores_series = pd.Series(exam_scores, index=students, name='Exam Scores')

print("Lab1: Exam Scores")
print(exam_scores_series)
print()

"""
Lab2: Suppose you want to track and analyze your household expenses for a month. 
You have recorded the expenses for various categories, such as groceries, utilities, rent, transportation, and entertainment. 
You can represent this expense data using a Pandas Series.
"""

categories = ['Groceries', 'Utilities',
              'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]
expenses_series = pd.Series(
    expenses, index=categories, name='Monthly Expenses')

print("Lab2: Household Expenses")
print(expenses_series)
print()

"""
Lab3: Suppose you want to track and analyze the monthly energy consumption in your home. 
You have recorded the monthly energy usage for electricity and gas over a year, and you want to represent this data using Pandas Series.
"""

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
electricity_usage = [350, 320, 310, 330,
                     340, 370, 380, 360, 350, 330, 320, 330]
gas_usage = [20, 18, 16, 15, 12, 10, 8, 9, 12, 15, 17, 19]
electricity_series = pd.Series(
    electricity_usage, index=months, name='Electricity Usage (kWh)')
gas_series = pd.Series(gas_usage, index=months, name='Gas Usage (therms)')

print("Lab3: Monthly Energy Consumption")
print(electricity_series)
print()
print("Monthly Gas Consumption")
print(gas_series)
print()

"""
Lab4: Suppose you are managing a website and want to analyze the monthly revenue generated from advertising. 
You have recorded the monthly revenue for the past year, and you want to represent this data using a Pandas Series.
"""

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
revenue = [5000, 5200, 4800, 5400, 5600,
           5800, 6100, 5900, 6200, 6500, 7000, 6900]
revenue_series = pd.Series(revenue, index=months,
                           name='Advertising Revenue (USD)')

print("Lab4: Monthly Advertising Revenue")
print(revenue_series)
