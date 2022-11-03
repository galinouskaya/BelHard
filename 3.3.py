# First way

name = input('enter your name ')
age = input('enter your age ')
city = input('enter your city ')
greetings = 'Hello {name}, {age} age, from {city}'.format(name=name.title(), age=age, city=city.title())
print(greetings)



