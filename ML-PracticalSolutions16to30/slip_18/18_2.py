import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Step 1: Load the dataset (Assuming the dataset is in the current directory)
df = pd.read_csv("Salary_positions.csv")

# Step 2: Extract the features (X) and target (y)
X = df[['Position_Level']].values  # Features: Level (reshaped to 2D)
y = df['Salary'].values  # Target: Salary

# Step 3: Create a PolynomialFeatures object for degree 4 (you can experiment with degree)
poly = PolynomialFeatures(degree=4)

# Step 4: Transform the feature into higher-degree polynomial features
X_poly = poly.fit_transform(X)

# Step 5: Fit the polynomial regression model
poly_regressor = LinearRegression()
poly_regressor.fit(X_poly, y)

# Step 6: Make predictions using the model
y_pred = poly_regressor.predict(X_poly)

# Step 7: Visualize the polynomial regression results
plt.scatter(X, y, color='red')  # Original data points
plt.plot(X, y_pred, color='blue')  # Polynomial regression line
plt.title("Polynomial Linear Regression for Salary Prediction")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

# Step 8: Predict salary for Level 11 and Level 12
level_11 = poly.transform([[11]])  # Transform level 11 to polynomial features
level_12 = poly.transform([[12]])  # Transform level 12 to polynomial features

predicted_salary_11 = poly_regressor.predict(level_11)
predicted_salary_12 = poly_regressor.predict(level_12)

print(f"Predicted salary for Level 11: ${predicted_salary_11[0]:,.2f}")
print(f"Predicted salary for Level 12: ${predicted_salary_12[0]:,.2f}")
