class father:
    def love1(self):
        print('father love')
class mother:
    def love2(self):
        print('mother love')
class child(father, mother):
    def love3(self):
        print('all love father and mother')
a1 = child()
a1.love1()
a1.love2()
a1.love3()