import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 1: Load the data
df = pd.read_csv('UniversalBank.csv')

# Step 2: Preprocess the data
# Assume 'PersonalLoan' is the target variable
# Drop any non-relevant columns or columns that could cause issues (like customer ID, etc.)
df = df.drop(['ID', 'ZIP Code'], axis=1)  # Drop customer ID and ZIP code if they exist

# Handle categorical data - Example, assuming 'Education' is categorical
# If there are other categorical variables, repeat this process for them
label_encoder = LabelEncoder()
df['Education'] = label_encoder.fit_transform(df['Education'])  # Assuming Education has categorical values

# Features and target variable
X = df.drop('PersonalLoan', axis=1)  # Features
y = df['PersonalLoan']  # Target variable

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 4: Train the Linear SVM
svm = SVC(kernel='linear', random_state=42)
svm.fit(X_train_scaled, y_train)

# Step 5: Make predictions
y_pred = svm.predict(X_test_scaled)

# Step 6: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

