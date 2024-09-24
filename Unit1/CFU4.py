#Jannatul Jami 9/24/25 Period 1 and 2

import math
name = input("What is your name: ") 
a = float(input("What do you want coefficent a to be?: "))
b = float(input("What do you want coefficent b to be?: "))
c = float(input("What do you want coefficent c to be?: "))

solution1 =  (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
solution2 =  (-b - math.sqrt(b**2 - 4*a*c) ) / (2*a)

print("The roots are x = " + str(solution1) + " and x = " + str(solution2))
