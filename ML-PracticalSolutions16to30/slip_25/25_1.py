# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Step 1: Load the Dataset (replace with actual file or use a synthetic dataset here)
# If you have a CSV file, load it like this:
# data = pd.read_csv("house_price_data.csv")

# For illustration, we create a synthetic dataset
np.random.seed(0)
house_size = 2.5 * np.random.rand(100, 1) + 0.5  # House size between 0.5 and 3 square units
house_price = 50 + 20 * house_size + 10 * (house_size ** 2) + np.random.randn(100, 1) * 5  # Price with some noise

# Create a DataFrame
data = pd.DataFrame({'Size': house_size.flatten(), 'Price': house_price.flatten()})

# Step 2: Separate features and target variable
X = data[['Size']]  # Independent variable: House size (as DataFrame, not a single-column array)
y = data['Price']   # Dependent variable: Price

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Apply Polynomial Features Transformation (degree=2 in this case)
poly_features = PolynomialFeatures(degree=2)
X_train_poly = poly_features.fit_transform(X_train)  # Training set transformation
X_test_poly = poly_features.transform(X_test)       # Testing set transformation

# Step 5: Train the Polynomial Regression Model
poly_reg_model = LinearRegression()
poly_reg_model.fit(X_train_poly, y_train)

# Step 6: Predict on the test set
y_pred = poly_reg_model.predict(X_test_poly)

# Step 7: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score: {r2:.2f}")

# Step 8: Visualize the Polynomial Regression
# Sorting values for a smooth curve
X_sorted = np.sort(X.values, axis=0)
X_poly_sorted = poly_features.transform(X_sorted)
y_poly_pred = poly_reg_model.predict(X_poly_sorted)

plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X_sorted, y_poly_pred, color='red', label='Polynomial Regression Fit')
plt.xlabel("House Size (units)")
plt.ylabel("House Price")
plt.title("Polynomial Regression for House Price Prediction")
plt.legend()
plt.show()
