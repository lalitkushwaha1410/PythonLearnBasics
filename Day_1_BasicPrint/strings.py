# 3 ways to create string
# double quotes
from traceback import print_tb

name = "Peter"

#single quotes
lastName = 'melvin'

# using constructor
address = str() #empty string
grade = str("first") # 'first' , single or double characters

print(grade)

# + and * operator with string
str = "welcome"
print(str + " programming")

print(str * 3) # prints str 3 times

#slicing strings
print(str[1:4])
print(str[:5])
print(str[3:])

print(str[1:-1])
print(str[2:-2])
#welcome
print(str[-5:4])
print(str[-5:-2])

# f string
num =23 ;
name = "Arun"
str = f"My name is {name} and my age is {num}"
print(str);

price = 55
total = f"Total price is {price:.3f}"
print(total);
