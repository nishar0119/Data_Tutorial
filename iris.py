import pandas as pd
import numpy as np
data = pd.read_csv('data.csv')
print(data.head(5))
print(data.describe())
print(data.sepal_length)