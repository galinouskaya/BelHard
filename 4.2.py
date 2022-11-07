a = input('enter some words: ')
my_dict = {a[i]: a.count(a[i]) for i in range(0, len(a))}
print(my_dict)
