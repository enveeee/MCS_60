# Import necessary libraries
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data  # Features: sepal length, sepal width, petal length, petal width
y = iris.target  # Target: flower species

# Apply PCA to reduce dimensions from 4D to 2D
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Split the reduced data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_reduced, y, test_size=0.3, random_state=42)

# Train an SVM model with the reduced data
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy after PCA and SVM classification: {accuracy:.2f}")

# Define a new sample (e.g., sepal length, sepal width, petal length, petal width)
# For example, let's predict for a new sample with these values:
new_sample = [[5.1, 3.5, 1.4, 0.2]]  # Replace with any given measurements

# Reduce the new sample to 2D using the trained PCA
new_sample_reduced = pca.transform(new_sample)

# Predict the class of the new sample
predicted_class = model.predict(new_sample_reduced)
predicted_flower = iris.target_names[predicted_class[0]]

print(f"The predicted flower type for the new measurements is: {predicted_flower}")
