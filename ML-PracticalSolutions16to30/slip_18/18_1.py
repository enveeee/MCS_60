import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the Pima Indians Diabetes Dataset from UCI repository
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 
           'DiabetesPedigreeFunction', 'Age', 'Outcome']

# Read the dataset into a pandas DataFrame
df = pd.read_csv(url, names=columns)

# Step 1: Data Preprocessing
# Check for missing values and replace them with the mean of each column
df.fillna(df.mean(), inplace=True)

# Step 2: Standardize the features (normalize the data)
scaler = StandardScaler()
X = df.drop('Outcome', axis=1)  # Use all features except the target (Outcome)
X_scaled = scaler.fit_transform(X)  # Apply scaling

# Step 3: Apply K-Means Clustering
kmeans = KMeans(n_clusters=2, n_init=10, random_state=42)  # Set n_init explicitly to 10 to avoid future warning
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Step 4: Evaluate the clustering
# Compare the clusters with the actual outcomes to see how well they match
print("\nCluster vs Outcome Distribution:")
print(df[['Cluster', 'Outcome']].value_counts())

# Step 5: Visualizing the clusters (using two features for simplicity)
# Let's use 'Glucose' and 'BMI' for visualization
plt.figure(figsize=(8, 6))
plt.scatter(df['Glucose'], df['BMI'], c=df['Cluster'], cmap='viridis', marker='o')
plt.title("K-Means Clustering on Diabetes Dataset")
plt.xlabel("Glucose")
plt.ylabel("BMI")
plt.colorbar(label='Cluster')
plt.show()

# Step 6: Print the cluster centers (centroids)
print("\nCluster Centers (Centroids):")
print(kmeans.cluster_centers_)
