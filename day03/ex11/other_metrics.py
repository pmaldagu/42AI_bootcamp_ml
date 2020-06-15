import numpy as np

def accuracy_score_(y, y_hat):
    """
    Compute the accuracy score.
    Args:
    y:a numpy.ndarray for the correct labels
    y_hat:a numpy.ndarray for the predicted labels
    Returns:
    The accuracy score as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    t = 0
    for yi, ypi in zip(y, y_hat):
        if yi == ypi:
            t += 1
    return t / len(y)


def precision_score_(y, y_hat, pos_label=1):
    """
    Compute the precision score.
    Args:
    y:a numpy.ndarray for the correct labels
    y_hat:a numpy.ndarray for the predicted labels
    pos_label: str or int, the class on which to report the precision_score (default=1)
    Returns:
    The precision score as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    tp = 0
    tn = 0
    fn = 0
    fp = 0
    for yi, ypi in zip(y, y_hat):
        if yi == ypi and yi == pos_label:
            tp += 1
        elif yi == ypi and yi != pos_label:
            tn += 1
        elif yi != ypi and yi == pos_label:
            fn += 1
        else:
            fp += 1
    return (tp) / (tp + fp)

def recall_score_(y, y_hat, pos_label=1):
    """
    Compute the recall score.
    Args:
    y:a numpy.ndarray for the correct labels
    y_hat:a numpy.ndarray for the predicted labels
    pos_label: str or int, the class on which to report the precision_score (default=1)
    Returns:
    The recall score as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    tp = 0
    tn = 0
    fn = 0
    fp = 0
    for yi, ypi in zip(y, y_hat):
        if yi == ypi and yi == pos_label:
            tp += 1
        elif yi == ypi and yi != pos_label:
            tn += 1
        elif yi != ypi and yi == pos_label:
            fn += 1
        else:
            fp += 1
    return tp / (tp + fn)

def f1_score_(y, y_hat, pos_label=1):
    """
    Compute the f1 score.
    Args:
    y:a numpy.ndarray for the correct labels
    y_hat:a numpy.ndarray for the predicted labels
    pos_label: str or int, the class on which to report the precision_score (default=1)
    Returns:
    The f1 score as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    prec = precision_score_(y, y_hat, pos_label)
    recall = recall_score_(y, y_hat, pos_label)
    return (2 * prec * recall) / (prec + recall)

#Example 1:
print("Example 1:")
y_hat = np.array([1, 1, 0, 1, 0, 0, 1, 1])
y = np.array([1, 0, 0, 1, 0, 1, 0, 0])
print("accuracy =", accuracy_score_(y, y_hat))
print(precision_score_(y, y_hat))
print(recall_score_(y, y_hat))
print(f1_score_(y, y_hat))

#Example 2:
print("Example 2:")
y_hat = np.array(['norminet', 'dog', 'norminet', 'norminet', 'dog', 'dog', 'dog', 'dog'])
y = np.array(['dog', 'dog', 'norminet', 'norminet', 'dog', 'norminet', 'dog', 'norminet'])
print(accuracy_score_(y, y_hat))
print(precision_score_(y, y_hat, pos_label='dog'))
print(recall_score_(y, y_hat, pos_label='dog'))
print(f1_score_(y, y_hat, pos_label='dog'))

#Example 3:
print("Example 3:")
y_hat = np.array(['norminet', 'dog', 'norminet', 'norminet', 'dog', 'dog', 'dog', 'dog'])
y = np.array(['dog', 'dog', 'norminet', 'norminet', 'dog', 'norminet', 'dog', 'norminet'])
print(f1_score_(y, y_hat, pos_label='norminet'))
