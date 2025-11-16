import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelEncoder

# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Target (species)

# Step 2: Convert Categorical values to Numeric (Target variable)
label_encoder = LabelEncoder()
y_numeric = label_encoder.fit_transform(y)  # Convert species to numeric labels

# Step 3: Create a DataFrame for better visualization
df = pd.DataFrame(X, columns=iris.feature_names)
df['Species'] = y_numeric  # Add the numeric species to the DataFrame

# Step 4: Create Scatter Plot
plt.figure(figsize=(10, 6))

# Scatter plot: Sepal length vs. Sepal width
plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=df['Species'], cmap='viridis')
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')

# Scatter plot: Petal length vs. Petal width
plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
plt.scatter(df['petal length (cm)'], df['petal width (cm)'], c=df['Species'], cmap='viridis')
plt.title('Petal Length vs Petal Width')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')

# Show the plot
plt.tight_layout()
plt.show()
