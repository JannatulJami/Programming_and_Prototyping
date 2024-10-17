#Janatul Jami
# Period 1 and 2
#10/17/202
import random
rolls = int(input("How many rolls do you want?"))

if rolls == 1:
    x = int(input("Guess a number: "))
    print(random.randint(1, 6))
elif rolls == 2: 
    x = int(input("Guess a number: "))
    y = int(input("Guess a number: "))
    print(random.randint(1, 6))
    print(random.randint(1,6))
elif rolls == 3:
    x = int(input("Guess a number: "))
    print(random.randint(1, 6))
    y = int(input("Guess a number: "))
    print(random.randint(1,6))
