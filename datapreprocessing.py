#libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#dataset
dataset=pd.read_csv('Data.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
#missing data
from sklearn.preprocessing import Imputer
imputer= Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])
#categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x=LabelEncoder()
x[:,0]= labelencoder_x.fit_transform(x[:,0])
onehotencoder=OneHotEncoder(categorical_features=[0])
x=onehotencoder.fit_transform(x).toarray()
labelencoder_y=LabelEncoder()
y= labelencoder_y.fit_transform(y)
#splitting dataset
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.2, random_state=0)
#feature scaling
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)
print(x_train)
print(x_test)