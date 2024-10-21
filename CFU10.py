#Jannatul jami Period 1 and 2 
import random
guesses = 0
number = random.randint(1,10)
user_guess = int(input("Guess a number bewteen 1-10: "))

print(number)
if user_guess == number:
    print(guesses)
elif user_guess > number:
    print("Too High")
else:
    print("Too Low")
   
