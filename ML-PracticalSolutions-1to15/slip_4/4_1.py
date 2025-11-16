import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Load the dataset
# Replace 'mall_customers.csv' with the correct path to your dataset
df = pd.read_csv('mall_customers.csv')

# Step 2: Check the first few rows of the dataset to understand its structure
print("\nFirst few rows of the dataset:")
print(df.head())

# Step 3: Select the relevant columns for clustering
# Assuming 'Annual Income (k$)' and 'Spending Score (1-100)' are the features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]  # Use the correct column names

# Step 4: Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Apply K-Means Clustering with the correct value for n_init
# Set n_clusters to 4 (or the number of clusters you want)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)  # Explicitly set n_init=10 to avoid warnings
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Step 6: Check the results
print("\nClusters assigned to each customer:")
print(df[['CustomerID', 'Cluster']].head())  # Assuming 'CustomerID' is the identifier

# Step 7: Plot the clusters
plt.figure(figsize=(8, 6))
plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=df['Cluster'], cmap='viridis')
plt.title('K-Means Clustering of Mall Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.colorbar(label='Cluster')
plt.show()
