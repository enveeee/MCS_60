#first install
#pip install tensorflow[and-cuda]


import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load the Pima Indians Diabetes dataset
# You can replace this with pd.read_csv if using a local dataset
data = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv", 
                   names=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
                          "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"])

# Split the data into features and labels
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Standardize the features for better neural network performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Create the neural network model
model = Sequential()

# Input layer and first hidden layer with ReLU activation function
model.add(Dense(16, input_dim=X_train.shape[1], activation='relu'))  # 16 units

# Output layer with Sigmoid activation function (for binary classification)
model.add(Dense(1, activation='sigmoid'))  # Output layer for binary classification

# Compile the model with binary crossentropy loss, adam optimizer, and accuracy metric
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=10, verbose=1, validation_data=(X_test, y_test))

# Evaluate the model on the test data
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy:.4f}")

# Predict on the test data
y_pred = (model.predict(X_test) > 0.5).astype("int32")

# Calculate accuracy score
print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.4f}")
