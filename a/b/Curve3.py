#--------------1-------------#
# def f1():
#     f2()
#     print('from f1')
  

# def f2():
#     print('form f2')

# f1()

#-------------2-------------#
# x=0
# def f1():
#     x=1
#     print("---f1---",x)
#     def f2():
#         x=2
#         print("---f2---",x)
#         def f3():
#             x=3
#             print("---f3---",x)
#         f3()
#     f2()
# f1()

#--------------3---------------#
# https://bbs.csdn.net/topics/392301450
# def f1():
#     print('f1')

# def f2(func):
#     print(func)
#     func()    

# print(f2(f1))

#--------------4----------------#
# https://blog.csdn.net/obaking/article/details/46318175
def f1():
    a = 2
    return a

def f2(f1):
    print(f1)
    return f1

print(f1)
print(type(f1))
print(type(f1()))
print(type(f2))
print(f1)
print(type(f2(2)))

