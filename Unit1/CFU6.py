import math
import random

num1 = random.randint(1, 100)
num2 = int(input("Input any number: "))

add = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1/num2
remainder = num1 % num2
root = math.sqrt(num1)
power = math.pow(num1, num2)

print("Results:")
print("Random Number: " + str(num1))
print("Your number: " + str(num2))
print("Sum: " + str(num1) + " + " + str(num2)+ " = " + str(add))
print("Difference: " + str(num1) + " - " + str(num2) + " = " + str(difference))
print("Product: " + str(num1) + " x " + str(num2) + " = " + str(product))
print("Quotient: " + str(num1) + " / " + str(num2) + " = " + str(quotient))
print("Remainder: " + str(num1) + " % " + str(num2)+ " = " + str(remainder))
print("Power: " + str(num1) + " ^ " + str(num2) + " = " + str(power))
