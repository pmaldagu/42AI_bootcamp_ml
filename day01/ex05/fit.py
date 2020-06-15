import numpy as np

def fit_(x, y, theta, alpha, max_iter):
    """
    Description:
    Fits the model to the training dataset contained in x and y.
    Args:
    x: has to be a numpy.ndarray, a vector of dimension m * 1: (number of training examples, 1).
    y: has to be a numpy.ndarray, a vector of dimension m * 1: (number of training examples, 1).
    theta: has to be a numpy.ndarray, a vector of dimension 2 * 1.
    alpha: has to be a float, the learning rate
    max_iter: has to be an int, the number of iterations done during the gradient descent
    Returns:
    new_theta: numpy.ndarray, a vector of dimension 2 * 1.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exception.
    """
    m = len(x)
    X = np.c_[np.ones((len(x), 1)), x]
    y = np.squeeze(y)
    i = 0
    while i < max_iter:
        gradient = (1 / m) * (np.dot(np.transpose(X), (np.dot(X, theta) - y)))
        theta = theta - alpha * gradient
        i += 1
    return theta

x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
theta = np.array([1, 1])
theta1 = fit_(x, y, theta, alpha=5e-8, max_iter = 1500000)
print(theta1)
