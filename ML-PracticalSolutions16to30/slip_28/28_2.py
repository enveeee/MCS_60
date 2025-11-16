import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# Initialize the SVM models with different kernels
svm_kernels = {
               'linear': SVC(kernel='linear'),
               'poly': SVC(kernel='poly', degree=3),
               'rbf': SVC(kernel='rbf')
               }
# Train and evaluate each model
accuracy_results = {}
for kernel, model in svm_kernels.items():
   model.fit(X_train, y_train)
   y_pred = model.predict(X_test)
   accuracy = accuracy_score(y_test, y_pred)
   accuracy_results[kernel] = accuracy
# Display the accuracy results
for kernel, accuracy in accuracy_results.items():
   print(f'Accuracy of SVM with {kernel} kernel: {accuracy:.4f}')
