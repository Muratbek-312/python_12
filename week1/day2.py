# Task 1
# speed = int(input('Enter speed: '))
# distance = int(input('Enter distance: '))
# time = distance / speed
# print('Time for reaching place: ' + str(time))


# name = input('Enter your name: ')
# age = input('Enter your age: ')
# surname = input('Enter your surname: ')
# print(f'Hello, Your surname is {surname}, your name is {name} and your age is {age} years old')


# Task2
# import random
# list_ = random.sample(range(100), 10)
# if 3 in list_:
#     print('Yes')
# else:
#     print('No')
# print(list_)

# Task3
# product_amount = int(input('Enter amount of product: '))
# product_price = int(input('Enter price off the prooduct: '))
# total = product_amount * product_price
# print(f'Total price:{total}')

# Task4
d = input('Choose diameter of your pizza: (30,,40, 50):')
count = input('How many pizzas do you want to order? :')
price_per_one = 0
if d == '30':
    price_per_one = 500
elif d == '40':
    price_per_one = 600
elif d == '50':
    price_per_one = 700
else:
    print('There is no such size')
total = int(count) * price_per_one
print(f'Total price is {total}$')

