# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Step 2: Load the dataset
# Replace 'house_data.csv' with your dataset's path
df = pd.read_csv('house_price.csv')

# Step 3: Check the structure of the dataset
print("\nFirst few rows of the dataset:")
print(df.head())

# Step 4: Clean the dataset if needed (e.g., drop missing values)
df = df.dropna()  # Remove rows with missing values

# Step 5: Select independent and dependent variables
# Assuming 'SquareFootage' is the feature and 'Price' is the target
X = df[['SquareFootage']]  # Independent variable (Feature)
y = df['Price']  # Dependent variable (Target)

# Step 6: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Train the Simple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 8: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 9: Evaluate the model using Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print("\nMean Squared Error (MSE):", mse)

# Step 10: Visualize the results
plt.figure(figsize=(8,6))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')  # Actual data points
plt.plot(X_test, y_pred, color='red', label='Predicted Prices')  # Model predictions
plt.title('Simple Linear Regression: House Price Prediction')
plt.xlabel('Square Footage')
plt.ylabel('Price')
plt.legend()
plt.show()
