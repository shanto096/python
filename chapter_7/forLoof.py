# 1. for loop দিয়ে সংখ্যা (range)

for i in range(10):
    print(i)

# 2. শুরু, শেষ, এবং ধাপ (start, stop, step)

for i in range(1, 11, 2):  # 1 থেকে 10 পর্যন্ত, 2 করে বাড়বে
    print(i)

# 3. উল্টো দিকে লুপ (descending)
for i in range(10, 0, -1):
    print(i)

 # 4. for loop with else
for i in range(3):
    print(i)
else:
    print("Loop finished.")
# 5. Break & Continue এর ব্যবহার
for i in range(1,6):
    if i==3:
        break
    print(f"break {i}")



    
for i in range(1,6):
    if i==3:
        continue
    print(f"continue {i}")


name='shanto'

for i in range(len(name)):
    print(name[i] )


l = ['shanto', "panto", 12, 18]
print(type(l))
for i in l:
    print(i)

t = ('nam', "noman", 12, 18)
print(type(t))
for i in t:
    print(i)

d= {'name':'shanto','time': 12, 'age':18}
print(type(d))
for k, v in d.items():
    print(k, v)

s= {1,2,3,4,4}
print(type(s))
for i in s:
    print(i)