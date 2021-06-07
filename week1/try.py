email = input('Enter your email: ')
emails = ('@gmail.com',
        '@mail.ru',
        '@yandex.ru',
        '@yahoo.com')
if email.endswith(emails):
    print('OK')
else:
    print("Invalid email")
