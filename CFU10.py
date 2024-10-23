#Jannatul jami Period 1 and 2 
import random
guesses = 0
user_guess = int(input("Guess a number bewteen 1-6: "))
number_rolls = int(input("How many rolls do you want to play: "))

def game():
number = random.randint(1,6)
print(number)
attempts += 1 
    if user_guess == number:
        print("That's correct")
    elif user_guess > number:
        print("Too High")
    else:
        print("Too Low")
   
