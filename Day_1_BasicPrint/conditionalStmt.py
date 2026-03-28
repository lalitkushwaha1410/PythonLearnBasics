#example-1
from traceback import print_tb

age=20

if age>=18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

if age>=18:print("Eligible to Vote")
# if elif else
marks =60
print("Marks obtained :", marks)

if marks>90:
    print("Grade A")
elif marks>70:
    print("Grade B")
elif marks>50:
    print("Grade C")
else:
    print("Fail");

# nested elif

#short hand if else
a,b = 20,50
print("a is greater") if a>b else print("b is greater")  #ternary operator

# match Case statement (similar to switch case)
day =3;
match day:
    case 1:print("Sunday")
    case 2:print("Monday")
    case 3:print("Tuesday")
    case 4:print("Wednesday")
    case _:print("Not Valid Day number")

num =20
match num:
    case 2|3|4|5|6:print("Weekday")
    case 1|7:print("Weekends")
    case _:print("Not valid day number")

