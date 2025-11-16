#Create a multiple linear regression model for house price dataset divide dataset into train and test data while giving it to model and predict prices of house
#-----------------------------------------------------------------------------------------------------------
# Import necessary libraries
import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset (replace 'house_price_data.csv' with the actual path to your dataset)
df = pd.read_csv('HousePrice.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Select relevant features (independent variables) and target (dependent variable)
# Example: Features 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', etc.
# Target: 'price'
X = df[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 
        'waterfront', 'view', 'condition', 'sqft_above', 'sqft_basement', 
        'yr_built', 'yr_renovated']]  # Features
y = df['price']  # Target

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Predict house prices on the test data
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2): {r2}")

# Display the actual vs predicted prices
comparison_df = pd.DataFrame({'Actual Price': y_test, 'Predicted Price': y_pred})
print("\nActual vs Predicted Prices:")
print(comparison_df.head())
