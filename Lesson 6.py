def multiply(a, b=6, c=None):
#     if not c:
#         print(a * b)
#     else:
#         print((a * b)**c)
#
#
# multiply(2, 7, 8)


# def bar(a, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(a)
#     print(lst)


# bar(4)
# bar(4)


# def baz(a, b, c, d=6, *args):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(args)


# def foo(**kwargs):
#     print(kwargs)
#
#
# foo(a=5, b=6, c=4)


# def multiply(a, b):
#     return a * b


# написать функцию is_palindrome принимающую строку,
# и возвращающая True если строка палиндром
# False если строка не палиндром, без учета регистра
# def is_palindrome(text):
#     return text.lower() == text.lower()[::-1]
#
#
# text = 'Алла'
# print(is_palindrome(text))

# def multiply(a):
#     def wrapper(b):
#         def inside_wrapper(c):
#             return a * b * c
#         return inside_wrapper
#     return wrapper


# def foo():
#     print('foo')
#
#
# def bar():
#     print('bar')
#
#
# def baz():
#     print('baz')
#
#
# def error():
#     print('error')
#
#
# a = int(input())
#
# data = {
#     1: foo,
#     2: bar,
#     3: baz,
# }
#
# data.get(a, error)()


# multiply = lambda a, b: a * b
#
#
# print(multiply(2, 5))


# numbers = ['1', '2', '3', '4', '5']
#
# numbers = list(map(lambda x: int(x)*2, numbers))
#
#
# def foo(x):
#     return int(x)*2
#
#
# numbers = list(map(foo, numbers))
# print(numbers)
# print(numbers)


# numbers = [1, 2, 3, 4, 5, 6]
# numbers = list(filter(lambda x: x % 2 == 0, numbers))
# numbers = [i for i in numbers if i % 2 == 0]
# print(numbers)

# from itertools import zip_longest
# text = 'hello'
# numbers = [1, 2, 3, 4, 5, 6, 7]
# tup = (True, False, True)
#
# res = list(zip_longest(text, numbers, tup))
# print(res)

# numbers = [i for i in range(2, 45, 2)]
# _i = iter(numbers)
# res = list(zip_longest(*([_i]*5)))
# print(res)

# a = 5
#
#
# def foo():
#     a = 4
#     def bar():
#         nonlocal a
#         print(a)
#
# text = 'foo'
# globals().get(text)()


# def foo():
#     for i in range(10):
#         yield i
#
#
# a = foo()
# for i in a:
#     print(i)
#
# numbers = [1, 2, 3, 4, 5, [4, 5, 6, [5, 6, 7, [6, 7, 8], [7, 8, 89], 8, 7, 5, [8, 6, 5]]]]
#
#
# def recursive_multiply(numbers):
#     res = 1
#     for i in numbers:
#         if isinstance(i, int):
#             res *= i
#         elif isinstance(i, list):
#             res *= recursive_multiply(i)
#     return res
#
#
# print(recursive_multiply(numbers))

# def is_numeric(func):
#     def wrapper(a, b):
#         if not isinstance(a, (int, float)):
#             raise TypeError('это не число')
#         if not isinstance(b, (int, float)):
#             raise TypeError('это не число')
#         a += 1
#         b += 2
#         res = func(a, b)
#         res = f'result = {res}'
#         return res
#     return wrapper
#
#
# def multiply(a, b):
#     return a * b
#
#
# multiply_decorated = is_numeric(multiply)
#
# print(multiply(2, 5))
# print(multiply_decorated(2, 5))

# @is_numeric
# def foo(a, b):
#     return a + b


# print(foo(2, 5))
# print(multiply(3, 6))


# def my_decorator(a, b):
#     def decorator(func):
#         def wrapper(c, d):
#             c += a
#             d += b
#             return func(c, d)
#         return wrapper
#     return decorator
#
#
# @my_decorator(2, 3)
# def multiply(c, d):
#     return c * d
#
#
# print(multiply(2, 5))