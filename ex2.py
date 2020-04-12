import pandas as pd
import numpy as np

datapre = pd.read_csv("C:\\Users\\asus\\Desktop\\大三下\\媒体数据管理\\ColorHistogram.asc", header=None, encoding='utf-8', sep=' ')
# data = datapre.values.tolist()
# data = datapre.values
# data = datapre.as_matrix()
data = np.array(datapre)
data = data[:, 1:]
# print(datapre)
# print(data)
data = data.T

c = np.cov(data)
# print(c)
w, v = np.linalg.eig(c)
sort_w = -np.sort(-w)
print("特征值序列为：")
print(sort_w)
sort_index = np.argsort(-w)
n = v.shape[1]
m = v.shape[0]
p = v[:, sort_index[0]].reshape(1, n)
i = 1
while i < 2:
    p = np.concatenate((p, v[:, sort_index[i]].reshape(1, n)), axis=0)
    i += 1
print("变换矩阵为：")
print(p)
res = np.dot(p, data)
print("结果为：")
print(res)
