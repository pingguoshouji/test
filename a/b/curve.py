#闭包：函数+环境变量

def Curve_pre():
    a = 25              #环境变量
    def Curve(x):
        b = a*x
        return b
    return Curve
    
t = Curve_pre()
print(t(2))
print(t.__closure__[0].cell_contents)  #输出环境变量
print(t.__closure__)                   #输出变量类型在内存中的地址
