
# 1 Dictionary কী?


 
d= {} # empty dict


person = {
    "name": "Ratul",
    "age": 21,
    "city": "Rajshahi"
}

print(person['name'])
print(person.values())
print(person.keys())

person["name"]='shanto'
print(person)

print(person.items())


# 2 Nested Dictionary

students = {
    "101": {"name": "Asha", "grade": "A"},
    "102": {"name": "Ratul", "grade": "B"},
}
print(students['102']['grade'])

#  3. Dictionary এর value গুলো যোগ করো (Sum)
marks = {"Math": 80, "English": 70, "Science": 90}

print(sum(marks.values()))

marks.update({"Math": 85, "English": 75, "math":50})
print(marks)


# Create a sample dictionary all method
d = {"name": "Ratul", "age": 21, "country": "Bangladesh"}

print(d.get("name"))           # Ratul
print(d.get("email", "N/A"))   # N/A

print(d.keys())                # dict_keys(['name', 'age', 'country'])
print(d.values())              # dict_values(['Ratul', 21, 'Bangladesh'])

d["gender"] = "Male"
d.update({"age": 22, "email": "ratul@gmail.com"})
print(d)

print(d.pop("country"))        # Bangladesh
print(d.popitem())             # Removes last item
print(d.setdefault("job", "None"))  # None if 'job' not exis