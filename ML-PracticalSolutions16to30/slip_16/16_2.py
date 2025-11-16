import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load California Housing Dataset
housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['MedHouseVal'] = housing.target  # Target column (similar to 'PRICE')

# Selecting the feature 'AveRooms' (average number of rooms per household)
X = df[['AveRooms']]
y = df['MedHouseVal']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Apply Polynomial Features transformation (e.g., degree 2 for quadratic relationship)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Initialize and train the Polynomial Regression model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Predict on test set
y_pred = model.predict(X_test_poly)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Polynomial Regression Model Evaluation:")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# Plotting the Polynomial Regression fit
plt.scatter(X, y, color='blue', label='Data Points')
X_fit = pd.DataFrame(np.linspace(X.min(), X.max(), 100), columns=['AveRooms'])
X_fit_poly = poly.transform(X_fit)
y_fit = model.predict(X_fit_poly)
plt.plot(X_fit, y_fit, color='red', label='Polynomial Fit (Degree 2)')
plt.xlabel("Average number of rooms per household (AveRooms)")
plt.ylabel("Median House Value (MedHouseVal)")
plt.title("Polynomial Regression Fit for California Housing Data")
plt.legend()
plt.show()
