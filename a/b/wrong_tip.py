# try...except...finally...
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:          # except: division by zero
    print('except:', e)
finally:
    print('finally...')
print('END')

print(10/0)             # ZeroDivisionError: division by zero


# logging   让程序打打印出错误堆栈，并且继续执行

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

# raise 自己创建错误并抛出
class FooError(ValueError):
    pass

def foo_1(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo_1('0')


#-------------------------------------------------------------------#

def foo1(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar1():
    try:
        foo1('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar1()

# assert 
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')


# logging

