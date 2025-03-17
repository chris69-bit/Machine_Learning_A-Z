# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import dataset
df = pd.read_csv('train.csv')
X = df[["PassengerId"]]
y = df[["Survived"]]

# Split the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# create and fit model
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier.fit(X_train, y_train)

# Predict the survivors
y_pred = classifier.predict(X_test)

# Confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
