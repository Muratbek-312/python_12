# # list
# numbers1 = []
# numbers2 = list()
# print(type(numbers1))
# print(type(numbers2))

# numbers = ['makers', ' boot'] *6
# print(numbers)

# """1.range(end)"""
# numbers = list(range(10))
# print(numbers)

# """2.range(start, end)"""
# numbers = list(range(1,10))
# print(numbers)

# """3.range(start, end, step)"""
# numbers = list(range(100,10,-2))
# print(numbers)


# for i in range(1, 11):
#     print(i ** 2)

# """сравнение листов"""
# numbers1 = [1,2,3,4,5,11,12]
# numbers2 = [1,2,3,4,5,11,100]
# print(numbers1>numbers2)


# append()

# guests = []
# list_lenght = int(input('Enter number of guests:'))
# for i in range(list_lenght):
#     guest = input('Enter guest name: ')
#     guests.append(guest)

# print(guests)



# extend(list)
# users = ['Tom', 'Lera']
# user1 = ['Lenny', 'John']
# users.extend(user1)
# print(users)



# users = ['Tom', 'Lera', 'Terry','Jerry']
# users.append('Bob') - Tom, Lera, Bob добавляем Боба в список
# users.insert(0, 'Bob') - включает Боба под индексом 0
# i = users.index('Lera')  - показывает индекс элемента
# users.pop(1) - удаляет по индексу элемент
# users.pop(-1) - удаляет по индексу элемент
# users.clear()  -clear all elements in list
# print(users)

users = ['Tom', 'Lera', 'Terry','Jerry']
users.sort(key=len)
print(users)















