#排序  sorted
my_dict={"cc":100,"aa":200,"bb":10}
a = sorted(my_dict.items(),key=lambda x:x[0])
print(type(a))   #list
print(sorted(my_dict.items(),key=lambda x:x[0]))#表示按照key排序
print(sorted(my_dict.items(),key=lambda x:x[1]))#表示按照value排序
print(my_dict)   #本身没有变原始的my_dict本身顺序并没有变,排序是通过sorted()返回了一个新的字典

#导入时排序
from collections import OrderedDict

orderDict=OrderedDict()
orderDict['a']=1
orderDict['b']=2
orderDict['c']=3
print(orderDict)

#取值
my_dict1={"cc":100,"aa":200,"bb":10}
print(my_dict1['cc'])
print(my_dict1['dd'])        #KeyError: 'dd'
print(my_dict1.get('cc','no found'))   

#字典中提取子集
students_score={'jack':80,'james':91,'leo':100,'sam':60}
good_score={name:score for name,score in students_score.items() if score>90}
print(good_score)

#取最值
stocks = {'wanke':25.6,'wuliangye':32.3,'maotai':299.5,'huatai':18.6}
#values()
print(min(stocks.values()))
print(max(stocks.values()))

#zip
new_stocks = zip(stocks.values(),stocks.keys())
print(new_stocks)
print(min(new_stocks))
print(max(new_stocks))

#字典的翻转:dict/itertools
invert_stocks = dict([(v,k)for k,v in stocks.items()])
print(invert_stocks)

#fromkeys  将字典的缺省值为100
adict = {}.fromkeys(('aa','bb','cc'),100)
for k,v in adict.items():
    print(k,v)
