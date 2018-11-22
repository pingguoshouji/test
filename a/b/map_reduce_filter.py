#map
def f1(x):
    return x*x

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = map(f1,b)        
print(list(a))          #map返回的是一个Iterator，需用list（）计算
print(map(f1,b))

#reduce
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

from functools import reduce
def add(x,y):
    return x+y

a = reduce(add,b)
print(a)

#--------------------------------------------#
from functools import reduce

def str_int(num):
    def fn(x,y):
        return x*10+y

    def charnum(num):
        DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return DIGITS[num]

    return reduce(fn,map(charnum,num))

print(str_int('123'))

#filter:用于过滤序列,回的是一个Iterator
def is_odd(n):
    return n % 2 == 1

a = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(a)

#sorted  排序
print(sorted([36, 5, -12, 9, -21], key=abs))
