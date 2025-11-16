import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Step 1: Load the dataset
# Assuming the dataset is a CSV file
df = pd.read_csv('weather.csv')

# Step 2: Preprocess the data (Label Encoding for categorical columns)
label_encoder = LabelEncoder()

# Encode categorical columns into numeric values
df['Outlook'] = label_encoder.fit_transform(df['Outlook'])
df['Temperature'] = label_encoder.fit_transform(df['Temperature'])
df['Humidity'] = label_encoder.fit_transform(df['Humidity'])
df['Wind'] = label_encoder.fit_transform(df['Wind'])
df['PlayTennis'] = label_encoder.fit_transform(df['PlayTennis'])

# Step 3: Split the dataset into features and target
X = df.drop('PlayTennis', axis=1)  # Features (Outlook, Temperature, Humidity, Wind)
y = df['PlayTennis']              # Target (PlayTennis)

# Step 4: Split the data into training and testing sets (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 5: Initialize the Naive Bayes model (Gaussian Naive Bayes)
naive_bayes_model = GaussianNB()

# Step 6: Train the model using the training data
naive_bayes_model.fit(X_train, y_train)

# Step 7: Make predictions on the test data
y_pred = naive_bayes_model.predict(X_test)

# Step 8: Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Step 9: Output results
print(f"Accuracy of Naive Bayes Model: {accuracy * 100:.2f}%")
print("Confusion Matrix:")
print(conf_matrix)
