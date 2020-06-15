import numpy as np
import matplotlib.pyplot as plt
from plot import plot

x = np.arange(1,6)
y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
theta1 = np.array([4.5, -0.2])
#plot(x, y, theta1)
theta2 = np.array([-1.5, 2])
plot(x, y, theta2)
#plt.show()
