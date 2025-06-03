# শিক্ষার্থীর নাম ও নম্বর ইনপুট নেওয়া হচ্ছে
name = input("Enter your name: ")
roll = input("Enter your roll number: ")
marks = int(input("Enter your marks (0 - 100): "))

print("\n------ Result Sheet ------")

# ইনপুট চেক
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter between 0 and 100.")

# ফেল
elif marks < 33:
    print(f"Name: {name}")
    print(f"Roll: {roll}")
    print("Marks:", marks)
    print("Result: Fail ❌")

# D Grade: 33 - 40
elif marks <= 40:
    print(f"Name: {name}")
    print(f"Roll: {roll}")
    print("Marks:", marks)
    print("Grade: D ✅")

# C Grade: 41 - 50
elif marks <= 50:
    print(f"Name: {name}")
    print(f"Roll: {roll}")
    print("Marks:", marks)
    print("Grade: C ✅")

# B Grade: 51 - 60
elif marks <= 60:
    print(f"Name: {name}")
    print(f"Roll: {roll}")
    print("Marks:", marks)
    print("Grade: B ✅")

# A Grade: 61 - 70
elif marks <= 70:
    print(f"Name: {name}")
    print(f"Roll: {roll}")
    print("Marks:", marks)
    print("Grade: A ✅")

# A+ Grade: 71 - 80
elif marks <= 80:
    print(f"Name: {name}")
    print(f"Roll: {roll}")
    print("Marks:", marks)
    print("Grade: A+ ✅")

# Golden A+: 81 - 100
elif marks <= 100:
    print(f"Name: {name}")
    print(f"Roll: {roll}")
    print("Marks:", marks)
    print("Grade: Golden A+ 🌟")







# if + and উদাহরণ:
age = 20
isActive= True

if(age >= 20 and isActive ):
    print('2 tai sotti ')

else:
    print('mittha ')



# if + or উদাহরণ:
isAdmin= True
isUser= False
if(isAdmin or isUser):
    print('2tar modha ekta sotti')
else:
    print('kono tai hobe na ')


#  if + not উদাহরণ:
isStudent = False
if(not isStudent):
    print(' ulta  kore dibe')
else:
    print('ulta kore na dile  tile hobe na ')