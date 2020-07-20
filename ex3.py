import pandas as pd
import numpy as np
import math
import time

time0 = time.time()
datapre = pd.read_csv("C:\\Users\\asus\\Desktop\\大三下\\媒体数据管理\\ColorHistogram.asc", header=None, encoding='utf-8', sep=' ')
data = np.array(datapre)
data = data[:, 1:]
# data = data[0:1000]
n = data.shape[1]
m = data.shape[0]

# 定义相似度
# 构造哈希函数
# 映射，查询


def dist(x, y):
    return np.sqrt(np.sum((x-y)**2))


r = 500  # 通过多次实验自己设定
h = []
hh = []
hhh = []
functimes = 2
fucclusters = 1
for i in range(fucclusters):
    for j in range(functimes):
        b = int(np.random.uniform(0, r))
        a = np.random.normal(loc=0.0, scale=1.0, size=n)
        a = a * 10
        for each in data:
            htemp = (np.dot(a, each.T) + b)/r
            htemp = math.floor(htemp)
            h.append(htemp)  # 每行对应一个hash值
        hh.append(h)  # 每行对应一个hash向量
    hhh.append(hh)
hh = np.array(hh)  # funtimes行，m列
hhh = np.array(hhh)  # fucclusters张表
# b = int(np.random.uniform(0, r))
# a = np.random.normal(loc=0.0, scale=1.0, size=n)
# a = a * 10
# for each in data:
#     htemp = (np.dot(a, each.T) + b)/r
#     htemp = math.floor(htemp)
#     h.append(htemp)  # 每行对应一个hash值
allres = []
num = 1000  # 前1000个点作为检测点
for i in range(num):
    resp = []
    resd = []
    res = []
    for j in range(m):
        if i != j:
            p = 0
            for ii in range(fucclusters):
                for jj in range(fucclusters):
                    if (hhh[ii, :, i] == hhh[jj, :, j]).all():
                        p = 1  # 不同组中存在一组值全部相等，则判定可能相似
                        break
                if p == 1:
                    break
            # if (hh[:, i] == hh[:, j]).all():
            # if h[i] == h[j]:
            if p == 1:  # 判定可能相似的点，保存其索引值和与待测点的真实距离
                resp.append(j)
                dtemp = dist(data[i], data[j])
                resd.append(dtemp)
    resd = np.array(resd)
    sort_index = np.argsort(resd)
    if(sort_index.shape[0] > 10):
        for ii in range(10):  # 将真实距离最近的10个点加入最终结果
            res.append(resp[sort_index[ii]] + 1)
    else:  # 若可能相似的点不足10个，则将全部可能相似的点加入最终结果
        res = resp
    print(i+1, end='')
    print("的近邻点为：")
    print(res)
    allres.append(res)
time1 = time.time()
print("运行时间：", end='')
print(time1 - time0, end='')
print("秒")

tp = 0
fp = 0
fn = 0
tn = 0
for i in range(num):
    trued = []
    trueres = []
    for j in range(m):
        tdtemp = dist(data[i], data[j])
        trued.append(tdtemp)
    trued = np.array(trued)
    sort_index = np.argsort(trued)
    for ii in range(10):
        trueres.append(sort_index[ii] + 1)
    for each1 in allres[i]:
        p = 0
        for each2 in trueres:
            if each1 == each2:
                tp += 1
                p = 1
                break
        if p == 0:
            fn += 1
tn = (m-10)*num-fn
r = tp/(tp+fn)
p = (tp+tn)/(num*m)
print("准确率：", end='')
print(p)
print("召回率：", end='')
print(r)
