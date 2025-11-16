# This file uses the pre-made 1your_dataset.csv file
# and it displays the cleaned_dataset.csv file after identifying NULL Values.

import pandas as pd

# Load the dataset (replace 'your_dataset.csv' with your actual file)
data = pd.read_csv("1your_dataset.csv")

# Display columns with null values and count of null values
print("Null values in each column before removing:")
print(data.isnull().sum())

# Remove rows with any null values
data_cleaned = data.dropna()

# Display columns with null values and count of null values after removing
print("\nNull values in each column after removing:")
print(data_cleaned.isnull().sum())

# Display the number of rows before and after removing nulls
print(f"\nNumber of rows before removing nulls: {len(data)}")
print(f"Number of rows after removing nulls: {len(data_cleaned)}")

# Save the cleaned dataset if needed
data_cleaned.to_csv("cleaned_dataset.csv", index=True)
