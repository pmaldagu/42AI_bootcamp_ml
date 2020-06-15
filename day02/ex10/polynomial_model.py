import numpy as np
np.set_printoptions(suppress=True)

def add_polynomial_features(x, power):
    """Add polynomial features to vector x by raising its values up to the power given in
    ,→ argument.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    power: has to be an int, the power up to which the components of vector x are going to be
    ,→ raised.
    Returns:
    The matrix of polynomial features as a numpy.ndarray, of dimension m * n, containg he
    ,→ polynomial feature values for all training examples.
    None if x is an empty numpy.ndarray.
    Raises:
    This function should not raise any Exception.
    """
    j = 0
    x2 = np.zeros((len(x), power))
    for row in x:
        i = 2
        while i <= power:
            row = np.append(row, (row[0] ** i))
            i +=1
        x2[j] = row
        j += 1
    return x2


x = np.arange(1,6).reshape(-1, 1)
print(add_polynomial_features(x, 3))
print(add_polynomial_features(x, 6))
