import numpy as np
import pandas as pd

datapre = pd.read_csv("C:\\Users\\asus\\Desktop\\大三下\\媒体数据管理\\ColorHistogram.asc", header=None, encoding='utf-8', sep=' ')
# data = datapre.values.tolist()
# data = datapre.values
# data = datapre.as_matrix()
data = np.array(datapre)
data = data[:1000, 1:]
# print(data)

m, n = data.shape
k = 10
c = np.zeros((k, n))
for i in range(k):
    index = int(np.random.uniform(0, m))
    c[i, :] = data[index, :]
# print(c)


def dist(x, y):
    return np.sqrt(np.sum((x-y)**2))


cluster = np.zeros((m, 2))
change = True
while change:
    change = False
    for i in range(m):
        # mind = 100000.0
        # minindex = -1
        # for j in range(k):
        #     d = dist(c[j,:],data[i,:])
        #     if d < mind:
        #         mind = d
        #         minindex = j
        d = dist(data[i, :], c[0, :])
        mind = d
        minindex = 0
        j = 1
        while j < k:
            d = dist(c[j, :], data[i, :])
            if d < mind:
                mind = d
                minindex = j
            j = j + 1
        if ((cluster[i, 0] != minindex)or(cluster[i, 1] != mind)):
            change = True
            cluster[i, :] = minindex, mind
    for l in range(k):
        pointsInCluster = data[np.nonzero(cluster[:, 0] == l)[0]]
        c[l, :] = np.mean(pointsInCluster, axis=0)

for i in range(k):
    pointsInCluster = data[np.nonzero(cluster[:, 0] == l)[0]]
    print("center" + str(i+1) + ":")
    print(c[i, :])
    print("point in cluster" + str(i+1) + ":")
    print(pointsInCluster)
