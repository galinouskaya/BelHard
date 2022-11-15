def my_reversed(lst):
    for i in range(len(lst) // 2):
        j = len(lst) - 1 - i  # индекс элемента с противоположной стороны
        lst[i], lst[j] = lst[j], lst[i]
        # lst[i], lst[~i] = lst[~i], lst[i]
    return lst


print(my_reversed(numbers))