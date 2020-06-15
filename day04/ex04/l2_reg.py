import numpy as np

def iterative_l2(theta):
    """Computes the L2 regularization of a non-empty numpy.ndarray, with a for-loop.
    Args:
    theta: has to be a numpy.ndarray, a vector of dimension n * 1.
    Returns:
    The L2 regularization as a float.
    None if theta in an empty numpy.ndarray.
    Raises:
    This function should not raise any Exception.
    """
    n = len(theta)
    i = 1
    result = 0
    while i < n:
        result += theta[i] ** 2
        i += 1
    return float(result)

def l2(theta):
    """Computes the L2 regularization of a non-empty numpy.ndarray, without any for-loop.
    Args:
    theta: has to be a numpy.ndarray, a vector of dimension n * 1.
    Returns:
    The L2 regularization as a float.
    None if theta in an empty numpy.ndarray.
    Raises:
    This function should not raise any Exception.
    """
    result = theta * theta
    result[0] = 0
    return float(sum(result))


x = np.array([2, 14, -13, 5, 12, 4, -19])
y = np.array([3,0.5,-6])
#print(iterative_l2(x))
#print(iterative_l2(y))
print(l2(x))
print(l2(y))
