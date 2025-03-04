# Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the dataset
df = pd.read_csv('train.csv')
X = df.iloc[:, [0]].values
y = df.iloc[:, [1]].values

# Splitting the data into trainig and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
