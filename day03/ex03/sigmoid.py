def sigmoid_(x):
    """
    Compute the sigmoid of a vector.
    Args:
    x: has to be an numpy.ndarray, a vector
    Returns:
    The sigmoid value as a numpy.ndarray.
    None if x is an empty numpy.ndarray.
    Raises:
    This function should not raise any Exception.
    """
    return 1 / (1 + np.exp(-x))
