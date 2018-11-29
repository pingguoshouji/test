# 文件读
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()


with open('/path/to/file', 'r') as f:
    print(f.read())


with open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore') as f:
    for line in f:                     # in mf.readlines()
        print(line.strip())            # 把末尾的'\n'删掉

# 文件写
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')


# StringIO :在内存中读写str。
from io import StringIO
f1 = StringIO()
print(f1.write('hello'))
print(f1.getvalue())                    # 获得写入后的str
# 读取
f2 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())                    # 如果不带参数，默认是清除两边的空白符

