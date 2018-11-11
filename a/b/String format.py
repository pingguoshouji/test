age = 18
print('my age is' + ' ' + str(age))
print('my age is %d'%age )  # %d会被%后面的值替换 %d只能替换整数

price = 17.2
print('Price is %f'%price)  # %f只能替换小数
print('price if %.1f'%price) # 保留几位小数

name = 'yuan'
print('%s is a good teacher'%name) # %s可替换字符
print(name + ' is a good teacher')

print("%s's score is %d"%('yuan',100)) 

print(bool('-123'))
print(bool('0'))
print(bool('abc'))
print(bool('false'))
print(bool(''))
