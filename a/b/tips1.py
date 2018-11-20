#++1    Python的解释器会将++i操作为+(+i).其中+表示是正数符号,对于--i也是类似的.
print(++1)
print(+++1)
print(++++1)

# == 与 is
# is是对象的标示符,用来比较两个对象的内存空间是不是一样，是不是用的同一块空间地址，而==是比较两个对象的内容是否相等.

# 连接大规模字符串：join  效率比‘+’高好多
str1,str2,str3='test ','string ','connection'
print(''.join([str1,str2,str3]))

# copy
a=[1,2,3]
b=a
b.append(4)
print(id(a),a)
print(id(b),b)

import copy
a=[1,2,3]
b=copy.copy(a)
b.append(4)
print('a:',a)
print('b:',b)


