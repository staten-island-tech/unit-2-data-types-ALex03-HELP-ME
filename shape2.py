




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



""" #odd and even

def check_odd_even():
    number = int (input("number"))
    if number % 2 == 0:
        print("Even")
    else:
        print("odd")
check_odd_even()
 """

""" def calculate_tip(bill, service_quality):
    # Define the tip percentages for each service quality
    if service_quality == "bad":
        tip_percentage = 0  # No tip for bad service
    elif service_quality == "okay":
        tip_percentage = 0.15  # 15% tip for okay service
    elif service_quality == "good":
        tip_percentage = 0.20  # 20% tip for good service
    elif service_quality == "great":
        tip_percentage = 0.25  # 25% tip for great service
    else:
        return "Invalid service quality"

    tip = bill * tip_percentage
    return f"Tip for {service} service: ${tip:.2f}"
bill = float(input("enter the bill amount: $"))
service = input("enter the service rating (bad, ok, good, great): ").strip()
tip = calculate_tip(bill, service)
print(tip) """