# #输出0-100的偶数
# for i in range(2,102,2):
#     print(i)

# j = 0
# while(j<=98):
#     j = j + 2
#     print(j)

# j = 1
# while j<=100:
#     if j % 2 == 1:
#         # j = j + 1
#         continue
#     else:
#         print(j)
#         j = j + 1


# #输出1-100的合
# sum = 0
# for i in range(1,101):
#     sum = sum +i
# print(sum)

#输出1=100中偶数的合
a = 0

for i in range(2,102,2):
    a = a + i
print(a)

#----------------------------------#
sums1 = 0

for i in range(1,101):
    if i%2==0:
        sums1+=i
print(sums1)

#输出1-100质数
i=2
for i in range(2,100):
    j=2
    for j in range(2,i):
        if i %j ==0:
            break
    else:
            sums3+=i
print(sums3)
