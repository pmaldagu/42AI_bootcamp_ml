import pandas as pd
from my_logistic_regression import MyLogisticRegression as MyLR
import numpy as np
import matplotlib.pyplot as plt

X = pd.read_csv("solar_system_census.csv")
Y = pd.read_csv("solar_system_census_planets.csv")

X = np.array(X[['height', 'weight', 'bone_density']]).reshape(-1,3)
Y = np.array(Y['Origin']).reshape(-1, 1)

mylr = MyLR([1, 1, 1, 1])
X = mylr.zscore(X)
Y = mylr.label(Y, 2)

x_train, x_test, y_train, y_test = mylr.data_spliter(X, Y, 0.6)

print(mylr.fit_(x_train, y_train))
#print(mylr.predict_(x_train))
print(mylr.cost_(x_train, y_train))

plt.plot(x_train[:,0], y_train, 'b.')
plt.plot(x_train[:,0], mylr.predict_(x_train), 'g.')

plt.show()
