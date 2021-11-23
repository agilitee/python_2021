import matplotlib.pyplot as plt
import math

for k in range(5):
    data = "00" + str(k + 1) + ".dat"
    x = []
    y = []
    with open(data, 'r') as file:
        all_data = file.read().split('\n')
        N = int(all_data[0])
        for i in range(1, N + 1):
            x.append(float(all_data[i].split()[0]))
            y.append(float(all_data[i].split()[1]))

    points_size = math.sqrt(x[0] ** 2 + y[0] ** 2)
    for a, b in zip(x, y):
        for c, d in zip(x, y):
            current_size = math.sqrt((a - c) ** 2 + (b - d) ** 2)
            if points_size > current_size > 0:
                points_size = current_size
    points_size *= 0.5
    print(points_size)

    plt.plot(x, y, '.', markersize=points_size)
    plt.axis('equal')
    plt.axis('scaled')
    plt.title("Number of points: " + str(N))
    plt.savefig(str(k + 1))
    plt.show()
