import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pickle

# 1. Load data
iris = load_iris()
X, y = iris.data, iris.target

# 2. Train a simple model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# 3. Save it to a file
with open('iris_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Success: iris_model.pkl created!")