import matplotlib.pyplot as plt

x = []
y = []

with open('frames.txt') as f:
    points = f.read().split('\n')
    points.pop(int(len(points)) - 1)
    N = int(len(points)/2)
    for i in range(0, N * 2, 2):
        x.append([float(point) for point in points[i].split(" ")])
        y.append([float(point) for point in points[i + 1].split(" ")])

min_x, min_y = min(min(x_points) for x_points in x), min(min(y_points) for y_points in y)
max_x, max_y = max(max(x_points) for x_points in x), max(max(y_points) for y_points in y)

fig, axs = plt.subplots(nrows=3, ncols=2)
fig.set_figheight(8)
plt.subplots_adjust(wspace=0.2, hspace=0.3)
coords = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
for coord, x_coord, y_coord in zip(coords, x, y):
    temp = axs[coord[0]][coord[1]]
    temp.plot(x_coord, y_coord)
    temp.grid()
    temp.set_title('Frame ' + str(y.index(y_coord)))
    temp.set_xlim([min_x, max_x])
    temp.set_ylim([1.1 * min_y, 1.1 * max_y])
    temp.set_xticks(range(int(min_x), int(max_x), 2))
    temp.set_yticks(range(int(min_y), int(max_y), 2))

plt.show()
plt.savefig('frames.png')
