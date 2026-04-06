# diff bet function and method
# group of statements which performs certain task , avoid code duplication , reusability
# functions created inside Class , they are called as Methods
# Def keyword is used to create a function in python.
# 1. No argument 2. parameterized function

def myfun():
    print("hello")

myfun() # function call

def namefun(name):
    print("Hello", name)  # name is parameter

namefun("Peter")  # peter is argument

#example :
def add(a,b):
    return a+b

sum = add(5,10)
print("@@@@@@@@@@@@@@@@@@@@@@",sum)

#example : arbitrary arguments : n number of arguments
def sum_function(*num):
    total =0
    for i in num:
        total =total +i
    return total

print(sum_function(10,20,30))
print(sum_function(50,60))
print(sum_function(4,6,7,8,9,2))

# Keyword and positional arguments
def myfun(a,b,c):
    print(a,b,c)

myfun(10,20,30) # positinal arguements

myfun(c=30,a=50,b=80)
myfun(20,70,c=40) # position argument must come before keyword argument
