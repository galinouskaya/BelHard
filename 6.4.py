lst = [2, 3, 4, 'klnvlk', True, [], None, 'sfsmklf', 'sjfslj']
lst = list(filter(lambda x: isinstance(x,str), lst))
print(lst)


lst = [2, 3, 4, 'klnvlk', True, [], None, 'sfsmklf', 'sjfslj']
i = 0
while i < len(lst):
    if not isinstance(lst[i], str):
        del lst[i]
    else:
        i += 1
    print(lst)

