# Classification Template
This template performs classifier regression on a dataset and visualizes the results.

The template includes the following steps:
1. Importing necessary libraries.
2. Importing the dataset.
3. Splitting the dataset into training and test sets.
4. Fitting the Logistic Regression model to the training data.
5. Predicting the test set results.
6. Making the Confusion Matrix.
7. Visualizing the Training set results.
8. Visualizing the Test set results.

## Template Structure
Functions and variables:
- dataset: The dataset imported from 'Social_Network_Ads.csv'.
- x: Features from the dataset (Age and Estimated Salary).
- y: Target variable from the dataset (Purchased).
- x_train, x_test: Training and test sets for features.
- y_train, y_test: Training and test sets for the target variable.
- classifier: The Logistic Regression model (to be defined).
- y_pred: Predictions for the test set.
- confusion_matrix: Function to create the confusion matrix.
- X_set, y_set: Variables used for visualization of training and test set results.
- X1, X2: Meshgrid arrays used for plotting decision boundaries.
