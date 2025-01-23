# Multiple linear regression

# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Categorical data
from sklearn.preprocessing  import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
x = np.array(ct.fit_transform(x))



# Splitting the dataset into training and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

# Fitting the Multiple Linear regression into the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Predicting the output
y_pred = regressor.predict(x_test)

# Building the optimal model using backward elimination
import statsmodels.api as sm
x = np.append(arr = np.ones((x.shape[0], 1)).astype(int), values = x, axis = 1)

# Fixing missing vales with small values
x[x == 0] = 1e-5

# Selecting the optimal columns
x_opt = x[:, [0, 1, 2, 3, 4]]
regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()




























