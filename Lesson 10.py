# from pydantic import BaseModel, EmailStr
#
# class User(BaseModel):
#     name: str
#     age: int
#     email: EmailStr
#
# data = {




# file = open('test.txt', 'r', encoding='utf-8')
# text = file.read()
# print(text)
# file.close()



# file = open('test.txt', 'r', encoding='utf-8')
# text = file.readline()
# print(text)
# text = file.readline()
# print(text)
# text = file.readline()
# print(text)
# text = file.readline()
# print(text)
# file.close()


# file = open('test.txt', 'r', encoding='utf-8')
# lines = file.readlines()
# print(lines[3])
# file.close()

#
# file = open('test.txt', 'r', encoding='utf-8')
# lines = [line.strip() for line in file if line.strip()]
# print(lines)
# file.close()

# file = open('numbers.txt', 'r', encoding='utf - 8')
# numbers = [int(line.strip())for line in file if line.strip().isdigit()]
# print(numbers)
# file.close()
#
# numbers = [1, 2, 3, 4, 5]
# text = '\n'.join(list(map(str, numbers)))
# file = open('numbers.txt', 'a', encoding='utf - 8')
# file.write(text + '\n')
# file.close()

# with open('test.txt', 'r', encoding='utf- 8') as file:
#     lines = [line.strip() for line in file if line.strip()]
#     print(lines)
# #     file
# from pydantic import BaseModel, EmailStr, Field
#
# class Address(BaseModel):
#     city: str
#     street: str
#     building: int
#
# class User (BaseModel):
#     name: str
#     age: int = Field(ge=18, le=60)
#     email: EmailStr
#     address: Address
#
# data = {
#     "name": "pavel",
#     "age": '38',
#     "email": "pavel@gmail.com",
#     "address": {
#         "city": "Minsk",
#         "street": "Heroev",
#         "building": 5}
# }
#
# pavel = User(**data)
# print(pavel.name)
# print(pavel.email)
# print(pavel.address.city)
# # print(pavel.street)


from csv import DictReader

with open('users excel.csv', 'r', encoding='utf-8 sig') as file:
    reader = DictReader(file, delimiter=';')
    for user in reader:
        print(user)
#
# from csv import DictWriter
#
# users = [{
#     "name": "pavel",
#     "age": '38',
#     "email": "pavel@gmail.com"
#        },
#        {
#     "name": "stepan",
#     "age": '24',
#     "email": "stepan@gmail.com"}]
#
# with open('users.csv', 'w', encoding='utf-8') as file:
#     fieldnames = ['name', 'age', 'email']
#     writer = DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(users)
