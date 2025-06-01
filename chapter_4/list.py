#  1. ✅ List তৈরি করা

empty=[]
numbers=[1, 2, 3, 4, 5,]
mixed = ['shanto', 1, 3.5, True]
nested= [1, [1,2], 4, [5, 6]]

#  2. ✅ Indexing & Slicing
 
number = [1,2,3,4,5,6] 

print(number[1:3])
print(number[0])
print(number[-1])
print(number[-4])


#  3. ✅ List পরিবর্তনযোগ্য (Mutable)...........................   

number2= [100, 200, 300, 400]
number2[1]=500
print(number2)

#   4 সব List Methods একসাথে

num = [1,2,3 ,5]
num.append(5)   # add korbe 
num.pop()   #paramitare value na dile last thake ar value dile value onojaiye detete hobe 
num.insert(1,5) # index onojaiye value add kora jabe 

num.extend([6, 7])
num.remove(2)
num.sort()
num.reverse()
count_5 = num.count(5)
print(count_5)
index_3 = num.index(3)
print(index_3)
copy_num = num.copy()
print(copy_num)
# num.clear()
print(num)