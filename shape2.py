




"""  print("test")

#def defines a function
#inside the parenthesis are the inputs aka argument

def add(x,y):
    #print(x + y)
    #return creates an output for the function
    print(x + y)
    return(x + Y)
    add(5,6)
 """

""" x = 3
y = float(3)
print(x,y)

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6])


x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)

day_of_week = input("what day is it? ")
if day_of_week == "Friday":

    print("correct")
else:
    print("incorrect")
 """

""" import turtle
from turtle import *
t = Turtle()

x = "test"
print(f"hello {x}")


temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """


def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

check_odd_even = input("number")
if  check_odd_even == "Even":
    print("Even")
else:
    print("odd")