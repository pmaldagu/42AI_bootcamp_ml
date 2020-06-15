import numpy as np

def logistic_predict_(x, theta):
    y_hat = np.dot(np.c_[np.ones((len(x), 1)), x], theta)
    return 1 / (1 + np.exp(-y_hat))

def vec_log_loss_(y, y_hat, eps=1e-15):
    """
    Compute the logistic loss value.
    Args:
    y: has to be an numpy.ndarray, a vector of dimension m * 1.
    y_hat: has to be an numpy.ndarray, a vector of dimension m * 1.
    eps: epsilon (default=1e-15)
    Returns:
    The logistic loss value as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    return sum((y * np.log(y_hat)) + ((1 - y) * np.log(1 - y_hat))) / -len(y)

y2 = np.array([[1], [0], [1], [0], [1]])
x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
theta2 = np.array([2], [0.5]])
y_hat2 = logistic_predict_(x2, theta2)
print(vec_log_loss_(y2, y_hat2))
