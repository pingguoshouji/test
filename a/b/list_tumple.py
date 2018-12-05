#list与tumple用法一模一样
#增加
alist = ['a','b','c']
alist[1] = 'd'
print(alist)

#append 增加到末尾
alist.append('D')   
print(alist)

#insert
alist.insert(2,'e')
print(alist)

#删除
del alist[0]
print(alist)

#remove
alist.remove('c')

#删除队尾的
alist.pop()
print(alist)

#sort  排序
blist = [1,2,5,3,8,6]
blist.sort(reverse=False)         #小到大
# blist.sort(reverse=True)
print(blist)

#len()
aList=[1,2,3,4,5]
print(len(aList))

#最大最小值
aList=[1,2,3,4,5]
print(len(aList))
print(max(aList))

#列表扩展  extend
#与+号的区别：区别在于+是返回一个新的列表，而extend是直接修改了列表
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

#查找索引 index
aList=['This','is','a','very','good','idea']
print(alist.index('very'))

#计数 count
aList=['to','do','or','not','to','do']
print(aList.count('to'))

# 拆分元组
tup = 1,2,(3,4)
# a,b,c = tup
a,b,(c,d) = tup
print(c)

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print('a={0}, b={1}, c={2}'.format(a, b, c))


seq = [7, 2, 3, 7, 5, 6, 0, 1]
print(seq[:5])
print(seq[-6:-2])

# enumerate
some_list = ['foo', 'bar', 'baz']
# a = enumerate(some_list)
# print(a)                                             # <enumerate object at 0x00DC9878>

# print(list(enumerate(some_list,start=1)))
# for i,v in enumerate(some_list):
#     print(i,v)
    # print(dict(i,v))                                   # TypeError: dict expected at most 1 arguments, got 2

mapping = {}
for i,v in enumerate(some_list):
    mapping[v] = i
    print(mapping[v])

print(mapping)
# print(mapping[i])


#
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}

for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)

print(by_letter)


# defaultdict
# https://blog.csdn.net/the_little_fairy___/article/details/80551538
from collections import defaultdict
a=dict()
b=defaultdict(int)
print(b["a"])

# 集合推导式
result = set()      # 创建空的集合

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
for i in strings:
    result.add(len(i))

print(result)

unique_lengths = {len(x) for x in strings}
result = set(map(len, strings))


students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted(students, key=lambda student : student[2])
print(students)

# 
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x: len(set(list(x))))
print(strings)
