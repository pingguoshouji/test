# raise OSError

# try:
#     x = int(input('Enter the fist number: '))
#     y = int(input('Enter the sevond number: '))
#     print(x/y)
# except:                                         # 可以捕获所有的异常
#     print('There are somethong wrong')


# class MuffledCalculator():
#     muffled = False
#     def calc(self,expr):
#         try:
#             return expr
#         except ZeroDivisionError:
#             if self.muffled:
#                 return('Division by zero is illegal')
#             else:
#                 raise

# calculator = MuffledCalculator()
# calculator.muffled = True
# calculator.calc('1/0')

# try:
#     x = int(input('Enter the fist number: '))
#     y = int(input('Enter the sevond number: '))
#     print(x/y)
# except (ZeroDivisionError,NameError):                                        
#     print('There are somethong wrong')
# print('111')

# try:
#     x = int(input('Enter the fist number: '))
#     y = int(input('Enter the sevond number: '))
#     print(x/y)
# except (ZeroDivisionError,TypeError,NameError) as e:                                        
#     print(e)


while True:
    try:
        x = int(input('Enter the fist number: '))
        y = int(input('Enter the sevond number: '))
        print(x/y)
    except Exception as e:
        print('Inalid input:',e)
        print('Please try again')
    else:
        break




