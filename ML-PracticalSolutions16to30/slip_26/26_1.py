# First, install - pip install mlxtend

# Import necessary libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Load data as raw text and preprocess it
transactions = []
with open('groceries.csv') as f:
    for line in f:
        # Split each line by comma and strip extra spaces
        transaction = [item.strip() for item in line.strip().split(',')]
        transactions.append(transaction)

print("Sample Transactions:")
for transaction in transactions[:5]:  # Limit to the first 10 transactions for brevity
    print(transaction)

# Convert the list of transactions to a one-hot encoded DataFrame using TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_onehot = pd.DataFrame(te_ary, columns=te.columns_)

# Apply the Apriori algorithm with a minimum support of 0.25
frequent_itemsets = apriori(df_onehot, min_support=0.25, use_colnames=True)

# Display the frequent itemsets
print(line)
print("Frequent Itemsets with support >= 0.25:")
print(frequent_itemsets)

# Generate the association rules with a minimum confidence threshold (e.g., 0.5)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

# Display the association rules
print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
