import numpy as np

def simple_predict(x, theta):
    y_hat = []
    X = np.c_[np.ones((len(x), 1)), x]
    #print(np.transpose(X))
    
    for xi in X:
        #print(xi)
        #print(theta)
        y_hat.append(sum(xi * theta))
    return np.array(y_hat)

x = np.arange(1,13).reshape((4,3))
theta1 = np.array([5, 0, 0, 0])
print(simple_predict(x, theta1))
theta2 = np.array([0, 1, 0, 0])
print(simple_predict(x, theta2))
