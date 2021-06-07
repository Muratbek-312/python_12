
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# # function_ = ['+', '-', '*', '/', '%', '**', '//']
# function_ = input('Please operation +-*/%**// :')
# if function_ =='*':
#     print(num1 * num2)
# elif function_ =='+':
#     print(num1 + num2)
# elif function_ =='-':
#     print(num1 - num2)
# elif function_ =='/':
#     print(num1 / num2)
# elif function_ =='%':
#     print(num1 % num2)
# elif function_ =='**':
#     print(num1 ** num2)
# elif function_ =='//':
#     print(num1 // num2)
# else:
#      print('Please enter right operation')



while True:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    function_ = input('Please operation +-*/%**// :')
    if function_ =='*':
        print(f'Result: {num1 * num2}')
    elif function_ =='+':
        print(f'Result: {num1 + num2}')
    elif function_ =='-':
        print(f'Result: {num1 - num2}')
    elif function_ == '/' and num2 == 0:
        print('No divison on zero')
    elif function_ =='/':
        print(f'Result: {num1 / num2}')
    elif function_ =='%':
        print(f'Result: {num1 % num2}')
    elif function_ =='**':
        print(f'Result: {num1 ** num2}')
    elif function_ =='//':
        print(f'Result: {num1 // num2}')
    else:
        print('Please enter right operation')
    question = input('Would you like to continue?(yes/no): ')
    if question == 'no':
        break
    else:
        continue

