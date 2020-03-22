from collections import Counter  # 统计列表出现次数最多的元素
import decimal
import operator

decimal.getcontext().prec = 1000

print("Input:\n")
inputstr = input()
# print(inputstr + "\n")

res = Counter(inputstr)  # 统计输入的每个字符的个数,res是一个字典类型
# print(res)

M = len(res)
# print(M)

reskeys = list(res.keys())      # 取字典res的键,按输入符号的先后顺序排列
# print("keys:"+str(reskeys))
resvalue = list(res.values())   # 取字典res的值
# print("value:"+str(resvalue))
# totalsum = sum(resvalue)        # 输入一共有几个字符
totalsum = len(inputstr)
# print("totalvalue:"+str(totalsum))
# Creating Table
percentage = list(res.values())
temptotal = decimal.Decimal(totalsum)
tempresval = list(res.values())
for i in range(M):
    tempresval[i] = decimal.Decimal(resvalue[i])
    percentage[i] = tempresval[i]/temptotal
left = []
right = []
left.append(decimal.Decimal(0))
right.append(percentage[0])
# left[0] = 0.0
# right[0] = percentage[0]
i = 1
while i < M:
    left.append(right[i-1])
    right.append(left[i] + percentage[i])
    i += 1
# print(A)

# Encoding

# print("\n------- ENCODING -------\n")
strlist = list(inputstr)
ltag = decimal.Decimal('0')
utag = decimal.Decimal('1')
index = 0
r = decimal.Decimal(1)
for i in range(len(strlist)):
    for j in range(M):
        if(strlist[i] == reskeys[j]):
            index = j
            break
    r = utag - ltag
    utag = right[index] * r + ltag
    ltag = left[index] * r + ltag
tag = (ltag + utag)/decimal.Decimal(2)
s1 = str(ltag)
s2 = str(utag)
for i in range(len(s1)):
    if(s1[i] != s2[i]):
        tag = decimal.Decimal(s2[0:i+1])
        break
# print("\nThe Tag is \n ")
print("\nCode:\n")
print(tag)

# Decoding

# print("\n------- DECODING -------\n")
ltag = decimal.Decimal('0')
utag = decimal.Decimal('1')
ret = []
for i in range(totalsum):
    temp = (tag - ltag)/(utag - ltag)    # 计算tag所占整个区间的比例
    for j in range(M):
        if (float(left[j]) < temp < float(right[j])):   # 判断是否在某个符号区间范围内
            ret.append(str(reskeys[j]))
            ltag = left[j]
            utag = right[j]
            tag = temp

# print("The decoded Sequence is \n ")
print("\nDecoded Sequence:\n")
print("".join(ret))

if(operator.eq(ret, strlist)):
    print("\nCorrect.")
else:
    print("\nWrong.")
