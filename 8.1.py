class Student:

    def __init__(self, first_name: str, group: int, marks: list[int]):
        self.name = first_name
        self.group = group
        self.marks = marks

    def __str__(self):
        return f'Name: {self.name}, Group: {self.group}, Marks: {self.marks}'

student1 = Student('vasia', 34, [4, 5, 2])
print(student1)
