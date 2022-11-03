# First way

name = input('enter your name: ')
age = input('enter your age: ')
city = input('enter your city: ')
greetings = 'Hello {name}, {age} age, from {city}'.format(name=name.title(), age=age, city=city.title())
print(greetings)

# Second way

name = input('enter your name: ')
age = input('enter your age: ')
city = input('enter your city: ')
greetings = f'Hello {name}, {age} age, from {city}'
print(greetings)

# Third way

name = input('enter your name: ')
age = input('enter your age: ')
city = input('enter your city: ')
print('Hello ' + name.title() + (', ') + age + (' age,') + ' from ' + city.title())
