class student:
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year
    def show(self):
        print(f'my name is {self.name} , age {self.age} and {self.year}')

s1 = student('shanto', 25, 2025)
s1.show()