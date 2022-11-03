# first way

text = input('enter any sentence: ')
new_sentence = '-'.join(text.split(' '))
print(new_sentence)

# second way

text2 = input('enter any sentence: ')
new_sentence = text2.replace(' ', '-')
print(new_sentence)



