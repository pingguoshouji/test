#type  动态创建一个类
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello',(object,), dict(hello=fn))         #创造class对象

h = Hello()
print(h.hello())
print(type(Hello))
print(type(h))


# metaclass  魔术代码
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

