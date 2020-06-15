import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression as LR
import random as rd

class MyLogisticRegression():
    """
    Description:
    My personnal logistic regression to classify things.
    """
    def __init__(self, theta, alpha=0.00015, max_iter=500000):
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

    def data_spliter(self, x, y, proportion):
        x_train = []
        x_test = []
        y_train = []
        y_test = []
        index = [i for i in range(len(x))]
        rd.shuffle(index)
        prop = proportion * len(x)
        i = 0
        while i < prop:
            x_train.append(x[index[i]])
            y_train.append(y[index[i]])
            i += 1
        while i < len(x):
            x_test.append(x[index[i]])
            y_test.append(y[index[i]])
            i += 1
        return (np.array(x_train), np.array(x_test), np.array(y_train), np.array(y_test))

    def zscore(self, x):
        m = sum(x) / len(x)
        std = (sum((x - m) ** 2))/ len(x)
        return (x - m)/(std ** (1/2))

    def label(self, y, label):
        lst = []
        for i in y:
            if i == label:
                lst.append(1)
            else:
                lst.append(0)
        return np.array(lst).reshape(-1, 1)


