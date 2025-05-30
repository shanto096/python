s = 'python'
print(len(s)) #length 6
print(s[0:5]) #slice pytho
print(s[0]) #first later p
print(s[-1]) #last later n 
print (s.capitalize())  #Python
print(s.upper()) #PYTHON
print(s.lower()) #python

l = 'i love you '
print('love' in l) #True
print('hate' in l) #False
print('hate' not in l) #True


p= 'programmer'
for char in p: #sob letter ak ak kore print korcha 
    print(char)

for char in p[::-1]: # utlta dik thake sob later ek ek kore print korcha 
    print(char)


k = 'i love you'
print(k.replace('you','me')) #replace kore dibe 


n= "apple,banana,mango"
print(n.split(',')) # array dibe ar sob golo koma diye separet kore dibe 

j = 'i', 'love', 'you'
print(' '.join(j))  # i love you kore dibe 

m= '          hello    '
print(m.strip())  #samne pichone gap sore dibe 

t='shanto.pdf'
print(t.startswith('sha')) # True

print(t.endswith('.pdf')) #True

f= 'i love you'
print(f.find('love')) # 2 result

print(f.find('hate')) # -1 result

print(f.count("o")) # 2 result karon 2 ta o acha 
