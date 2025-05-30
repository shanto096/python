#  1. Arithmetic Operations (সংখ্যার অপারেশন)
a = 10
b = 3

print("➕ যোগ:", a + b)          # 13
print("➖ বিয়োগ:", a - b)        # 7
print("✖️ গুণ:", a * b)          # 30
print("➗ ভাগ:", a / b)          # 3.333...
print("// Floor Division:", a // b)  # 3
print("% ভাগশেষ (Modulus):", a % b) # 1
print("** ঘাত (Power):", a ** b)     # 1000



# 2. Comparison Operators (তুলনা অপারেশন)
x = 5
y = 7

print("== সমান?", x == y)     # False
print("!= অসমান?", x != y)    # True
print("> বড়?", x > y)         # False
print("< ছোট?", x < y)        # True
print(">= বড় বা সমান?", x >= y) # False
print("<= ছোট বা সমান?", x <= y) # True





#  3. Logical Operators (যুক্তি অপারেশন)

a = True
b = False

print("and (এবং):", a and b)  # False
print("or (অথবা):", a or b)   # True
print("not (নয়):", not a)     # False


# 4. Assignment Operators (অ্যাসাইনমেন্ট)
x = 5
x += 3   # x = x + 3
print("x += 3 =", x)

x -= 2   # x = x - 2
print("x -= 2 =", x)

x *= 2   # x = x * 2
print("x *= 2 =", x)

x /= 2   # x = x / 2
print("x /= 2 =", x)

x %= 3   # x = x % 3
print("x %= 3 =", x)

x = 4
x **= 2  # x = x ** 2
print("x **= 2 =", x)



# 5. Membership Operators (সদস্যতা চেক)
text = "hello"

print("'h' in text:", 'h' in text)       # True
print("'z' not in text:", 'z' not in text) # True

#  7. Identity Operators (অবজেক্ট একই কিনা)

# এটা দুই ভ্যারিয়েবলের রেফারেন্স (অর্থাৎ, তারা একই মেমোরি ঠিকানা শেয়ার করছে কিনা) চেক করে।

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y:", x is y)         # True (same object)
print("x is z:", x is z)         # False (same value, different object)
print("x == z:", x == z)        # True (same content)



#  8. Built-in Functions (আরো কিছু দরকারি অপারেশন)

a = "Bangladesh"
b = 123

print("len():", len(a))       # 10
print("type():", type(a))      # <class 'str'>
print("int to str:", str(b))   # '123'
print("input():", input("তোমার নাম কী? "))  # ইউজার থেকে ইনপুট নেয়