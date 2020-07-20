import numpy as np
import pandas as pd
import heapq
import time

time0 = time.time()
capre = pd.read_csv("C:\\Users\\asus\\Desktop\\大三下\\媒体数据管理\\第五次实验\\CA\\real.txt", header=None, encoding='utf-8', sep=' ')
ca = np.array(capre)
ca = ca[:, -2:]
# data = data[0:1000]
cak = ca.shape[1]
can = ca.shape[0]


class Node:
    def __init__(self, data, sp, left=None, right=None):
        self.data = data  # 该节点对应的二维数据
        self.sp = sp  # 用0/1维数据作为切分依据
        self.left = left  # 左子节点
        self.right = right  # 右子节点


class KDTree:
    def __init__(self, data):
        k = data.shape[1]

        def create(dataset, sp):
            if len(dataset) == 0:
                return None
            # sort by current dimension
            dataset = sorted(dataset, key=lambda x: x[sp])
            mid = len(dataset)//2
            # split by the median
            dat = dataset[mid]  # 切分点
            return Node(dat, sp, create(dataset[:mid], (sp+1) % k), create(dataset[mid+1:], (sp+1) % k))
        self.root = create(data, 0)

    def nearest(self, x, near_k=1):
        self.knn = [(-np.inf, None)]*near_k

        def visit(node):
            if node is not None:
                # 判断目标节点在当前节点哪个方位，计算目标点距坐标轴的距离
                dis = x[node.sp] - node.data[node.sp]
                # 根据计算值决定方位左/右子节点
                visit(node.left if dis < 0 else node.right)
                # 计算目标点与当前点的距离
                curr_dis = np.linalg.norm(x-node.data, 2)
                # 引入堆排序，将上一步计算的距离压入knn，然后将堆内距离最大的弹出
                heapq.heappushpop(self.knn, (-curr_dis, node))
                # 如果真实距离大于距坐标轴的距离，访问其兄弟节点
                if -(self.knn[0][0]) > abs(dis):
                    visit(node.right if dis < 0 else node.left)
        visit(self.root)
        self.knn = np.array([i[1].data for i in self.knn])  # 输出每一个元组中节点对应的二维数据
        return self.knn


# sort_index = np.lexsort(ca[:, ::-1].T)
# sortca = ca[np.lexsort(ca[:, ::-1].T)]
# div = int(np.median(sort_index))
# caroot = Node(sortca[div], 0)
catree = KDTree(ca)
print("Input:")
time1 = time.time()
inputstr = input()
time2 = time.time()
target = int(inputstr)
cat = ca[target]
print(cat)
print("---------------------------")
print("CA:")
knn = catree.nearest(cat, 2)
for each in knn:
    if(each != cat).any():
        print(each)
# print(catree.nearest(cat))
time3 = time.time()
time = time3-time2+time1-time0
print("运行时间："+str(time)+"秒")
