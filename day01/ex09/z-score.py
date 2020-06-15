import numpy as np

def zscore(x):
    """Computes the normalized version of a non-empty numpy.ndarray using the z-score, standardization.
    Args:
    x: has to be an numpy.ndarray, a vector.
    Returns:
    x' as a numpy.ndarray.
    None if x is a non-empty numpy.ndarray.
    Raises:
    This function shouldn't raise any Exception.
    """
    m = len(x)
    mean = (sum(x) / m)
    print(mean)
    var = sum((x - mean) ** 2) / m
    print(var)
    x_prime = (x - mean) / (var ** (1 / 2))
    return x_prime

X = np.array([0, 15, -9, 7, 12, 3, -21])
print(zscore(X))
