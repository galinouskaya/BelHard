# number = 6
# word = input('enter: ')

# if number % 2:
# # if number % 2: ==1:   или так
#     print('odd')
# if word.isdigit():
#      word = int(word)
#      print('digit')
# elif word.isalpha():
#     print('word')
# elif word.isalnum():
#     print('letters and numbers')
# else:
#     print('symbols')

#                   тернарный оператор

# number = 5
# is_even = 'нечетное' if number  % 2 else 'четное'
#
# if number %2:
#     is_even = 'нечетное'
# else:
#     is_even = 'четное'

#



#  Циклы

# for i in range(1, 10, 2):  #1 3 5 7 9
#     i**= 2
#     print(i)

# numbers = [2, 5, 3, 5, 6, 9]
# итерация по индексам
# for i in range(len(numbers)):
#     print(numbers[i])

# итерация по элементам
# for number in numbers:
#     print(number)

# итерация по индексам и ключам одновременно
# for i, val in enumerate(numbers):
#     print(f'на индексе: {i} значение: {val}')

# data = {'name': 'vasia', 'email': 'vasia@info'}
# for val in data.values():
#     print(val)


# data = {'name': 'vasia', 'email': 'vasia@info'}
# for key, val in data.items():
#     print(key, val)


#      continue and break

# numbers = [1, 3, 6, 0, 2, 0, 4]
# for number in numbers:
#     if number == 0:
#         continue
#     number **= 2
#     print(number)

#
# numbers = [1, 3, 6, 0, 2, 0, 4]
# for i, number in enumerate(numbers):
#     if number == 0:
#         continue
#     numbers[i] = number ** 2
# print(numbers)

# numbers = [1, 3, 6, 0, 2, 0, 4]
# for i, number in enumerate(numbers):
#     if number == 10:
#         break
#     numbers[i] = number ** 2
# else:
#     print('закончился самостоятельно')
# print(numbers)


#    цикл  while

# n = 100
# while n!= 0:
#     n = n-1
#     print(n)


#           обработка ошибок
# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
# except ValueError:
#     print('ты ввел не число')
# except ZeroDivisionError:
#     print('на ноль делить нельзя')
# else:
#     print('ошибок не было')
# finally:
#     print('сработает в любом случае')

# raise ValueError('пользователь дурак')

#                          моржовый оператор

# word = input()
# if word.isalpha():
#      тоже самое но короче с моржовым оператором
# if (word := input()).isalpha():






# вводится текст, вывести слова, длина которых больше 5

# text = input()
# words = text.split()
# for word in words:
#     if len(word) >5:
#         print(word)


# # Спрашивать данные у пользователя с клавиатуры до тех пор пока он не введет число


# number = input('Введите число: ')
# while not number.isdigit():
#     number = input('это не число, давай еще раз: ')
# print('молодец')

