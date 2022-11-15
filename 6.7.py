def sum_neighbor(numbers):
    result = []
    for i in range(len(numbers)):
        if i < len(numbers) - 1:
            result.append(numbers[i-1] + numbers[i+1])
        else:
            result.append(numbers[i-1] + numbers[0])
    return result


numbers = [1, 2, 3, 4, 5, 6, 7]
print(sum_neighbor(numbers))