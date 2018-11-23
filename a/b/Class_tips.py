class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
bart.score = 60                         #可以更改值
print(bart.score)   
print(bart.print_score())


#-----------------------------------------------#
class Student1(object):

    def __init__(self, name, score):
        self.__name = name                              #私有变量
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def getname(self):                                  #通过内部方法获取
        return self.__name

    def set_soure(self,score):                          #更改scoure，并作错值判断
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

jack = Student1('jack',18)
jack.score = 20
print(jack.score)                                       #20
print(jack.__score)                                     #AttributeError: 'Student1' object has no attribute '__score'
print(jack._Student1__score)                            #18
print(jack._Student1__name)                             #当name私有化后变为_Student1__name


#----------------------------------------------#
class Student2(object):

    def __init__(self, name, score):
        self._name = name                                         #单下划线实例变量外部是可以访问的，但是约定俗称不访问
        self._score = score

    def print_score(self):
        print('%s: %s' % (self._name, self._score))

jimmy = Student2('jimmy',20)
print(jimmy._name)



#--------------------继承与多态------------------------#
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
class Tortoise(object):
    def run(self):
        print('Tortoise is running slowly...')

cat = Cat()
tortoise = Tortoise()

print(isinstance(cat,Cat))                      #isinstance()判断是否是在类里面

def run_twice(animal):
    animal.run()
    animal.run()

print(run_twice(cat))
print(run_twice(tortoise))


#-------------------------------------------------------------#
class Person(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

class Child(Person):                                # Child 继承 Person
    def __init__(self,name,sex,mother,father):      # 重写父类构造方法
        Person.__init__(self,name,sex)              # 子类对父类的构造方法的调用
        self.mother = mother
        self.father = father

May = Child("May","female","April","June")
print(May.name,May.sex,May.mother,May.father)

class Jimmer(Child):
    def __init__(self,name,sex,mother,father,age):
        Child.__init__(self,name,sex,mother,father)
        self.age = age


jimmer = Jimmer('jimmer','boy','yuanz','yang',18)    #所有参数必须写入


#isinstance() :能用type()判断的基本类型也可以用isinstance()判断
print(isinstance([1,2,3],(list,tuple)))   #可以判断一个变量是否是某些类型中的一种

#dir() :获得一个对象的所有属性和方法

print(len('abc'))
print('abc'.__len__())


#getattr()  setattr()  hasattr()
class Myobj(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = Myobj()
print(hasattr(Myobj,'x'))
print(hasattr(obj,'x'))       # 有属性'x'吗？
print(setattr(obj,'y',19))    # 设置一个属性'y'
print(getattr(obj,'y'))       # 获取属性'y'     如果试图获取不存在的属性，会抛出AttributeError的错误
print(getattr(obj,'z',404))   # 获取属性'z'，如果不存在，返回默认值404

#这些校区，也可以获得对象方法
fn = getattr(obj,'power')
print(fn)
print(fn())


#--------------------------------------------#
class Student4(object):
    name = 'Student'                            # 类属性

    def __init__(self):                         # 实例变量的属性
        self.x = 1


student4 = Student4()
print(student4.name)
print(Student4.name)
student4.name = 'Michael'                        #如此更改，不会更改类属性,只会改变实例变量的属性
print(student4.name)
print(Student4.name)


#当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法
class Student5(object):
    pass

student5 = Student5()
student5.name = 'Michael'
print(hasattr(student5,'name'))
print(student5.name)
s = Student5()
print(s.name)                                   #AttributeError: 'Student5' object has no attribute 'name'
print(student5.name)


#__slots__  限制，实例的属性，只允许对Student实例添加name和age属性,且对子类不起作用
class Student6(object):
    __slots__ = ('name','age')

student6 = Student6()
# student6.score = 99                             #AttributeError: 'Student6' object has no attribute 'score'
try:
    student6.score = 99
except AttributeError as e:
    print('AttributeError:', e)

