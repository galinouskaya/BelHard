
list = [163, 156, 184, 159, 193, 159, 158, 158, 158]
height = 192

if height not in list:
    list.append(height)
    list.sort(reverse=True)
    print(list.index(height) + 1)
    print(list)

else:
    list.sort(reverse=True)
    repeat = list.count(height)
    new_index = list.index(height)
    list.insert((repeat + new_index), height)
    print(list.index(height) + (repeat+1))
    print(list)
