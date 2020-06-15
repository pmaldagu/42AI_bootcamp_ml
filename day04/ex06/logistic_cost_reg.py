import numpy as np
import math as mt

def reg_log_cost_(y, y_hat, theta, lambda_):
    """Computes the regularized cost of a logistic regression model from two non-empty 
    numpy.ndarray, without any for loop. The two arrays must have the same dimensions.
    Args:
    y: has to be an numpy.ndarray, a vector of dimension m * 1.
    y_hat: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be a numpy.ndarray, a vector of dimension n * 1.
    lambda_: has to be a float.
    Returns:
    The regularized cost as a float.
    None if y, y_hat, or theta is empty numpy.ndarray.
    None if y and y_hat do not share the same dimensions.
    Raises:
    This function should not raise any Exception.
    """
    eps = 1e-15
    solution = sum((y * np.log(y_hat + eps)) + ((1 - y) * np.log(1 - y_hat + eps))) / -len(y)
    result = theta * theta
    result[0] = 0
    print(solution)
    print(sum(result))
    return solution + ((lambda_ / (2 * len(y))) * sum(result))

y = np.array([1, 1, 0, 0, 1, 1, 0])
y_hat = np.array([.9, .79, .12, .04, .89, .93, .01])
theta = np.array([1, 2.5, 1.5, -0.9])
print(reg_log_cost_(y, y_hat, theta, .5))
