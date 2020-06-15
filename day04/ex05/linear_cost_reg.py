import numpy as np

def reg_cost_(y, y_hat, theta, lambda_):
    solution = 0.0
    for i, j in zip(y, y_hat):
        solution += (j - i) ** 2
    result = theta * theta
    result[0] = 0
    solution = solution + lambda_ * (sum(result))
    return float(0.5 / len(y) * solution)

y = np.array([2, 14, -13, 5, 12, 4, -19])
y_hat = np.array([3, 13, -11.5, 5, 11, 5, -20])
theta = np.array([1, 2.5, 1.5, -0.9])

print(reg_cost_(y, y_hat, theta, .9))

