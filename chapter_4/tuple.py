# 1 ✅ Tuple তৈরি করার নিয়ম
t1 = ()                      # খালি টাপল
t2 = (1, 2, 3)               # সংখ্যার টাপল
t3 = ("a", "b", "c")         # স্ট্রিং টাপল
t4 = (1, "hi", 3.5, True)    # মিশ্র ডাটা
t5 = (1,)                    # এক আইটেমের tuple (comma must)

# 2. ✅ Indexing & Slicing
t = (10, 20, 30, 40, 50)
print(t[0])
print(t[-4])
print(t[0:3])





# 3 ✅ Tuple এর উপর কাজ করার মেথড


tM = (10, 20, 30, 40, 50)
print(tM.count(2))
print(tM.index(40))



# 4 ✅ Tuple immutable কেন?

# ti = (1, 2, 3)
# ti[0] = 10     # Error: 'tuple' object does not support item assignment


# 5. ✅ Tuple Concatenation & Repetition

c= (1,2,3)
c2=(4,5,6)
print(c+c2)
print(c*3)



# 6 ✅ Tuple কে List-এ এবং List কে Tuple-এ রূপান্তর

tr=[1,2,3]
print(tuple(tr))

lr=(1,2,3)
print(list(lr))



students = (
    ("Asha", 23),
    ("Ratul", 21),
    ("Nila", 24),
)

for name, age in students:
    print(f"{name} is {age} years old.")