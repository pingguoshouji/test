# # https://www.cnblogs.com/benric/p/4965224.html  formate
# # http://www.runoob.com/python/att-string-format.html
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}\t'.format(i,j,i*j),end='')
#         # print('{} * {} = {}'.format(i,j,i*j),end=' , ')
#     print()

site = {'name':'new ','url':'www.runoob.com'}
print('name:{name}  url:{url}'.format(**site))
