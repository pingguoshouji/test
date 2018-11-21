#创建1（列表版）
g = (x * x for x in range(10))    #生成器
for x in g:                       #也可用next()
    print(x)

L = [x * x for x in range(10)]    #列表生成式
print(L)

#创建2（函数版）
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(10))


#没错遇到yield会返回
def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b                    #加上这个，就是生成器
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib_generator(10))           # <generator object fib_generator at 0x0073EE30>

g = fib_generator(10)

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

#Iterable与iterator
from collections import Iterable

print(isinstance([],Iterable))
print(isinstance((x for x in range(5)),Iterable))

from collections import Iterator

print(isinstance([],Iterator))
print(isinstance((x for x in range(5)),Iterator))

