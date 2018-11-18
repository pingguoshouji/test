# def buchang():
#     x = 0
#     def bu(m):
#         nonlocal x
#         x = x + m
#         return x
#     return bu

# chang = buchang()
# print(chang(2))
# print(chang(3))

#------------------------------------#
# x = 0

# def step(num):
#     global x
#     x = x + num
#     return x

# print(step(2))
# print(step(3))
# print(step(6))  

#------------------------------------#
x = 0

def step(num):
    def distance(a):
        nonlocal num      #闭包环境变量可以保存上一次调用的状态
        b = num + a
        num = b
        return num
    return distance

y = step(x)
print(y(1))
print(y(3))
print(x)        #不会改变全局变量