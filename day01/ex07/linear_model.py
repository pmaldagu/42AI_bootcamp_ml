from my_linear_regression import MyLinearRegression as MyLR
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

data = pd.read_csv("are_blue_pills_magics.csv")
Xpill = np.array(data['Micrograms']).reshape(-1,1)
Yscore = np.array(data['Score']).reshape(-1,1)
linear_model1 = MyLR(np.array([89.0, -8]))
linear_model2 = MyLR(np.array([89.0, -6]))
linear_model1.fit_ulti(Xpill, Yscore)
#Y_model1 = linear_model1.predict_(Xpill)
#Y_model2 = linear_model2.predict_(Xpill)
#print(Y_model1)
#print(Y_model2)
#print(linear_model1.cost_(Xpill, Yscore))
theta = linear_model1.fit_(Xpill, Yscore)
#print(theta)
