# # # string = 'Jibek'
# # # print(string[0])


# # # string = 'Jibek'
# # # print(string[-2:])
# # string = 'Jibek'
# # print(string[::-1])

# string = 'Jibek '
# print(string * 4)

# string = 'Jibek'
# x = len(string)
# print(x)

# string = "The quick brown fox jumps over the lazy dog"
# print(string.replace('o','*'))

# string = "The quick brown fox jumps over the lazy dog"
# print(string.upper())
# string = "The quick brown fox jumps over the lazy dog"
# print(string.lower())

# string = 'Jibek'
# start = string[0]
# end = string[-1]
# result = end + string[1:-1] + start
# print(result)   
# string = '#makers#bootcamp#программирование#it#курсы'
# print(string.replace('#', '\n'))


# string = input('Enter your name: ')
# string1 = input('Enter your surname: ')
# string2 = input('Enter your age: ')
# string3 = input('Enter your city: ')
# print(f'Your name is {string} {string1}. You are {string2} years old. You live in {string3} city.')

# string = 'Makers bootcamp'
# print(string[1::2])

# string = 'abracadabra'
# print(string.replace('a','K',3)

# string = 'abracadabra'
# string2 = string.replace(string[5:5], 'K', 1)
# print(string2)

# string = 'abracadabra'
# string2 = string.replace('[5:6]', 'k')
# print(string2)

string = 'abracadabra'
new = list(string)
new[5] = 'K'
print (''.join(new))