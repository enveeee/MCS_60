import pandas as pd
import numpy as np

# Step 1: Create a sample dataset with null values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', np.nan],
    'Age': [24, np.nan, 22, 32, 29, 27],
    'City': ['New York', 'Los Angeles', 'Chicago', np.nan, 'Houston', 'Phoenix'],
    'Salary': [70000, 80000, np.nan, 54000, 62000, 67000]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)
print("Original Dataset with Null Values:")
print(df)

# Step 2: Find all null values in the dataset
print("\nNull Values in Each Column:")
print(df.isnull().sum())

# Step 3: Remove rows with any null values
df_cleaned = df.dropna()
print("\nDataset after Removing Rows with Null Values:")
print(df_cleaned)
