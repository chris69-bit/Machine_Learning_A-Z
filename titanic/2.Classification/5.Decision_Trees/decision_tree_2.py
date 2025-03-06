# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the dataset
df_train = pd.read_csv("train.csv")
df_test = pd.read_csv("test.csv")
X_train = df_train[["PassengerId"]]
y_train = df_train[["Survived"]]

X_test = df_test[["PassengerId"]]

# Train and Fit model
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(X_train, y_train)

# Predict the survivors
y_pred = classifier.predict(X_test)


