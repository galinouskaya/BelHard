users = {
    1: {
        'name': 'alex',
        'email': 'alex@gmail.com'
    },
    2: {
        'name': 'pavel',
        'email': ''
    },
    3: {
        'name': 'masha'
    }
}

for user in users.values():
    # var 1
    # if 'email' not in user:
    #     print(user['name'])
    # elif user['email'] == '':
    #     print(user['name'])

    # var2
    if not user.get('email'):
        print(user.get('name'))