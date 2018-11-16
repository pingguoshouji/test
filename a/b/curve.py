#闭包：函数+环境变量
# https://www.cnblogs.com/Lin-Yi/p/7305364.html
# https://m.jb51.net/article/86989.htm

def Curve_pre():
    a = 25              #环境变量
    def Curve(x):
        b = a*x
        return b
    # return Curve
    
# t = Curve_pre()
# print(t(2))
print(type(Curve_pre()))

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
