#闭包：函数+环境变量
# https://www.cnblogs.com/Lin-Yi/p/7305364.html
# https://m.jb51.net/article/86989.htm
# https://m.jb51.net/article/65009.htm

def Curve_pre():
    a = 25           #环境变量
    def Curve(x):
        a = 20
        b = a*x
        return b
    # print(a)
    return Curve

t = Curve_pre()
print(t)
print(t.__closure__)
# print(t(2))
# print(type(t(2)))               #int
# # print(type(Curve_pre()))      #function
# print(Curve_pre())

# print(Curve_pre(2))                    #这样子会报错
# print(t.__closure__[0].cell_contents)  #输出环境变量
# print(t.__closure__)                   #输出变量类型在内存中的地址

#--------------------------------------#

# def Curve_pre(x):
#     a = 25              #环境变量
#     def Curve():
#         # a =20
#         b = a*x
#         return b
#     return Curve
    
# t = Curve_pre(2)
# print(t())
# print(t)

#--------------------------------------#

# a = 25 

# def Curve_pre(x):
                
#     a = Curve(x)
#     return a
    
# def Curve(x):
#     b = a*x
#     return b

# t = Curve_pre(2)
# print(t)

#-------------------------------------#
# def count():
#   fs = []
#   for i in range(1, 4):
#     def f():
#        return i*i
#     fs.append(f)
#   return fs

# f1,f2,f3 = count()

# # f1 = count()
# # print(f1)         #不能print(f1())

# print(f1())
# print(f2())
# print(f3())

#----------------------------------#

# def f1():
#     a = 10
#     def f2():
#         a = 20
#         print(a)
#         # return a
#     print(a)
#     f2()
#     print(a)

# f1()


#----------------------------------#
def f1():
    x = 100
    def f2():
        print(x)
    # f2()
    # return f2

print(f1())
print(f1)

# a = f1()
# print(a())
