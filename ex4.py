import os
import cv2
import numpy as np

# path = "D:/py/cifar-10/test/0"
# files = os.listdir(path)
# count = 0
# for file in files:
#     if(file.lower().endswith(('.jpg'))):
#         count += 1
#         dir = path + "/" + file
#         img1 = cv2.imread(dir)
#     if count == 1:
#         break
dir = "D:/py/cifar-10/test/0/0_3.jpg"
img1 = cv2.imread(dir)
# 提取特征点
# 特征点描述
# 匹配

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)   # des是描述子
path = "D:/py/cifar-10/train"
folders = os.listdir(path)
count = 0
mm = 0
for folder in folders:
    dir = path + "/" + folder
    if os.path.isdir(dir):
        files = os.listdir(dir)
        for file in files:
            if(file.lower().endswith(('.jpg'))):
                dir2 = dir + "/" + file
                img2 = cv2.imread(dir2)
                if(img2 is not None):
                    kp2, des2 = sift.detectAndCompute(img2, None)  # des是描述子
                    if len(kp2) > 0:
                        bf = cv2.BFMatcher()
                        match = bf.match(des1, des2)  # 得到最佳匹配
                        dist = 0
                        for each in match:  # 最佳匹配之间距离的总和
                            dist += each.distance
                if count == 0:
                    mm = dist
                if(dist < mm):
                    mm = dist  # 总和最小的，保存其总和与图片地址
                    resdir = dir2
                count += 1
                print(count)
    #         if count == 20:
    #             break
    # if count == 20:
    #     break
if mm > 0:
    print(mm)
    print(resdir)
    img = cv2.imread(resdir)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
