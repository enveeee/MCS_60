# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelEncoder

# Load the Iris dataset
iris_data = load_iris()

# Convert the dataset into a DataFrame
df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)

# Add the target (species) column
df['species'] = iris_data.target

# Convert species (categorical values) into numeric using LabelEncoder
label_encoder = LabelEncoder()
df['species'] = label_encoder.fit_transform(df['species'])

# Display the first few rows of the DataFrame to confirm conversion
print(df.head())

# Create a scatter plot for the Iris dataset
plt.figure(figsize=(8, 6))

# You can plot using any two features (here, sepal length and sepal width)
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='species', data=df, palette='Set2')

# Title and labels
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')

# Show plot
plt.show()
