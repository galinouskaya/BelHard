numbers = [2, 3, 4, 5, 6, 98, 45, 234, 45, 7]
#
#
# def my_sort(numbers):
#     result = []
#     for number in range(len(numbers)):
#         if numbers[i]%2:
#             result.append(numbers[i])
#         else:
#             result.insert(0,numbers[i])
#     return result



for i in range(len(numbers)):
    if numbers[i]%2 == 0:
        numbers.insert(0, numbers.pop(i))
return numbers


# numbers = list(filter(lambda x: not x % 2, numbers)) + list(filter(lambda x: x % 2, numbers))
#     return numbers
#
#
# print(my_reversed(numbers))
# print(my_sort(numbers))

