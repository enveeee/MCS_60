# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv('Wholesale_customers_data.csv')  # Replace with your dataset path

# Step 2: Inspect the first few rows of the dataset to understand its structure
print("\nFirst few rows of the dataset:")
print(df.head())

# Step 3: Check for null values and handle them (if any)
print("\nChecking for null values:")
print(df.isnull().sum())

# If there are null values, you can remove them or fill them with the mean
df = df.dropna()  # Or you can fill missing values with df.fillna(df.mean())

# Step 4: Standardize the data (important for clustering)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Step 5: Apply Agglomerative Clustering
# We will try different number of clusters and use the silhouette score to evaluate
clustering = AgglomerativeClustering(linkage='ward')  # Ward minimizes the variance within clusters
labels = clustering.fit_predict(df_scaled)

# Step 6: Add the cluster labels to the dataset
df['Cluster'] = labels

# Step 7: Inspect the resulting clusters
print("\nClustered Data (with labels):")
print(df.head())

# Step 8: Evaluate the clustering quality using silhouette score
sil_score = silhouette_score(df_scaled, labels)
print("\nSilhouette Score:", sil_score)

# Step 9: Visualize the clusters (Optional for high-dimensional data)
# If the dataset has more than 2 features, use PCA to reduce to 2D for visualization
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca_components = pca.fit_transform(df_scaled)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=pca_components[:, 0], y=pca_components[:, 1], hue=labels, palette="viridis", s=100, alpha=0.7)
plt.title('Agglomerative Clustering of Wholesale Customers')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend(title='Cluster')
plt.show()
