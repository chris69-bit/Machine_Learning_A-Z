#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import The dataset
df = pd.read_csv('train.csv')
X = df.iloc[:, [0]].values
y = df.iloc[:, [1]].values


#Spliting the dataset into test and training 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature scalling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Creating and Fitting model
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

#Classify the test set
y_pred = classifier.predict(X_test)

# Confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)