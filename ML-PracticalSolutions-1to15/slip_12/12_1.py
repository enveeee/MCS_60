# Import necessary libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data  # Feature matrix
y = iris.target  # Target vector

# Step 2: Split the data into training and testing sets (e.g., 70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Initialize the k-NN classifier and set the number of neighbors (e.g., k=3)
knn = KNeighborsClassifier(n_neighbors=3)

# Train the k-NN model
knn.fit(X_train, y_train)

# Step 4: Make predictions on the test set
y_pred = knn.predict(X_test)

# Step 5: Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Print the classification report for detailed performance metrics
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
