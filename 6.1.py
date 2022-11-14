def binary(a, c=''):
    while a > 0:
        c = str(a % 2) + c
        a = a // 2
    return c


res = binary(34)
print(res)
