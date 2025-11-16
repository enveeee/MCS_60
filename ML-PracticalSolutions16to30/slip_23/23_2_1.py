import pandas as pd
import numpy as np

# Create a sample dataframe with some null values
data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eva'],
    'Age': [25, np.nan, 29, 40, 35],
    'Department': ['HR', 'Finance', 'IT', np.nan, 'Marketing'],
    'Salary': [50000, 60000, 55000, 65000, np.nan]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("your_dataset.csv", index=False)

print("Sample CSV file 'your_dataset.csv' created with dummy data and null values.")
