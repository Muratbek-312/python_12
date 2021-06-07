# # 1
# string = 'Azamat is an amazing actor.'
# # print(string.replace('a','*')) - чувствителен к регистру
# list_ = list(string)  
# for letter in list_:
#     # print(letter)
#     if letter.lower()=='a':
#         index = list_.index(letter)
#         list_.remove(letter)
#         list_.insert(index, '*')
# new_string =''.join(list_)
# print(new_string)


# 2 method

# string = 'Azamat is an amazing actor.'
# list_=[]
# for letter in string:
#     if letter.lower()=='a':
#         list_.append('*')
#     else:
#         list_.append(letter)
# new_string =''.join(list_)
# print(new_string)



# 3
# list_lenght =int(input('How many elements do you want to include in list? : '))
# list_ = []
# while list_lenght > 0:
#     element = input('Enter your element: ')
#     list_.append(element)
#     list_lenght -=1 #=list_lenght -1
# print(list_)



# # 4
# list_ = [
#     ['sher1234','qwerty'],
#     ['beka789', 'sdf45'],
#     ['hahah34','456786sd']
# ]
# # for inner_list in list_:
# #     for i in inner_list:
# #         print(i)
# #     print('----------')

# users = []
# for user in list_:
#     users.append(user[0])
# print(users)

# username = input('enter your username: ')
# if not username in users:
#     password= input('enter passwor: ')
#     list_.append([username, password])
# else: print('username exists.Enter another:')

# print(list_)


# 5
# append(), pop()
# insert()
# FIFO, FILO
# First in, first out
# First in, last out

from collections import deque
queue = deque(['Saadat', 'Begayim', 'Kalys', 'Aykol'])
person = queue.popleft()
print(person)
print(queue)

queue.appendleft('Chika')
print(list(queue))



