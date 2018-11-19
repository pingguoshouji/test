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


