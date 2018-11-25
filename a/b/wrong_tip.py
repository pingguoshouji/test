# try...except...finally...
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:          # except: division by zero
    print('except:', e)
finally:
    print('finally...')
print('END')

print(10/0)             # ZeroDivisionError: division by zero