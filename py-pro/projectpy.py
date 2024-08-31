# Step 1: Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Loading the dataset
data_path = 'imdb-movies.csv'
df = pd.read_csv(data_path)

# Step 3: Exploring the dataset
print("Dataset Overview:")
print(df.info())
print("\nFirst few rows of the dataset:")
print(df.head())