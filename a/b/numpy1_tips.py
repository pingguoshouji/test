import numpy as np

data = np.random.randn(7,4)             # 生成正态分布的随机数据
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

# a = names == 'Bob'
# print(a)

# 布尔型索引
# print(data[names == 'Bob', 2:])                 # 选取了names == 'Bob'的行，并索引了列

# print(data[(names == 'Bob') | (names == 'Will'), 2:])

# 花式索引
arr1 = np.empty((8, 4))
for i in range(8):
    arr1[i] = i

# print(arr1[[4, 3, 0, 6]])
# print(arr1([-4, -3, -0, -6]))                #负数会从尾部进行索引

# 
arr2 = np.arange(32).reshape((8,4))             #reshape：改变数组形状  返回视图
# print(arr2[[1, 5, 7, 2], [0, 2, 1, 3]])


# 转制
arr3 = np.arange(15).reshape(3,5)
print(arr3.T)


print(arr1[[4, 3, 0, 6]])

# 将条件逻辑表述为数组运算
import numpy as np
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result1 = [(x if c else y)for x, y, c in zip(xarr, yarr, cond)]
result2 = np.where(cond, xarr, yarr)

print(result2)

import numpy as np

arr2 = np.random.randn(5,4)
print(arr2)
print(arr2.sum(axis = 2))               # numpy.core._internal.AxisError: axis 2 is out of bounds for array of dimension 2


import numpy as np

arr3 = np.random.randn(100)
print((arr3>0).sum())
