import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-pastel')

N = 255
vector_u = np.loadtxt('start.dat')
x = np.arange(len(vector_u))
matrix_A = np.eye(len(vector_u)) - np.eye(len(vector_u), k=-1)
matrix_A[0][-1] = -1

fig = plt.figure()
ax = plt.axes(xlim=(0, len(x)), ylim=(0, 1.1 * max(vector_u)))
line, = ax.plot([], [])


def animate(i):
    global x, vector_u
    vector_u = vector_u - 0.5 * matrix_A @ vector_u
    line.set_data(x, vector_u)
    return line,


anim = FuncAnimation(fig, animate, frames=N, interval=10, blit=True)
anim.save('numpy.gif', writer='pillow')
