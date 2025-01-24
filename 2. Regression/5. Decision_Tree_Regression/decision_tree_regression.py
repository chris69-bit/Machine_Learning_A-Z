#Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing dataset
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Fitting the regression model
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state= 0)
regressor.fit(x, y)

# Predicting The salary with  regression model
#y_pred = regressor.predict(6.5)

# Visualising the Polynomial Regression results
plt.scatter(x, y, color = 'red')
plt.plot(x, regressor.predict((x)), color = 'blue')
plt.title('Truth or Bluff (Decision Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression (Higher resolution) results
x_grid = np.arange(min(x), max(x), 0.001)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, regressor.predict((x_grid)), color = 'blue')
plt.title('Truth or Bluff (Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()