import numpy as np
import matplotlib.pyplot as plt

def cost_(y, y_hat):
    if len(y) != len(y_hat):
        return Error
    result = sum((y_hat - y) ** 2)
    return result/(2 * len(y))

def plot_with_cost(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    y: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exception.
    """
    y_hat = np.dot(np.c_[np.ones((len(x), 1)), x], theta)
    cost = cost_(y, y_hat) * 2
    plt.plot(x, y, 'o')
    plt.plot(x, y_hat)
    i = 0
    while i < len(x):
        plt.plot([x[i], x[i]],[y[i], y_hat[i]] , 'r--')
        i += 1
    plt.title("Cost : {}".format(cost))
    plt.show()

x = np.arange(1,6)
y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])
theta1= np.array([18,-1])
#plot_with_cost(x, y, theta1)
theta2 = np.array([14, 0])
plot_with_cost(x, y, theta2)
