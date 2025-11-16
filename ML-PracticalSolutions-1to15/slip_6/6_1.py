import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the California housing dataset
housing = fetch_california_housing()

# Convert to a DataFrame for better visualization and manipulation
df = pd.DataFrame(housing.data, columns=housing.feature_names)

# Add the target variable (house prices) to the DataFrame
df['PRICE'] = housing.target

# Display the first few rows of the dataset
print(df.head())

# Features (X) and target (y)
X = df.drop('PRICE', axis=1)  # Drop the target column to get features
y = df['PRICE']  # Target variable (house prices)

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create PolynomialFeatures object (degree 2 for simplicity)
poly = PolynomialFeatures(degree=2)

# Transform the features into polynomial features
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Train the Linear Regression model on the transformed features
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_poly)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Plot the actual vs predicted house prices
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices (Polynomial Regression)")
plt.show()
