import numpy as np

def predict(x, theta):
    return np.dot(np.c_[np.ones((len(x), 1)), x], theta)

def cost_elem_(y, y_hat):
    """
    Description:
    Calculates all the elements (1/2*M)*(y_pred - y)^2 of the cost function.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    J_elem: numpy.ndarray, a vector of dimension (number of the training examples,1).
    None if there is a dimension matching problem between X, Y or theta.
    Raises:
    This function should not raise any Exception.
    """
    j = []
    for yi_hat, yi in zip(y, y_hat):
        j.append((yi_hat - yi) ** 2 * (1 / (2*len(y))))
    return np.array(j)

def cost_(y, y_hat):
    """
    Description:
    Calculates the value of cost function.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    J_value : has to be a float.
    None if there is a dimension matching problem between X, Y or theta.
    Raises:
    This function should not raise any Exception.
    """
    add = 0
    j = cost_elem_(y, y_hat)
    for ji in j:
        add += ji
    return float(add)

x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
y_hat1 = predict(x1, theta1)
y1 = np.array([[2.], [7.], [12.], [17.], [22.]])

print(cost_elem_(y1, y_hat1))
print(cost_(y1, y_hat1))
