# https://segmentfault.com/q/1010000003902146

a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

# [[row[i] for row in a] for i in range(4)]

# # print(a)

# [[t[i] for t in a] for i in range(4)]

# print(a)

[print(i) for i in a]


for i in range(4):
    for row in a:
        row[i]

[row[i] for row in a for i in range(4)]
