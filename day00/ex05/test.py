import numpy as np
from prediction import predict_

x = np.arange(1,6)
theta1 = np.array([5, 0])
print(predict_(x, theta1))
