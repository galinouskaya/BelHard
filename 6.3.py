def list_ofset(lst, n):
    lst = lst[-n:] + lst[:n]
    return lst

print(list_ofset([1, 2, 3, 4, 5, 6, 7], -3))



def list_ofset(lst, n):
    n-=len(lst) * (n // len(lst))
    lst = lst[-n:] + lst[:n]
    return lst

print(list_ofset([1, 2, 3, 4, 5, 6, 7], -3))