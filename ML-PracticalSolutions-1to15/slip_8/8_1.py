# Import necessary libraries
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# Load the 20 newsgroups dataset
newsgroups = fetch_20newsgroups(subset='all')
X, y = newsgroups.data, newsgroups.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Convert the text data to TF-IDF feature vectors
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.5)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Create the Multinomial Naive Bayes classifier
model = MultinomialNB()

# Train the classifier
model.fit(X_train_tfidf, y_train)

# Predict the categories of the test data
y_pred = model.predict(X_test_tfidf)

# Print the classification report
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=newsgroups.target_names))

# Print the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Define a function to categorize new news text
def categorize_news(text):
    text_tfidf = vectorizer.transform([text])  # Transform input text using the trained TF-IDF vectorizer
    category_index = model.predict(text_tfidf)[0]  # Predict the category index
    return newsgroups.target_names[category_index]  # Return the category name

# Example usage
sample_text = "The government has announced new tax reforms for the next fiscal year."
category = categorize_news(sample_text)
print(f"The category of the given text is: {category}")
