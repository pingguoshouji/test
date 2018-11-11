
# def Curve2():
#     a = 10        #环境变量
#     def Curve():
#         a = 20    #局部变量,不影响其他的，若有这个则不是闭包，闭包是引用环境变量，而不能更改
#         print(a)
#     print(a)
#     Curve()
#     print(a)

# Curve2()

def Curve2():
    a = 10        #环境变量
    def Curve():
        a = 20    #局部变量,不影响其他的，若有这个则不是闭包，闭包是引用环境变量，而不能更改
        return a
    return Curve

print(Curve2())
print(Curve2().__closure__)
