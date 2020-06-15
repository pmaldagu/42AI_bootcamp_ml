import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression as LR

class MyLogisticRegression():
    """
    Description:
    My personnal logistic regression to classify things.
    """
    def __init__(self, theta, alpha=0.001, max_iter=100000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.theta = theta

    def predict_(self, x):
        y_hat = np.dot(np.c_[np.ones((len(x), 1)), x], self.theta)
        return 1 / (1 + np.exp(-y_hat))

    def fit_(self, x, y):
        m = len(x)
        X = np.c_[np.ones((len(x), 1)), x]
        y_hat = self.predict_(x)
        y = np.squeeze(y)
        i = 0
        while i < self.max_iter:
            gradient = (1 / m) * (np.dot(np.transpose(X), (np.dot(X, self.theta) - y)))
            self.theta = self.theta - self.alpha * gradient
            i += 1
        return self.theta

    def cost_(self, x, y):
        eps = 1e-15
        y_hat = self.predict_(x)
        y = np.squeeze(y)
        return sum((y * np.log(y_hat + eps)) + ((1 - y) * np.log(1 - y_hat + eps))) / -len(y)



X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [3., 5., 9., 14.]])
Y = np.array([1, 0, 1])

mylr = MyLogisticRegression([2, 0.5, 7.1, -4.3, 2.09])

lr = LR(tol=0.001, max_iter=100000)

#lr.coef_ = np.array([2, 0.5, 7.1, -4.3, 2.09])
#lr.intercept_ = np.array([2])

#print(mylr.predict_(X))
lr.fit(X, Y)
#print(lr.predict(X))
print(lr.intercept_)
print(lr.coef_)





#print(mylr.cost_(X,Y))

#plt.plot(X, Y, 'o')
#plt.plot(X, y_hat)

#mylr.fit_(X, Y)

#y_hat2 = mylr.predict_(X)

#mylr2 = MyLogisticRegression(([1.04565272, 0.62555148, 0.38387466, 0.15622435, -0.45990099])

#plt.plot(X, y_hat2, 'go')
#plt.show()

#print(mylr.theta)
#print(mylr.cost_(X,Y))
