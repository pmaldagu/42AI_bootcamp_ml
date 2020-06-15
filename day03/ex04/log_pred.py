import numpy as np

def logistic_predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * n.
    theta: has to be an numpy.ndarray, a vector of dimension (n + 1) * 1.
    Returns:
    y_hat as a numpy.ndarray, a vector of dimension m * 1.
    None if x or theta are empty numpy.ndarray.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exception.
    """
    y_hat = mp.dot(np.c_[np.ones((len(x), 1)), x], theta)
    return 1 / (1 + np.exp(-y_hat))

