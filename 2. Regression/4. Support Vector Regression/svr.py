#Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing dataset
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Fitting the regression model
from sklearn.svm import SVR
regressor = SVR()
regressor.fit(x, y)

# Predicting The salary with  regression model

# Visualising the Polynomial Regression results
plt.scatter(x, y, color = 'red')
plt.plot(x, regressor.predict((x)), color = 'blue')
plt.title('Truth or Bluff (Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()