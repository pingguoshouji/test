#默认参数
#默认参数必须指向不变对象
def add_end(L=None):
    if L == None:
        L = []
    L.append('END')
    return L

print(add_end([1,2,3]))
# print(add_end())
# print(add_end())

def add_end_bug(L=[]):
    L.append('end')
    return L

print(add_end_bug())
print(add_end_bug())

#可变参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
def cale(*number):
    sum = 0
    print(type(number))             # <class 'tuple'>
    for i in number:
        sum = sum + i*i
    return sum

print(cale(1,2,3))
# print(cale([1,2,3]))                # can't multiply sequence by non-int of type 'list'
print(cale(*[1,2,3]))

#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Bob', 35, city='Beijing')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('jack', 24,**extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

#命名关键字参数
#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person1(name, age, *, city, job):
    print(name, age, city, job)

person1('Jack', 24, city='Beijing', job='Engineer')

#可以有默认值
def person2(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person2('Jack', 24, job='Engineer')

#组合参数
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


#递归函数
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(10))

#尾递归
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(10))


#返回多个值与丢弃
def getRoomData():
	return 'class room is 203',1000,'2016-10-06'

a = getRoomData()         #将返回值以元组的形式返回回来
print(a)
a,b,c = getRoomData()
_,a,_ = getRoomData()     #将不需要的值赋值给一个几乎用不到的变量名，可以将不用的数值丢弃
print(a)

#尽量用异常表示特殊情况，不要返回None
#利用try，except
def divide(a,b):
	try:
		return True,a/b
	except ZeroDivisionError:
		return False,None

print (divide(0,10))


