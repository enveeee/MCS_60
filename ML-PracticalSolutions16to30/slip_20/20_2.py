import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Step 1: Create the dataset
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Mild', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'High', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'Normal', 'High', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Weak', 'Strong', 'Weak', 'Weak', 'Strong', 'Weak', 'Strong', 'Strong', 'Weak'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Step 2: Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Encode the categorical columns using the fitted encoder
df['Outlook'] = label_encoder.fit_transform(df['Outlook'])
df['Temperature'] = label_encoder.fit_transform(df['Temperature'])
df['Humidity'] = label_encoder.fit_transform(df['Humidity'])
df['Wind'] = label_encoder.fit_transform(df['Wind'])
df['PlayTennis'] = label_encoder.fit_transform(df['PlayTennis'])

# Step 3: Split the data into features (X) and target (y)
X = df.drop('PlayTennis', axis=1)  # Features (all columns except 'PlayTennis')
y = df['PlayTennis']  # Target (the 'PlayTennis' column)

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 5: Train the Decision Tree Classifier
dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train, y_train)

# Step 6: Make predictions on the test set
y_pred = dt_classifier.predict(X_test)

# Step 7: Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Print the classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Step 8: Visualizing the decision tree (optional)
# Print the tree rules
tree_rules = export_text(dt_classifier, feature_names=list(X.columns))
print("\nDecision Tree Rules:")
print(tree_rules)

# Step 9: Predict if tennis will be played based on a new sample (e.g., Sunny, Mild, High Humidity, Weak Wind)
# Encode the new sample using the same label encoder fitted earlier
new_data = pd.DataFrame({
    'Outlook': label_encoder.transform(['Sunny']),  # 'Sunny' transformed
    'Temperature': label_encoder.transform(['Mild']),  # 'Mild' transformed
    'Humidity': label_encoder.transform(['High']),  # 'High' transformed
    'Wind': label_encoder.transform(['Weak'])  # 'Weak' transformed
})

# Make a prediction
prediction = dt_classifier.predict(new_data)
predicted_class = label_encoder.inverse_transform(prediction)  # Inverse transform to get original label
print(f"\nPredicted class for new sample: {predicted_class[0]}")
