import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error

# Load the data
df = pd.read_csv('boston_houses.csv')  # Make sure you have the correct path

# Select only the 'RM' and 'Price' columns
X = df[['RM']]  # Feature (number of rooms)
y = df['Price']  # Target (house price)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize Ridge and Lasso regression models
ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)

# Fit the models on the training data
ridge.fit(X_train, y_train)
lasso.fit(X_train, y_train)

# Make predictions on the test data
ridge_predictions = ridge.predict(X_test)
lasso_predictions = lasso.predict(X_test)

# Calculate Mean Squared Error (MSE) for both models
ridge_mse = mean_squared_error(y_test, ridge_predictions)
lasso_mse = mean_squared_error(y_test, lasso_predictions)

# Print the MSE for both models
print(f"Ridge Regression Mean Squared Error: {ridge_mse}")
print(f"Lasso Regression Mean Squared Error: {lasso_mse}")

# Predict the price of a house with 5 rooms (pass the input as DataFrame to match training format)
room_count = pd.DataFrame([[5]], columns=['RM'])  # Correct format with feature name 'RM'

ridge_price = ridge.predict(room_count)  # Predict using Ridge
lasso_price = lasso.predict(room_count)  # Predict using Lasso

print(f"Predicted Price of a house with 5 rooms (Ridge): {ridge_price[0]}")
print(f"Predicted Price of a house with 5 rooms (Lasso): {lasso_price[0]}")
