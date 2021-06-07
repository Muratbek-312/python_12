# a = int(input("Enter your number:"))
# print( a > 5 if True else False)


# a = input("Enter data:")
# b = len(a)
# print( b >= 5 if True else False)

# a = int(input("Enter your point:"))
# if a >= 90:
#   print('Great job. Your point is 5')
# elif a >= 80:
#   print('Cool! Your point is ')
# elif a >= 70:
#   print('Good! Your point is 3')
# elif a >= 60:
#   print('You should study harder')
# else:
#   print('You failed exam.')

# a = int(input("Enter your number: "))
# if a > 0:
#   print('Your number is positive.')
# elif a < 0:
#   print('Your number is negative.')
# else:
#   print('Your number is Zero')

# a = 10
# b = 9
# if a<b:
#   print(a)
# else:
#   print(b)



# a = 900
# b = 700
# c = 600
# if a<b and b<c:
#   print(a)
# elif b<a and a<c:
#   print(b)
# else:
#   print(c)



# a = int(input('Enter number: '))
# b = int(input('Enter number: '))
# if b == 0:
#     print('Zero error. Cant be divided by zero')
# elif a // b != 0: 
#      print(f'{a} cant be divided by {b}')
#      print('Quoitent:', a // b)
#      print('Remain:' , a % b)


# a = int(input('Enter data:'))
# b = input('Enter bytes or kilobytes. Type b or kb: ')
# if b == 'b':
#   print('Result:', a / 1024)
# elif b == 'kb':
#   print('Result:', a * 1024)


# a = int(input('Enter number in range 1 - 256:'))
# print(chr(a))


# a = int(input('Enter number: '))
# b = int(input('Enter number: '))
# c = int(input('Enter number: '))
# if a == b and b == c:
#   print('3')
# elif a==b or c==b or a==c:
#   print('2')
# else:
#   print('0')

# a = int(input('Enter a year:'))
# if (a%4==0 and a%100!=0) or a%400==0:
#   print('YES')
# else:
#   print('NO')

# n = int(input('Enter number: '))
# m = int(input('Enter number: '))
# k = int(input('Enter number: '))
# if k < n * m and ((k % n == 0) or (k % m == 0)):
#     print('YES')
# else:
#     print('NO')

"""Посчитайте возраст собаки в собачьих годах. Введите возраст в человеческих годах, 
переведите в собачьи и распечатайте. Формула перевода следующая: Первые 2 года жизни равны 10.5 собачьих лет.
 Далее каждый год равен 4 годам.
"""

# h_age = int(input('How many years your dog love?: '))
# d_age = h_age*10.5 if h_age<=2 else (h_age-2)*4+21
# print(d_age)


# a1= int(input('Enter number: '))
# b1= int(input('Enter number: '))
# a2= int(input('Enter number: '))
# b2= int(input('Enter number: '))
# 5
# 4
# if abs(a1-a2) == abs(b1-b2):
#   print('YES')
# else:
#   print('No')

a1= int(input('Enter number: '))
b1= int(input('Enter number: '))
a2= int(input('Enter number: '))
b2= int(input('Enter number: '))
5
4
if a1 == a2 or b1==b2 :
  print('YES')
else:
  print('No')