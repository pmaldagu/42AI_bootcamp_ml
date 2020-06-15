import numpy as np
import random as rd

def data_spliter(x, y, proportion):
    """Shuffles and splits the dataset (given by x and y) into a training and a test set, while
    ,→ respecting the indicated proportion.
    Args:
    x: has to be an numpy.ndarray, a matrix of dimension m * n.
    y: has to be an numpy.ndarray, a vector of dimension m * 1.
    proportion: has to be a float, the proportion of the dataset that will be assigned to the
    ,→ training set.
    Returns:
    (train_set, test_set, y_train, y_test) as a tuple of numpy.ndarray
    y_hat as a numpy.ndarray, a vector of dimension m * 1.
    None if x or y are empty numpy.ndarray.
    None if x and y do not share compatible dimensions.
    Raises:
    This function should not raise any Exception.
    """
    x_train = []
    x_test = []
    y_train = []
    y_test = []
    index = [i for i in range(len(x))]
    rd.shuffle(index)
    prop = proportion * len(x)
    i = 0
    while i < prop:
        x_train.append(x[index[i]])
        y_train.append(y[index[i]])
        i += 1
    while i < len(x):
        x_test.append(x[index[i]])
        y_test.append(y[index[i]])
        i += 1
    return (np.array(x_train), np.array(x_test), np.array(y_train), np.array(y_test))


x1 = np.array([1, 42, 300, 10, 59])
y = np.array([0,1,0,1,0])

print(data_spliter(x1, y, 0.8))
