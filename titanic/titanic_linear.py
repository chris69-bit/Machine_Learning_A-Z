# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the dataset
df = pd.read_csv('train.csv')
X = df.iloc[:, [2]].values
y = df.iloc[:, [1]].values

# Splitting the data into training and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Linear model creation
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the test set
y_pred = regressor.predict(X_test)

# Visualising the trainig set
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Wrong Model')
plt.xlabel('Ticket Class')
plt.ylabel('Survived')
plt.show()