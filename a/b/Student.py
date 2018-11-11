class Student():
    a = 1

    def __init__(self,name,age,a):
        self.name = name
        self.age = age
        self.a = a 
        # print(Student.a)
        # print(self.__class__.a)

    def print_a(self):
        print(self.a)
        print(self.__class__.a)
        print(self.name)

student1 = Student('YUANZHE',18,2)
student1.print_a()
# print(student1.name)
# print(student1.__dict__)
print(Student.a)
print(Student.a == 1)


