#Jannatul Jami Period 1 and 2

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

def sum():
    add = num1 + num2 + num3
    print("The sum of your three numbers are: " + str(add))

def average():
   avg = (num1 + num2 + num3) / 3
   print("The sum of your three numbers are: " + str(avg))
    
sum()
average()
