class student:
    name='shanto'
    age=24
    def deva(self):
        print(f'my name is {self.name} and age {self.age}')
    def wlc(self):
        print('welcome')
    @staticmethod  # eita dile kono object nibe na ba self dite hobe na emni call korlei hobe 
    def help():
        print("please help")

man = student()
print(man.name)
man.deva()
man.wlc()
man.help()
# student.deva(man) eivab lakle o kaj korbe 
