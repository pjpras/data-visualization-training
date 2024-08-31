import pandas as pd
import numpy as np

"""
Lab1: Write a Pandas program to detect missing values of a given DataFrame.
"""

df = pd.DataFrame({
    'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],
    'salesman_id': [5002, 5003, 5001, np.nan, 5002, 5001, 5001, np.nan, 5003, 5002, 5003, np.nan]
})

missing_values = df.isnull()
print("Lab1: Missing Values Detection")
print(missing_values)
print()

"""
Lab2: Write a Pandas program to drop the rows where at least one element is missing in a given DataFrame.
"""

df_dropped_any = df.dropna()
print("Lab2: Drop Rows with At Least One Missing Value")
print(df_dropped_any)
print()

"""
Lab3: Write a Pandas program to drop the rows where all elements are missing in a given DataFrame.
"""

df_all_missing = pd.DataFrame({
    'ord_no': [np.nan, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
    'purch_amt': [np.nan, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': [np.nan, '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [np.nan, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001]
})

df_dropped_all = df_all_missing.dropna(how='all')
print("Lab3: Drop Rows Where All Elements Are Missing")
print(df_dropped_all)
print()

"""
Lab4: Write a Pandas program to drop those rows from a given DataFrame in which specific columns have missing values.
"""

df_specific_columns = pd.DataFrame({
    'ord_no': [np.nan, np.nan, 70002, np.nan, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, np.nan],
    'purch_amt': [np.nan, 270.65, 65.26, np.nan, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, np.nan],
    'ord_date': [np.nan, '2012-09-10', np.nan, np.nan, '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', np.nan],
    'customer_id': [np.nan, 3001, 3001, np.nan, 3002, 3001, 3001, 3004, 3003, 3002, 3001, np.nan]
})

df_dropped_specific = df_specific_columns.dropna(subset=['ord_no', 'purch_amt'])
print("Lab4: Drop Rows Where Specific Columns Have Missing Values")
print(df_dropped_specific)
