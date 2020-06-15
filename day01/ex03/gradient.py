import numpy as np

def simple_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.ndarray, without any for-loop. The
    ,→ three arrays must have compatible dimensions.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    y: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a 2 * 1 vector.
    Returns:
    The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
    None if x, y, or theta are empty numpy.ndarray.
    None if x, y and theta do not have compatible dimensions.
    Raises:
    This function should not raise any Exception.
    """
    y_hat = np.dot(np.c_[np.ones((len(x), 1)), x], theta)
    result = []
    result.append(theta[0] - (sum(y_hat - y) / len(x)))
    result.append(theta[1] - (sum((y_hat - y) * x) / len(x)))
    return np.array(result)

x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])
theta1 = np.array([2, 0.7])
print(simple_gradient(x, y, theta1))
theta2 = np.array([1, -0.4])
print(simple_gradient(x, y, theta2))
