# Parent/Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is making a sound.")

# Child/Derived Class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

# Object তৈরি
d = Dog("Tommy")
d.speak()   # Animal class থেকে পাওয়া
d.bark()    # Dog class এর নিজস্ব
