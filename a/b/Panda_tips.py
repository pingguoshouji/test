import numpy as np
import pandas as pd
from pandas import  Series,DataFrame

obj = pd.Series([4, 7, -5, 3],index=['d', 'b', 'a', 'c'])

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj2 = pd.Series(sdata,index=states)
obj2.name = 'abj2'
obj2.index.name = 'state'

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame = pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one', 'two', 'three', 'four','five', 'six'])
frame['debt'] = np.arange(6.)
# frame['state']
# frame.loc['three']     #获取行
vla = pd.Series([-1.2, -1.5, -1.7],index=['two', 'four', 'five'])
frame['debt'] = vla
frame['eastern'] = frame2.state == 'Ohio'

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
    'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame2 = pd.DataFrame(pop)
frame2.T

pdata = {'Ohio': frame2['Ohio'][:-1],
    'Nevada': frame2['Nevada'][:2]}
pd.DataFrame(pdata)

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])


obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3.reindex(range(6),method = 'ffill')

obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
new_obj


pop2 = {'Nevada': {2001: 2.4, 2002: 2.9},
    'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
obj2 = pd.DataFrame(pop2)
new_obj2 = obj2.drop('Ohio',axis=1)
new_obj2
