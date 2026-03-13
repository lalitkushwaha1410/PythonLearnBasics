a=20;
b=30.5;
name = "Peter";
grade = 'A';

#Example :1
print(type(a));
print(type(b));
print(type(name)); # at runtime , datatype is assigned to variables by python
print(type(grade));

#Example :2
#single print statement for multiple variables
print(a,b);

#Example :3
c,d,e = 5,6,7;
print(c,d,e);

#example :4
x=4
y=10
print("before swap -",x,y);
x,y = y,x; # swapping values
print("after swap -",x,y);

# python is dynamically typed programming language means
# python will assign data type to variable based on assigned value.
#Python has no keyword for declaring variables like const , int , let , var str etc.
# variable is created the moment value is assigned to the variable.