import numpy as np
import pandas as pd
from my_linear_regression import MyLinearRegression as MLR
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)

def poly_feat(x, power):
    """Add polynomial features to vector x by raising its values up to the power given in
    ,→ argument.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    power: has to be an int, the power up to which the components of vector x are going to be
    ,→ raised.
    Returns:
    The matrix of polynomial features as a numpy.ndarray, of dimension m * n, containg he
    ,→ polynomial feature values for all training examples.
    None if x is an empty numpy.ndarray.
    Raises:
    This function should not raise any Exception.
    """
    j = 0
    x2 = np.zeros((len(x), power))
    for row in x:
        i = 2
        while i <= power:
            row = np.append(row, (row[0] ** i))
            i +=1
        x2[j] = row
        j += 1
    return x2


data = pd.read_csv("are_blue_pills_magics.csv")
X = np.array(data[['Micrograms']])
Y = np.array(data[['Score']])

x1 = poly_feat(X, 2)
x2 = poly_feat(X, 3)
x3 = poly_feat(X, 4)
x4 = poly_feat(X, 5)
x5 = poly_feat(X, 6)
x6 = poly_feat(X, 7)
x7 = poly_feat(X, 8)
x8 = poly_feat(X, 9)
x9 = poly_feat(X, 10)

lr1 = MLR([80, 1, 1])
lr2 = MLR([80, 1, 1, 1])
lr3 = MLR([80, 1, 1, 1, 1])
lr4 = MLR([80, 1, 1, 1, 1, 1])
lr5 = MLR([80, 1, 1, 1, 1, 1, 1])
lr6 = MLR([1, 1, 1, 1, 1, 1, 1, 1])
lr7 = MLR([1, 1, 1, 1, 1, 1, 1, 1, 1])
lr8 = MLR([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
lr9 = MLR([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

lr1.fit_(x1, Y)
lr2.fit_(x2, Y)
lr3.fit_(x3, Y)
lr4.fit_(x4, Y)
#lr5.fit_(x5, Y)
#lr6.fit_(x6, Y)
#lr7.fit_(x7, Y)
#lr8.fit_(x8, Y)
#lr9.fit_(x9, Y)

y_1 = lr1.predict_(x1)
y_2 = lr2.predict_(x2)
y_3 = lr3.predict_(x3)
y_4 = lr4.predict_(x4)
#y_5 = lr5.predict_(x5)
#y_6 = lr6.predict_(x6)
#y_7 = lr7.predict_(x7)
#y_8 = lr8.predict_(x8)
#y_9 = lr9.predict_(x9)

print(lr3.cost_(x3, Y))

plt.plot(X, Y, 'o')
plt.plot(X, y_1, 'g')
plt.plot(X, y_2, 'r')
plt.plot(X, y_3, 'b')
#plt.plot(X, y_4)
#plt.plot(X, y_6)
plt.show()
