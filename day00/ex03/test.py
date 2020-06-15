import numpy as np
from prediction import simple_predict

x = np.arange(1,6)
theta1 = np.array([5, 0])
print(simple_predict(x, theta1))
print(np.array([1., 2., 3., 4., 5.]))
