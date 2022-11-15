morse = {
    'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•',
    'g': '——•', 'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
    'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•',
    's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
    'y': '—•——', 'z': '——••'}


def binary_to_decimal2(binary):
    decimal = 0
    binary = binary[::-1]
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2 ** i
    return decimal
def text_to_morse(text):
    global morse
    result = ''
    text = text.lower()
    for i in text:
        if i in morse:
            result += morse[i] + ' '
        elif i == ' ':
            result += '  '
    return result



def morse_to_text(morse_text):
    global morse
    morse_text = morse_text.replace('   ', ' | ').split()
    text = ''
    for i in morse_text:
        if i == '|':
            text += ' '
        else:
            for key, val in morse.items():
                if i == val:
                    text += key
                    break
    return text


print(morse_to_text(text_to_morse(text='Hello world')))