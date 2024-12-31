"""
Data Retrieval
==============
This quick python code extracts data from the California Housing dataset included in the scikit-learn library.

- The dataset is loaded and the data is extracted.
- The data is then stored in a pandas dataframe.
- The data is then saved in a csv file.

Dependencies
------------
- pandas
- sklearn
"""

# Importing the necessary libraries
import pandas as pd
from sklearn.datasets import fetch_california_housing

# Loading the dataset
california_housing = fetch_california_housing()

# Extracting the data
data = california_housing.data
feature_names = california_housing.feature_names
target = california_housing.target

# Creating a pandas dataframe
df = pd.DataFrame(data, columns=feature_names)
df['target'] = target

# Saving the data in a csv file
df.to_csv('../data/california_housing.csv', index=False)
