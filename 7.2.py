def witcher():
    orens = int(input('enter sum: '))
    coins = [25, 10, 5, 1]
    res = 0
    for coin in coins:
        res = res + orens//coin
        orens = orens % coin
    print('You need ' + str(res) + ' coins')


witcher()