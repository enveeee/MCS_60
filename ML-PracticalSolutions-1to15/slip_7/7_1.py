import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv('Salary_positions.csv')

# Step 2: Check for missing values (if any)
print(df.isnull().sum())

# Step 3: Preprocess the data (if necessary, like removing missing values)
df = df.dropna()  # Drop rows with missing values

# Step 4: Select features (Position Level) and target (Salary)
X = df[['Position_Level']]  # Feature: Position Level (keep it as a DataFrame)
y = df['Salary']            # Target: Salary

# Step 5: Initialize the Linear Regression model
model = LinearRegression()

# Step 6: Fit the model to the data
model.fit(X, y)

# Step 7: Predict the salary for level 11 and level 12 employees
levels_to_predict = pd.DataFrame([[11], [12]], columns=['Position_Level'])  # Ensure this is a DataFrame
predicted_salaries = model.predict(levels_to_predict)

# Step 8: Output the predictions
for level, salary in zip([11, 12], predicted_salaries):
    print(f"Predicted salary for Level {level}: ${salary:.2f}")

# Optional: Visualizing the data and regression line
plt.scatter(X, y, color='blue')  # Plot the actual data points
plt.plot(X, model.predict(X), color='red')  # Plot the regression line
plt.title('Salary vs Position Level')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
