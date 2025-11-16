import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_california_housing
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score

# Load the dataset
data = fetch_california_housing()

# Convert the data to a DataFrame for easier handling
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Define the average price to classify above/below average house prices
average_price = y.mean()

# Create binary labels: 1 for above average, 0 for below average
y_binary = (y > average_price).astype(int)

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y_binary,test_size=0.2, random_state=42)

# Standardize the features (normalize the data for better performance in ANN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create the ANN model
model = Sequential()

# Input layer and first hidden layer with 16 neurons and ReLU activation
model.add(Dense(16, input_dim=X_train_scaled.shape[1], activation='relu'))

# Second hidden layer with 8 neurons and ReLU activation
model.add(Dense(8, activation='relu'))

# Output layer with Sigmoid activation (binary classification)
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, verbose=1,
          validation_split=0.2)

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test_scaled, y_test)
print(f"Test Accuracy: {accuracy:.4f}")

# Make predictions
y_pred = (model.predict(X_test_scaled) > 0.5).astype("int32")

# Calculate accuracy score
accuracy_test = accuracy_score(y_test, y_pred)
print(f"Accuracy on Test Set: {accuracy_test:.4f}")
