import numpy as np

data = np.random.randn(7,4)             # 生成正态分布的随机数据
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

# a = names == 'Bob'
# print(a)

# 布尔型索引
# print(data[names == 'Bob', 2:])                 # 选取了names == 'Bob'的行，并索引了列

# print(data[(names == 'Bob') | (names == 'Will'), 2:])

# 花式索引
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i

print(arr[[4, 3, 0, 6]])
print(arr([4, 3, 0, 6]))

