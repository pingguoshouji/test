from enum import Enum
from enum import IntEnum   #要求数据类型为数值
from enum import unique    #装饰器，强制数值不能重复
# from types import MappingProxyType

@unique
class COLOR(Enum):
    RED = 1       #常量大写
    GREEN = 2
    BULE = 3

# print(COLOR.RED.value)   #输出所对应的值
print(COLOR.RED)         #COLOR 下面的类型
print(COLOR['RED'])
print(COLOR(1))
# print(COLOR.RED.name)    #名字
# print(type(COLOR.RED.name))   #<class 'str'>
# print(type(COLOR.RED))        #<enum 'COLOR'>
print(type(COLOR.RED.value))

#遍历
# for c in COLOR:
#     print(c)

#便利出元素
# for c in COLOR.__members__.items():
#     print(c)

# for c in COLOR.__members__:
#     print(type(c))

# print(type(COLOR.__members__))
#通过数值访问表情
# a = 1
# print(COLOR(a))


#较为简单的枚举
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# @unique
# class Month(Enum):
#     Sun = 0 # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6

for name,member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

