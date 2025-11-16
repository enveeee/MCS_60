# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
data = pd.read_csv("1Salary_positions.csv")

# Separate features and target variable
X = data[['Level']].values  # Independent variable (Level)
y = data['Salary'].values   # Dependent variable (Salary)

# Fit Simple Linear Regression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fit Polynomial Linear Regression (degree=4 for more flexibility)
poly_features = PolynomialFeatures(degree=4)
X_poly = poly_features.fit_transform(X)
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)

# Predictions for the dataset using both models
y_pred_linear = lin_reg.predict(X)
y_pred_poly = poly_reg.predict(X_poly)

# Calculate the accuracy of both models using R² and Mean Squared Error (MSE)
r2_linear = r2_score(y, y_pred_linear)
mse_linear = mean_squared_error(y, y_pred_linear)
r2_poly = r2_score(y, y_pred_poly)
mse_poly = mean_squared_error(y, y_pred_poly)

# Print model accuracy
print("Simple Linear Regression R²:", r2_linear)
print("Simple Linear Regression MSE:", mse_linear)
print("Polynomial Regression R²:", r2_poly)
print("Polynomial Regression MSE:", mse_poly)

# Predicting salaries for Level 11 and Level 12
level_11 = np.array([[11]])
level_12 = np.array([[12]])

# Simple Linear Regression predictions
salary_11_linear = lin_reg.predict(level_11)
salary_12_linear = lin_reg.predict(level_12)

# Polynomial Regression predictions
salary_11_poly = poly_reg.predict(poly_features.transform(level_11))
salary_12_poly = poly_reg.predict(poly_features.transform(level_12))

# Print predictions
print(f"Predicted salary for level 11 (Simple Linear Regression): {salary_11_linear[0]}")
print(f"Predicted salary for level 12 (Simple Linear Regression): {salary_12_linear[0]}")
print(f"Predicted salary for level 11 (Polynomial Regression): {salary_11_poly[0]}")
print(f"Predicted salary for level 12 (Polynomial Regression): {salary_12_poly[0]}")

# Visualization of both models
plt.scatter(X, y, color='red', label='Actual Salaries')
plt.plot(X, y_pred_linear, color='blue', label='Simple Linear Regression')
plt.plot(X, y_pred_poly, color='green', label='Polynomial Regression')
plt.xlabel("Employee Level")
plt.ylabel("Salary")
plt.legend()
plt.title("Simple Linear vs Polynomial Regression")
plt.show()
