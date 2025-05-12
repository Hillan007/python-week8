import pandas as pd

# Load the dataset
df = pd.read_csv("owid-covid-data.csv")

# View the first few rows
print(df.head())

# Check available columns
print(df.columns)

# Identify missing values
print(df.isnull().sum())