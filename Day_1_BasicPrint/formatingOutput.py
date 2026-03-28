name, age, sal = "john", 25, 50000.00

#approach-1
print(name, age, sal);

#approach-2
print("Name :" + name);  #+ used for string concatenation
print("Name :", name);  # , is also used for concate
print("Age :", age);  # , is used to concate number values

#approach-3
# %s--string , %d--->int   %g---> decimal
print("Name:%s  Age:%d  Salary:%g" % (name, age, sal));

#approach-4

print("Name:{} Age:{} Salary:{}".format(name, age, sal))

#approach-5
print("Name:{0} Age:{1} Salary:{2}".format(name, age, sal))
print("Salary:{2} Age:{1} Name:{0} ".format(name, age, sal))

#approach-6 : print data in multiple lines

print(" Welcome to \npython world")
print(" Welcome to \tpython world")
