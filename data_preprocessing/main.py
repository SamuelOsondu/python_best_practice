import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

dataset = pd.read_csv("Data.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, :3].values

# taking care of the missing data
imp = SimpleImputer(missing_values=np.nan)
imp = imp.fit(x[:, 1:3])
x[:, 1:3] = imp.transform(x[:, 1:3])

# print(x[:, 1:3])

# Encoding categorical data

labelencoder_x = LabelEncoder()
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])

# print(x[:, 0])
onehotencoder = OneHotEncoder(categorical_features=)
x = onehotencoder.fit_transform(x).toarray()
print(x)