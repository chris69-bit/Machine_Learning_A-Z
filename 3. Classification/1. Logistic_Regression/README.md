# Logistic Regression Project

This project performs logistic regression on a dataset and visualizes the results.

## Project Structure

- `Classification_Template.py`: Template script for performing logistic regression and visualizing results.
- `logistic_regression.py`: Script that implements logistic regression and visualizes results.
- `Social_Network_Ads.csv`: Dataset used for training and testing the logistic regression model.
- `README.md`: Project documentation.

## Dataset

The dataset `Social_Network_Ads.csv` contains the following columns:
- `User ID`: Unique identifier for each user.
- `Gender`: Gender of the user.
- `Age`: Age of the user.
- `EstimatedSalary`: Estimated salary of the user.
- `Purchased`: Whether the user purchased the product (1) or not (0).

## Steps to Run the Project

1. Ensure you have the necessary libraries installed:
    ```sh
    pip install numpy pandas matplotlib scikit-learn
    ```

2. Run the logistic regression script:
    ```sh
    python logistic_regression.py
    ```

## Script Details

### 

This script performs the following steps:
1. Importing necessary libraries.
2. Importing the dataset.
3. Splitting the dataset into training and test sets.
4. Fitting the Logistic Regression model to the training data.
5. Predicting the test set results.
6. Making the Confusion Matrix.
7. Visualizing the Training set results.
8. Visualizing the Test set results.

### 

This script performs logistic regression on the dataset and visualizes the results. It includes:
- Data preprocessing
- Model training
- Predictions
- Confusion matrix creation
- Visualization of training and test set results

## Visualization

The project visualizes the decision boundaries of the logistic regression model for both the training and test sets using matplotlib.

## License

This project is licensed under the MIT License.