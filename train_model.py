import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and save a Random Forest classifier
model_rf = RandomForestClassifier()
model_rf.fit(X_train, y_train)
joblib.dump(model_rf, 'models/model_rf.joblib')

# Train and save a K-Nearest Neighbors classifier
model_knn = KNeighborsClassifier()
model_knn.fit(X_train, y_train)
joblib.dump(model_knn, 'models/model_knn.joblib')

print("Models trained and saved successfully.")
