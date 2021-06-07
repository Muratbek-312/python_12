# print(type(4 > 3))

# print('makers' > 'bootcamp')

# ord()
# print(ord('m'))
# print(ord('M'))
# print('m' > 'M')
# print(ord('b'))


# chr()
# print(chr(109))

# print(type(True))
# print(type(False))

# a = True
# b= False
# print(int(a))
# print(int(b))

# print(bool(3.4))
# print(bool(-200))
# print(bool(0))
# print(bool(' '))
# print(bool(""))

# False: 0, "", [], {}, set(), frozenset(). None, False
# > < <= >= == !=

# a = 10
# b = 7
# c = a==b
# print(c) # False


# # and, or
# a=15
# b=25
# print(a>=15 and b<30)   #True
# print(a==15 or b>30)    #true
# print(a!=15 or b>30)   #false



#  not
# x = 20
# print(not x == 10)

# a = True
# b= False
# print(not a)
# print(not b)


#  if, elif, else
# a = 25
# if a > 20:
#     if a > 30:
#         print('a is greater than 30')
#     else:
#         print('a is greater than 20')
# elif a ==20:
#     print('a is equal 20')
# else:
#     print('a is less than 20')


# a = 10
# b = 5
# c = 25
# if not (a>b or b>c):
#     print("MAKERS")
# else:
#     print('makers')

# list_ = [11,42,64,59]
# if not 20 in list_ and 11 in list_:
#     print('YES')


# тернарный оператор

# """ epression_true if condition else expression_false"""

# a = True  
# print( a if True else False)


# a = 'MAKERS'
# b = 10
# print(a if b else 'makers')

"""(expression_false, expression_true)[condition]"""

# a = 10
# print(('negative', ' positive')[a>=0])


# Nonetype

# None

# print(type(None))
# null_variable = None
# not_null_variable = 'MAKERS'






# #  1 Task

# password =input('Enter password: ')
# if password.isdigit() and len(password) >=8:
#     print('Your password is saved')

# if not password.isdigit:
#     print('Enter only numbers')

# if not len(password) >=8:
#     print('Enter at least 8 digits')


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
# function_ = ['+', '-', '*', '/', '%', '**', '//']
function_ = input('Please operation +-*/%**// :')
if function_ =='*':
    print(num1 * num2)
elif function_ =='+':
    print(num1 + num2)
elif function_ =='-':
    print(num1 - num2)
elif function_ =='/':
    print(num1 / num2)
elif function_ =='%':
    print(num1 % num2)
elif function_ =='**':
    print(num1 ** num2)
elif function_ =='//':
    print(num1 // num2)
else:
     print('Please enter right operation')