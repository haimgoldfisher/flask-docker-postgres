import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Define all possible inputs (True and False)
inputs = [True, False]

# Generate all possible combinations of inputs
input_combinations = list(itertools.product(inputs, repeat=2))  # Change repeat value as needed

# Define a dictionary to store boolean functions and their outputs
bool_functions = {
    'AND': lambda x, y: x and y,
    'OR': lambda x, y: x or y,
    'NOT x': lambda x, y: not x,
    'NOT y': lambda x, y: not y,
    'XOR': lambda x, y: x ^ y,
    'NAND': lambda x, y: not (x and y),
    'NOR': lambda x, y: not (x or y),
    'XNOR': lambda x, y: not (x ^ y)
}

# Create a list to store the results
results = []

# Iterate over each boolean function and input combination
for func_name, func in bool_functions.items():
    for input_comb in input_combinations:
        x, y = input_comb
        output = func(x, y)
        results.append((func_name, x, y, output))

# Create a DataFrame
df = pd.DataFrame(results, columns=['Function', 'Input x', 'Input y', 'Output'])

# Display the DataFrame
#print(df)

df['Function'], mapping_index = pd.factorize(df['Function'])

print(df)

# Split the data into features (inputs) and target (output)
X = df.drop(columns=['Function'])  # Features
y = df['Function']  # Target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)  # You can adjust the number of neighbors as needed

# Train the classifier
knn.fit(X_train, y_train)

# Predict the outputs for the test set
y_pred = knn.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

from sklearn.tree import DecisionTreeClassifier

# Initialize Decision Tree classifier
dt_classifier = DecisionTreeClassifier(random_state=42)

# Train the classifier
dt_classifier.fit(X_train, y_train)

# Predict the outputs for the test set
y_pred_dt = dt_classifier.predict(X_test)

# Calculate accuracy
accuracy_dt = accuracy_score(y_test, y_pred_dt)
print("Decision Tree Accuracy:", accuracy_dt)

