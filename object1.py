class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())


students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 87, 98, 88, 95),
    Student("구지연", 87, 98, 88, 95),
    Student("나선주", 87, 98, 88, 95),
    Student("윤아린", 87, 98, 88, 95),
]

for students in students:
    print(students.to_string())


# isinstance()

class Student:
    def study(self):
        print("공부를 합니다.")


class Teacher():
    def teach(self):
        print("학생을 가르칩니다.")


classroom = [Student(), Teacher(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

n = 1260
count = 0
coin_type = [500, 100, 50, 10]

for coin in coin_type:
    div = n // coin
    print(div)
    count += div
    n %= coin

print(count)
