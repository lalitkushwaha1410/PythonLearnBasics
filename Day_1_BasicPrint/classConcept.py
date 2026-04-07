#ex-1 : creating a class with Object

# class MyClass:
#     def myfun(self, ):
#         pass
#
#     def display(self, name):
#         print(name)
#
# mc1 = MyClass()
# mc1.display("Peter")
#
# mc2 = MyClass()
# mc2.display("Robin")

# Ex-2 : instance and static method
# class myClass:
#     def m1(self):
#         print("instance method")
#
#     @staticmethod
#     def m2(self,num):
#         print("static method :",self, num)
#
#
# mc = myClass()
#
# #print(mc.m2(10,30))
# print(myClass.m2(40,50))


# Ex-3 : Define variables inside the Class
#  myClass:
#     a,b =20,40
#
#     def add(self):
#         print(self.a + self.b)
#
#     def multiply(self):
#         print(self.a * self.b)
#
# mc = myClass()
# mc.add()
# mc.multiply()


# Ex-4 : local variables , Global variables & Class variables
# i,j =45,67
#
# class myClass:
#      a,b=20,30 # Class variables
#
#      def add(self,x,y):
#         print(x+y)
#         print(self.a + self.b)
#         print(i+j)
#
# mc = myClass()
# mc.add(100,400)

# Ex-5 : when global and class varibales have same name

# a,b = 2,14
#
# class myClass:
#     a,b =50,70
#
#     def add(self, a,b):
#         print(a+b)
#         print(globals()['a'] + globals()['b'])
#
# mc = myClass()
# mc.add(400,600)

#Ex-7 : class with constructor : used for initialize the data
# __init__(self)
# invoked automatically when object is created

# class Myclass:
#     def __init__(self):
#         print("constructor called")
#     def m1(self):
#         print("hello....")
#     def m2(self,x,y):
#         return x+y
#
# mc1 = Myclass()
# mc2 = Myclass() # when object created, constructor is called

# Ex-7 : contrcutor with parameters and class varibales
# class myClass:
#     name ="peter"
#
#     def __init__(self, name):
#         print(name)
#         print(self.name)
#
# mc = myClass("David ")

# Ex-8 : class with constructor and methods

class emp:
    def __init__(self, eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal
        print(self.eid, self.ename, self.esal)
    def display(self):
        print(self.eid,self.ename,self.esal)

e1= emp(101, "john", 30000)
#e1.display()