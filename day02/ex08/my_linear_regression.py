import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)

class MyLinearRegression:
    """
    Description:
    My personnal linear regression class to fit like a boss.
    """
    def __init__(self, thetas, alpha=0.000098, max_iter=1000000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas

    def predict_(self, x):
        return np.dot(np.c_[np.ones((len(x), 1)), x], self.thetas)

    def fit_(self, x, y):
        m = len(x)
        X = np.c_[np.ones((len(x), 1)), x]
        y_hat = self.predict_(x)
        y = np.squeeze(y)
        i = 0
        new_theta = self.thetas
        while i < self.max_iter:
            gradient = (1 / m) * (np.dot(np.transpose(X), (np.dot(X, new_theta) - y)))
            #print(gradient)
            new_theta = new_theta - self.alpha * gradient
            #print(new_theta)
            #print(self.mse_(x, y, new_theta))
            #print(self.mse_(x, y, self.thetas))
            #if self.mse_(x, y, new_theta) < self.mse_(x, y, self.thetas):
            #    self.thetas = new_theta
            #print(self.thetas)
            #plt.plot(x, self.predict_(x))
            i += 1
        self.thetas = new_theta
        return self.thetas

    def cost_elem_(self, x, y):
        m = len(x)
        y_hat = self.predict_(x)
        y = np.squeeze(y)
        return (((y_hat - y) ** 2) / (m))

    def cost_(self, x, y):
        elem = self.cost_elem_(x, y)
        return sum(elem)

    def mse_(self, x, y, theta):
        m = len(x)
        y_hat = np.dot(np.c_[np.ones((len(x), 1)), x], theta)
        y = np.squeeze(y)
        elem = (((y_hat - y) ** 2) / (m))
        return sum(elem)



data = pd.read_csv("spacecraft_data.csv")
#X = np.array(data[['Age']])
Y = np.array(data[['Sell_price']])
#myLR_age = MyLinearRegression([1000.0, -1.0])
#print(myLR_age.fit_(X[:,0].reshape(-1,1), Y))
#y_hat = myLR_age.predict_(X)
#plt.plot(X, Y, 'bo', label="Sell price")
#plt.plot(X, y_hat, '.')
#plt.grid()
#plt.legend()
#plt.show()

np.set_printoptions(suppress=True)
X = np.array(data[['Age','Thrust_power','Terameters']])
my_lreg = MyLinearRegression([1.0, 1.0, 1.0, 1.0])
print(my_lreg.cost_(X,Y))
plt.plot(X, Y, 'o')
my_lreg.fit_(X,Y)
plt.plot(X, my_lreg.predict_(X), 'g.')
plt.show()
print(my_lreg.thetas)
print(my_lreg.cost_(X,Y))


#my_lreg = MyLinearRegression([1.0, 1.0, 1.0, 1.0])
#print(my_lreg.cost_(X,Y))
#print(my_lreg.thetas)
#print(my_lreg.fit_(X,Y))
#print(my_lreg.cost_(X,Y))
#print(my_lreg.thetas)
