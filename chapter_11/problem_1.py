class twoWord:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print(f'word two {self.a}a and {self.b}b')

class threeWord(twoWord):
     def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
     def show(self):
        print(f'word two {self.a}a and {self.b}b and {self.c}c')

a1=twoWord(1,2)
a1.show()
a2=threeWord(3,4,5)
a2.show()