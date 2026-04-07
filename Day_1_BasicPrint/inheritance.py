# single inheritance
# class A:
#     x,y=10,30
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=50,5
#     def m2(self):
#         print(self.a-self.b)
#
# bobj = B()
# bobj.m1()
# bobj.m2()

# Multiple inheritance
class A:
    x,y=10,30
    def m1(self):
        print(self.x+self.y)

class B:
    a,b=50,5
    def m2(self):
        print(self.a-self.b)

class C(A,B):
    c,d=70,10
    def m3(self):
        print(self.c-self.d)


cobj = C()
cobj.m2()


