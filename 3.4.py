number1 = int(input('enter number 1: '))
number2 = int(input('enter number 2: '))
number3 = int(input('enter number 3: '))
positive = (number3 > 0) + (number2 > 0) + (number1 > 0)
negative = (number3 < 0) + (number2 < 0) + (number1 < 0)
print('positive numbers: ', positive)
print('negative numbers: ', negative)