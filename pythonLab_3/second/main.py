import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=3, ncols=2)
fig.set_figheight(9)
plt.subplots_adjust(wspace=0.3, hspace=0.4)
coords = [[0, 0], [1, 0], [2, 0]]

for num, coord in zip(range(1, 4), coords):
    initial_y = np.loadtxt('signal0' + str(num) + '.dat')
    x = np.arange(len(initial_y))
    upd_y = np.zeros(len(x))
    upd_y[0: 10] = np.cumsum(initial_y[0:10]) / np.arange(1, 11)
    upd_y[10:] = np.convolve(initial_y, np.ones(11) / 10, mode='valid')
    left = axs[coord[0]][coord[1]]
    left.plot(x, initial_y)
    left.set_xlim([x.min(), x.max()])
    left.set_ylim([1.1 * initial_y.min(), 1.1 * initial_y.max()])
    left.grid()
    left.set_title('Сырой сигнал ' + str(num))
    right = axs[coord[0]][coord[1] + 1]
    right.plot(x, upd_y)
    right.set_xlim([x.min(), x.max()])
    right.set_ylim([1.1 * initial_y.min(), 1.1 * initial_y.max()])
    right.grid()
    right.set_title('После фильтра ' + str(num))

plt.savefig('signals.png')
