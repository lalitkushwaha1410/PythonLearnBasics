from traceback import print_tb

str = "Welcome to Python"

print(str.upper())

print(str.lower())

print(str.title())

print(str.swapcase())

print(str.capitalize())

#center output
s= "banana"
print(s.center(10))


#format specified value in string
name = "peter"
print("Hello {}".format(name))

# find() , index() - searched the string for specified value and returns the position
str = "hello"
print(str.find("e")) # 1 position of the string in str
print(str.find("x")) # -1 if not found

print(str.index("e")) # 1 position
#print(str.index("x")) # valueError

name = "banana"
print(name.count("a")) # count() returns the number of times a specifiec value is repeated

#replace() - returns a string a specified value is replaced with a specified value
s = "hello world"
print(s.replace("world" , "there"));

#isalnum () - returns true if all characters in the string are alphanumeric
s = "ACBD123"
print(s.isalnum());

#isalpha - returns if all characters are alphabet
s = "lalit123";
print(s.isalpha());








