# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Import the dataset
df = pd.read_csv('train.csv')
X = df[['PassengerId']]
y = df[['Survived']]

# Split the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
X_train = sc_x.fit_transform(X_train)
X_test = sc_x.transform(X_test)

# Create model and fit to the dataset
from sklearn.svm import SVC
classifier = SVC(kernel='rbf', random_state=0)
classifier.fit(X_train, y_train)

# Predictions from the trained model
y_pred = classifier.predict(X_test)

# Confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Visualising the Training set results
