# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Step 1: Load the dataset
df = pd.read_csv('house_price_data.csv')  # Replace with the actual dataset path

# Step 2: Check the first few rows of the dataset to understand its structure
print("\nFirst few rows of the dataset:")
print(df.head())

# Step 3: Check for null values and handle them
print("\nChecking for null values in the dataset:")
print(df.isnull().sum())

# Handle missing values: You can drop rows with null values or fill them with mean/median
df = df.dropna()  # Alternatively: df.fillna(df.mean(), inplace=True)

# Step 4: Check the columns to make sure we are using the right ones for features and target
print("\nColumns in the dataset:", df.columns)

# Step 5: Define the features (X) and the target variable (y)
# Assuming columns like 'Size', 'Num_Rooms', 'Location', 'Age' (replace with actual names)
X = df[['Size', 'Num_Rooms', 'Age']]  # Make sure these match your actual dataset's column names
y = df['Price']  # Assuming 'Price' is the target variable for house prices

# Step 6: Handle categorical variables (if any)
# Example: If 'Location' is a categorical variable, we need to one-hot encode it
# Uncomment if 'Location' exists and is categorical
# df = pd.get_dummies(df, columns=['Location'], drop_first=True)

# Re-define features (X) and target (y) after encoding
# X = df.drop(columns=['Price'])  # Adjust based on the actual dataset
# y = df['Price']

# Step 7: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 8: Optional - Scaling features (important if features have different scales)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 9: Train a Multiple Linear Regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)  # Using scaled features

# Step 10: Make predictions on the testing set
y_pred = model.predict(X_test_scaled)

# Step 11: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error (MSE):", mse)
print("R² Score:", r2)

# Step 12: Visualize the results (Actual vs Predicted values)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, color='blue')
plt.title('Actual vs Predicted House Prices')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.show()

# Step 13: Show model coefficients (Optional)
print("\nModel Coefficients:")
print(f"Intercept: {model.intercept_}")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef}")
