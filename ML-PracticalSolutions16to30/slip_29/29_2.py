# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample DataFrame with synthetic income data for demonstration purposes
np.random.seed(42)
income_data = np.random.normal(50000, 15000, 100)  # Normally distributed income data
df = pd.DataFrame({'Income': income_data})

# Data Preprocessing: Remove null values if any
df.dropna(inplace=True)

# Data Scaling: Standardize the "Income" column
scaler = StandardScaler()
df['Income_scaled'] = scaler.fit_transform(df[['Income']])

# Determine the optimal number of clusters using the Elbow Method and Silhouette Score
inertia = []
silhouette_scores = []
K_range = range(2, 11)  # Testing for k values from 2 to 10

for k in K_range:
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)  # Set n_init=10 to suppress warning
    kmeans.fit(df[['Income_scaled']])
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(df[['Income_scaled']], kmeans.labels_))

# Plot the Elbow Curve
plt.figure(figsize=(10, 5))
plt.plot(K_range, inertia, marker='o')
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal k")
plt.show()

# Plot Silhouette Scores
plt.figure(figsize=(10, 5))
plt.plot(K_range, silhouette_scores, marker='o', color='orange')
plt.xlabel("Number of clusters (k)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Score for Optimal k")
plt.show()

# Select the optimal k based on the silhouette score or elbow method
optimal_k = K_range[silhouette_scores.index(max(silhouette_scores))]
print(f"Optimal number of clusters based on silhouette score: {optimal_k}")

# Fit the K-means model with the optimal number of clusters
kmeans_optimal = KMeans(n_clusters=optimal_k, n_init=10, random_state=42)
df['Income_Cluster'] = kmeans_optimal.fit_predict(df[['Income_scaled']])

# Analyze and print the clusters
print("Cluster centers (Income groups):")
print(scaler.inverse_transform(kmeans_optimal.cluster_centers_))  # Inverse transform to get original scale income

# Visualize the clusters
sns.scatterplot(data=df, x='Income', y='Income_scaled', hue='Income_Cluster', palette='viridis')
plt.title("Income Clusters")
plt.show()
