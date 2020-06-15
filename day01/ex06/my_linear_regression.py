import numpy as np

class MyLinearRegression:
    """
    Description:
    My personnal linear regression class to fit like a boss.
    """
    def __init__(self, thetas, alpha=0.001, max_iter=1000):
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
        while i < self.max_iter:
            gradient = (1 / m) * (np.dot(np.transpose(X), (np.dot(X, self.thetas) - y)))
            self.thetas = self.thetas - self.alpha * gradient
            i += 1
        return self.thetas

    def cost_elem_(self, x, y):
        m = len(x)
        y_hat = self.predict_(x)
        print(y_hat)
        y = np.squeeze(y)
        return (((y_hat - y) ** 2) / (2 * m))

    def cost_(self, x, y):
        elem = self.cost_elem_(x, y)
        return sum(elem)


x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
lr1 = MyLinearRegression([2, 0.7])
print(lr1.predict_(x))
print(lr1.cost_elem_(lr1.predict_(x), y))
print(lr1.cost_(lr1.predict_(x),y))

lr2 = MyLinearRegression([0, 0])
lr2.fit_(x, y)
print(lr2.thetas)
