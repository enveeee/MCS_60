import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, VotingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import load_diabetes

# Load the dataset
# You can replace this with pd.read_csv('diabetes.csv') if you have the CSV file
data = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv", 
                   names=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
                          "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"])

# Split data into features and target
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. Bagging (Random Forest)
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
random_forest.fit(X_train, y_train)
y_pred_rf = random_forest.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)

# 2. Boosting (AdaBoost and GradientBoosting)
ada_boost = AdaBoostClassifier(n_estimators=100, random_state=42)
ada_boost.fit(X_train, y_train)
y_pred_ada = ada_boost.predict(X_test)
accuracy_ada = accuracy_score(y_test, y_pred_ada)

gradient_boost = GradientBoostingClassifier(n_estimators=100, random_state=42)
gradient_boost.fit(X_train, y_train)
y_pred_gb = gradient_boost.predict(X_test)
accuracy_gb = accuracy_score(y_test, y_pred_gb)

# 3. Voting Classifier (combination of Logistic Regression, Random Forest, and SVM)
log_clf = LogisticRegression(solver='lbfgs', max_iter=1000)
svc_clf = SVC(probability=True, random_state=42)

voting_clf = VotingClassifier(estimators=[
    ('lr', log_clf), 
    ('rf', random_forest), 
    ('svc', svc_clf)], voting='soft')

voting_clf.fit(X_train, y_train)
y_pred_voting = voting_clf.predict(X_test)
accuracy_voting = accuracy_score(y_test, y_pred_voting)

# 4. Stacking (combine Logistic Regression, Decision Tree, SVC, with Random Forest as final estimator)
stacking_clf = StackingClassifier(estimators=[
    ('lr', log_clf), 
    ('dt', DecisionTreeClassifier(random_state=42)),
    ('svc', svc_clf)],
    final_estimator=RandomForestClassifier(random_state=42)
)

stacking_clf.fit(X_train, y_train)
y_pred_stacking = stacking_clf.predict(X_test)
accuracy_stacking = accuracy_score(y_test, y_pred_stacking)

# Display the results
print("Accuracy Results:")
print(f"Random Forest (Bagging): {accuracy_rf:.4f}")
print(f"AdaBoost (Boosting): {accuracy_ada:.4f}")
print(f"GradientBoosting (Boosting): {accuracy_gb:.4f}")
print(f"Voting Classifier: {accuracy_voting:.4f}")
print(f"Stacking Classifier: {accuracy_stacking:.4f}")

# Display confusion matrix for the best-performing model (Stacking)
print("\nConfusion Matrix for Stacking Classifier:")
print(confusion_matrix(y_test, y_pred_stacking))

# Classification report for detailed analysis
print("\nClassification Report for Stacking Classifier:")
print(classification_report(y_test, y_pred_stacking))
