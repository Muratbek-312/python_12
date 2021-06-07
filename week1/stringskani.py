# # indexes
# string = 'Hello! We are Python Vol.12'
# print(string[0])
# print(string[9])
# print(string[14])

# # slice
# string = 'Hello! We are Python Vol.12'
# print(string[0:5])
# print(string[-2:])
# print(string.index('Python'))


# polyndrome
# string = input('Enter word: ')
# if string.lower() == string[::-1].lower():
#     print('this word is polyndrome')
# else:
#     print('This word is not polyndrome')

# while True:
#     password = input('enter your password: ')
#     if len(password) < 8:
#         print('Too short password')
#     elif password.isalpha() or password.isdigit():
#         print('Please enter letters and numbers as well')
#     elif password.islower():
#         print('Enter at least one upper letter')
#     else:
#         print('Password is saved')
#     print(password.isalpha())
#     break


# email = input('Enter your email: ')
# emails = ('@gmail.com',
#         '@mail.ru',
#         '@yandex.ru',
#         '@yahoo.com')
# if email.endswith(emails):
#     print('OK')
# else:
#     print("Invalid email")


# string = 'Beautiful is better than ugly.'
# for k in string:
#     print(k.upper()*5)

i =10
while i>0:
    print('Makers')
    