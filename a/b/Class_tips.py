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

