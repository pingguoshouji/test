#字符串的链接和合并
str1 = 'hello'
str2 = 'world'
print(str1 + str2)

url = ['www','python','org']
print('.'.join(url))

#切片
str3 = 'Monday is a busy day'
print(str3[0:7])
print(str3[-3:])
print(str3[::])

#字符串分割
#split
phone_nummber = '400-1966-0327'
print(phone_nummber.split('-'))

#分隔符可以是 ；，
line = 'hello world; python, I,like, it'
import re
print(re.split(r'[;,s]\s*',line))

#判断字符串以什么开头和结尾
filename = 'trace.h'
print(filename.endswith('h'))
print(filename.startswith('trace'))

#字符串查找与匹配
title = 'Life is short, you need Python'
print(title.find('is short'))
print(title.find('or short'))    # -1

import re
mydate = '2018/11/18'
print(re.match(r'\d+/\d+/\d+',mydate))

#字符串的替换
text = 'Life is short, you need Python'
print(text.replace('you','i'))

student = 'Boy 103, girl 105'
print(re.sub(r'\d+','100',student))

#去除两边的空格
line = ' Life is short, you need Python '
print(line.strip())
