# a list is a collection which is ordered and changeable.
# in python lists are written with square brackets [].

list1 = [10,20,30,40]
list2 = [10, "apple", 30, "mango"]

mylist3 = list()
print(list2)
print(mylist3)
print(list2[-1]) # from 1st one from end
print(list2[2]) # from begin , starts with zero index , from end starts from -1

fruits = ["apple", "mango","apple","banana", "cherry", "lemon", "kiwi", "orange"]
print(fruits[2:5])
print("**********************************************************")
for i in fruits:
    print(i)

print(len(fruits))
print(fruits.count("apple"))