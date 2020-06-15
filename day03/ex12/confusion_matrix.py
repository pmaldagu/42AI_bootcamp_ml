import numpy as np
import pandas as pd

def confusion_matrix_(y_true, y_hat, labels=None, df_option=False):
    """
    Compute confusion matrix to evaluate the accuracy of a classification.
    Args:
    y_true:a numpy.ndarray for the correct labels
    y_hat:a numpy.ndarray for the predicted labels
    labels: optional, a list of labels to index the matrix. This may be used to reorder or 
    select a subset of labels. (default=None)
    Returns:
    The confusion matrix as a numpy ndarray.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    result = []
    labels_hat = np.sort(np.unique(y_hat))
    labels_y = np.sort(np.unique(y_true))
    if labels != None:
        labels_y = labels
    elif len(labels_hat) > len(labels_y):
        labels_y = labels_hat
    for row in labels_y:
        r_row = []
        for col in labels_y:
            nb = 0
            for yi, ypi in zip(y_true, y_hat):
                if yi == row and ypi == col:
                    nb += 1
            r_row.append(nb)
        result.append(r_row)
    result = np.array(result)
    if df_option == True:
        data = {}
        i = 0
        for label in labels_y:
            data[label] = result[:, i]
            i += 1
        result = pd.DataFrame(data, labels_y, labels_y)         
    return result
            


y_hat = np.array(['norminet', 'dog', 'norminet', 'norminet', 'dog', 'bird'])
y = np.array(['dog', 'dog', 'norminet', 'norminet', 'dog', 'norminet'])

print("Example 1:\n", confusion_matrix_(y, y_hat))
print("Example 2:\n", confusion_matrix_(y, y_hat, labels=['dog', 'norminet']))
print("Example 3:\n", confusion_matrix_(y, y_hat, labels=['bird', 'dog'], df_option=True))

