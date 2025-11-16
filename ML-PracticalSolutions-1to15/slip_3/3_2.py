# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv('crash.csv')  # Replace with your dataset path

# Step 2: Check the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(df.head())

# Step 3: Check for missing values
print("\nChecking for missing values:")
print(df.isnull().sum())

# Step 4: Handle missing values if any (you can either drop or fill missing values)
# For now, we'll drop rows with missing values
df.dropna(inplace=True)

# Step 5: Prepare the features (X) and target (y)
X = df[['Age', 'Speed']]  # Features (Age and Speed)
y = df['Survived']  # Target (Survived: 1 for survived, 0 for not survived)

# Step 6: Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Initialize the Logistic Regression model
model = LogisticRegression()

# Step 8: Train the model on the training data
model.fit(X_train, y_train)

# Step 9: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 10: Evaluate the model performance
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Print the results
print("\nModel Accuracy:", accuracy)
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(class_report)

# Step 11: Visualize the confusion matrix (optional)
fig, ax = plt.subplots(figsize=(6, 6))
ax.matshow(conf_matrix, cmap='Blues', alpha=0.7)
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        ax.text(j, i, str(conf_matrix[i, j]), ha='center', va='center', color='black')

plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Step 12: Predict the survival probability of a new passenger
age = 45
speed = 60
new_data = pd.DataFrame([[age, speed]], columns=['Age', 'Speed'])  # Make it a DataFrame with proper column names
survival_prob = model.predict_proba(new_data)
print(f"\nSurvival probability for a passenger with Age={age} and Speed={speed} mph: {survival_prob[0][1]:.2f}")
