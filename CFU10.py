#Jannatul Jami Period 1 and 2 10/18/2024

import random
print("Let's roll the dice!")
num_rolls = int(input("How many times do we want to roll the dice?"))

def guess(num_random,total):
    
    guess = int(input("Guess the roll: "))
    if guess == num_random:
        total = total +6
    else:
        total = total -1
        
        
def rolls(num_rolls, total =0):
    num_random = random.randint(1,6)
    if num_rolls ==0:
        return total
    else:
        num_rolls = num_rolls -1
        guess(num_random,total)
        print(f"you roll a {num_random}!")
        return rolls(num_rolls,total)
    
total =rolls(num_rolls)
print(f"total is: {total}")