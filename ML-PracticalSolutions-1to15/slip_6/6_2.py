import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings

# Suppress FutureWarnings about the n_init change in KMeans
warnings.filterwarnings("ignore", category=FutureWarning)

# Load the dataset (replace with your actual dataset path)
df = pd.read_csv('employees.csv')

# Step 1: Check for missing or null values and handle them
print("Checking for missing values in the dataset:")
print(df.isnull().sum())  # Show count of missing values per column

# Step 2: Drop rows with missing values (or handle them as needed)
df_cleaned = df.dropna()  # Drop rows with any missing values
print("\nData after removing rows with missing values:")
print(df_cleaned.isnull().sum())  # Check again for missing values

# Step 3: Select the relevant columns for clustering (e.g., 'Income' and 'Age')
# Make sure these columns exist in your dataset
X = df_cleaned[['Income', 'Age']]

# Step 4: Standardize the data (important for K-Means clustering)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Initialize and fit the KMeans model
kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
kmeans.fit(X_scaled)

# Step 6: Get the cluster labels for each employee
df_cleaned['Cluster'] = kmeans.labels_

# Step 7: Show the results with the cluster labels
print("\nClustered data with labels:")
print(df_cleaned.head())

# Step 8: Optionally, you can save the results to a new CSV file
df_cleaned.to_csv('employees_with_clusters.csv', index=False)

# Optional: Plotting the clusters for visualization (optional step)
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.scatter(df_cleaned['Income'], df_cleaned['Age'], c=df_cleaned['Cluster'], cmap='viridis')
plt.title('K-Means Clustering of Employees')
plt.xlabel('Income')
plt.ylabel('Age')
plt.colorbar(label='Cluster')
plt.show()
