# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import dataset
df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

X_train = df_train[["PassengerId"]]
y_train = df_train[["Survived"]]

X_test = df_train[["PassengerId"]]

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

# Fitting the Naive Bayes Model
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

#Predict the Classification of new dataset
y_pred = classifier.predict(X_test)