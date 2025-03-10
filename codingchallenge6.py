#Jannatul Jami
#Period 1 and 2
#3/10/2025

def is_triangle(a, b, c):
    if (a+b> c) and (a + c > b) and (b + c> a):
        print("no")
    else:
        print("yes")

def what_triangle(f):
    num1 = int(input("First length: "))
    num2 = int(input("Second length: "))
    num3 = int(input("Third Length: "))
    f(num1, num2, num3)
   


what_triangle(is_triangle)
