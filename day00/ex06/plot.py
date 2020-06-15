import numpy as np
import matplotlib.pyplot as plt

def plot(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    y: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exceptions.
    """
    y_hat = np.dot(np.c_[np.ones((len(x), 1)), x], theta)
    plt.plot(x, y, 'o') #o veut dire point, peut rajouter couleur ex: 'ro'
    plt.plot(x, y_hat)
    plt.show()
