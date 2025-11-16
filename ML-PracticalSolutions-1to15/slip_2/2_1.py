# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv('house_data.csv')  # Replace with your actual dataset path

# Step 2: Check the column names to verify the structure of the dataset
print("Columns in the dataset:", df.columns)

# Step 3: Check the first few rows of the dataset to verify its structure
print("\nFirst few rows of the dataset:")
print(df.head())

# Step 4: Check for null values in the dataset
print("\nChecking for null values in the dataset:")
print(df.isnull().sum())

# Step 5: Remove rows with null values
df_cleaned = df.dropna()

# Step 6: Verify that there are no more null values
print("\nNull values after cleaning:")
print(df_cleaned.isnull().sum())

# Step 7: Check columns of the cleaned DataFrame
print("\nColumns in the cleaned DataFrame:")
print(df_cleaned.columns)

# Step 8: Ensure correct column names and assign features (X) and target (y)
# Use the correct column names based on the output of the previous print statement
X = df_cleaned[['sqft_above']]  # Adjust to the correct column name if necessary
y = df_cleaned['price']  # Adjust to the correct target column name if necessary

# Step 9: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 10: Train a Simple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 11: Make predictions using the trained model
y_pred = model.predict(X_test)

# Step 12: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("\nMean Squared Error (MSE):", mse)

# Step 13: Plot the results
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')  # Actual house prices
plt.plot(X_test, y_pred, color='red', label='Predicted Prices')  # Predicted prices by the model
plt.title('Simple Linear Regression - House Price Prediction')
plt.xlabel('sqft_above')
plt.ylabel('price')
plt.legend()
plt.show()
