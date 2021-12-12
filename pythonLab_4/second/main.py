import numpy as np
from scipy.linalg import solve
from matplotlib import pyplot as plt

data = np.loadtxt('large.txt', skiprows=1)

b = data[np.shape(data)[0] - 1].reshape((np.shape(data)[1], 1))
A = np.delete(data, np.shape(data)[0] - 1, 0)

x = solve(A, b).reshape(1, np.shape(data)[1])

plt.bar(range(x[0].shape[0]), x[0])
plt.grid()
plt.show()
