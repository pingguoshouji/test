#装饰器
import functools

def log(func):      
    @functools.wraps(func)                  #因为函数名被改变，会有要加这个
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log                    # now = log(now)
def now():
    print('haha')

# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
# 只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，
# 即在log()函数中返回的wrapper()函数。
now()

print(log.__name__)
print(now.__name__)


#-------------------------#
import time

# def decorator(func):
#     def wrapper():
#         print(time.time())
#         func()
#     return wrapper

def wrapper(func):
    print(time.time())
    func()

@wrapper
def f1():
    print('hahaha')

f1()
