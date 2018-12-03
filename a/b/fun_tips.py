# 数据内存形式
# https://blog.csdn.net/u014248127/article/details/79170958
def  append_element(some_list,element):
    # print(id(some_list))
    a_list = some_list
    # print(id(a_list))
    a_list = a_list.append(element)
    # print(a_list.append(element))
    return a_list 

data = [1,2,3]
append_element(data,4)
# print(id(data))
# print(append_element(data,4))
# print(id(data))
print(data)


# 函数传参
x = 20
s = '世界你好'
def test(x,s):
    x = 40
    s = "hello world"
test(x,s)
print(x,s)


a = [1,2,3]
print(id(a))
a.append(4)
print(a.append(4))

x = (1,2,3)
print(id(x))
y = (1,2,3)
print(id(y))


