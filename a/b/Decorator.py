#装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# def wrapper(*args, **kw):
#     print('call %s():' % func.__name__)
#     return func(*args, **kw)

@log
def now():
    print('haha')

now()
