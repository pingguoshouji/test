# 一个猜数字的蠢游戏

from random import randint

num = randint(1,100)
# print(num)

a = False

while a != True:


    b = int(input())

    if num < b:
        print("big")
    elif num > b:
        print("small")
    else:
        print('bingo')
        a = True

    # print(num > b)
    # print(b)
    
