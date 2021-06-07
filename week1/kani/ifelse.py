# number = int(input('Enter your number: '))
# if number > 0:
#     print('This number is positive')
# elif number < 0:
#     print('This number is negative')
# else:
#     print('This is equal 0')


# string = 'The creator of Python is Guido Van Rossum'
# if 'python' and 'javascript' in string.lower():
#     print('YES')
# else:
#     print('NO')

# a = 200
# b = 200
# c = 700
# if a>b and c>a:
#     print('Both condition are right')
# elif a>c or c>b:
#     print('At least one condition is right')
# else:
        # print('OK')

# тернарный оператор
# method1

# a = 9   
# b = 10
# if a<=b:print('a less or equal b')

# # method2 
# a =500
# b = 333
# c = None
# # print('makers') if a>b else print('Bootcamp')
# c = 'Aykol' if a>b else 'Nazarbek'
# print(c)

# example
# a = input('Your age: ')
# c = None
# c = 'access is available' if int(a)>18 else ('access is not available')
# print(c)


# example
# age = int(input('Your age: '))
# print('access is available') if age > 18 else print('access is not available') if age < 18 else print ('OK')

# Inserted if-else
# x=15
# if x > 10:
#     print('Larger 10')
#     if x > 20:
#         print('Larger 20')
#     else:
#         print('Till 20')


# pass - пропучти, дай подумаю
# a = 200
# b = 33
# if a>b:
#     pass
# print('Hello')





# форматирование строк
# 1 method
# name = input('Enter name: ')
# string = f'Hi, {name}'
# print(string)



# 2method
# name = input('Enter name: ')
# age = input('Enter age: ')
# string = 'Hi, {1}! Your age is {0}'.format(age, name)
# print(string)


# # 3method
# name = input('Enter name: ')
# string = 'Hi, %s' % name
# print(string)

# for i in range(0, 1000):
#     if i % 2 ==0:
#         print(f'This number is even {i}')



# for i in range(1, 1000, 2):
#     print(i)


# string = 'MakersBootcampPython12'
# newstring = string[::2]
# print(newstring)