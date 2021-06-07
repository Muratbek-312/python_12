#  1 Task

# password = input('Enter password: ')
# if password.isdigit() and len(password) >=8 :
#     print('Your password is saved')

# if not password.isdigit():
#     print('Enter only numbers')

# if not len(password) >=8:
#     print('Enter at least 8 digits')


# #  2 Task
# point =input('enter your math, literature and history points: ').split(',')
# math = int(point[0])
# litr = int(point[1])
# hist = int(point[-1])

# average = (math + litr + hist) / 3

# if average > 69:
#     print(f'You have access to exams. Your average point is: {round(average, 1)}')
# else:
#     print('You dont have access to exams.')


import random
play = ['Stone', 'Paper', 'Scissors']
my_choice =  input('Your choice:')
comp_choice = random.choice(play)
if my_choice == 'Scissors' and comp_choice == 'Paper':
    print('You win')
elif my_choice == 'Stone' and comp_choice ==    
