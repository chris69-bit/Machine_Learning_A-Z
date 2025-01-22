# Data Preprocessing

Welcome to the Data preprocessing repository. This folder contains a single project related to data preprocessing in machine learning.

## Table of Contents
- [Introduction](#introduction)
- [Data Preprocessing Template](#template)
- [License](#license)

## Introduction

This repository includes data preprocessing template that demonstrate different techniques used in building machine learning models. The project is designed to help you understand and implement models with ease.

## Data Preprocessing Template

### 1. Data Preprocessing

This script performs data preprocessing for a machine learning project. The steps include:

1. Importing necessary libraries.
2. Importing the dataset.
3. Handling missing values by replacing them with the mean of the column.
4. Encoding categorical data.
5. Splitting the dataset into training and test sets.
6. Feature scaling.

Libraries used:
- numpy
- pandas
- matplotlib.pyplot
- sklearn.impute.SimpleImputer
- sklearn.preprocessing.LabelEncoder
- sklearn.preprocessing.StandardScaler

Functions:
- None

Variables:
- dataset: The imported dataset.
- x: Independent variables from the dataset.
- y: Dependent variable from the dataset.
- imputer: SimpleImputer object for handling missing values.
- labelencoder_y: LabelEncoder object for encoding the dependent variable.
- sc_x: StandardScaler object for feature scaling.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.