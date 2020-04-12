import numpy as np
import pandas as pd

datapre = pd.read_csv("C:\\Users\\asus\\Desktop\\大三下\\媒体数据管理\\ColorHistogram.asc", header=None, encoding='utf-8', sep=' ')
# data = datapre.values.tolist()
# data = datapre.values
# data = datapre.as_matrix()
data = np.array(datapre)
data = data[:, 1:]
# print(data)


def dist(x, y):
    return np.sqrt(np.sum((x-y)**2))


e = 0.01
N = 1
Nmax = 2**14
m, n = data.shape
c = np.zeros((Nmax+1, n))
c[1] = np.mean(data, axis=0)
D = 0
for i in range(m):
    D += dist(c[1], data[i, :])
D = 1.0 * D / m

while N < Nmax:
    i = 1
    while i <= N:
        c[N+i] = c[i] * (1 - e)
        c[i] = c[i] * (1 + e)
        i += 1
    N = 2 * N

    cluster = np.zeros((m, 2))
    change = True
    while change:
        for i in range(m):
            d = dist(data[i, :], c[1, :])
            mind = d
            minindex = 1
            j = 2
            while j <= N:
                d = dist(c[j, :], data[i, :])
                if d < mind:
                    mind = d
                    minindex = j
                j = j + 1
            cluster[i, :] = minindex, mind
        for l in range(N):
            pointsInCluster = data[np.nonzero(cluster[:, 0] == (l+1))[0]]
            c[l+1, :] = np.mean(pointsInCluster, axis=0)
        D1 = 0
        for i in range(m):
            index = int(cluster[i, 0])
            D1 += dist(c[index], data[i, :])
        D1 = 1.0 * D1 / m
        if (((D - D1) * 1.0 / D) <= e):
            change = False
        else:
            D = D1

    for i in range(N):
        pointsInCluster = data[np.nonzero(cluster[:, 0] == (i+1))[0]]
        print("center" + str(i+1) + ":")
        print(c[i+1, :])
        print("point in cluster" + str(i+1) + ":")
        print(pointsInCluster)
