# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt"
column_names = ['Variance', 'Skewness', 'Curtosis', 'Entropy', 'Class']
data = pd.read_csv(url, header=None, names=column_names)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Step 2: Separate features and target variable
X = data.drop('Class', axis=1)  # Features (Variance, Skewness, Curtosis, Entropy)
y = data['Class']               # Target variable (Class: 0 = forged, 1 = genuine)

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Initialize and train the Decision Tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Step 5: Predict on the test set
y_pred = clf.predict(X_test)

# Step 6: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the Decision Tree classifier: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Step 7: Plot the Decision Tree
plt.figure(figsize=(15, 10))
plot_tree(clf, feature_names=X.columns, class_names=['Forged', 'Genuine'], filled=True)
plt.title("Decision Tree for Banknote Authentication")
plt.show()
