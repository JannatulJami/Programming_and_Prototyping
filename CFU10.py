#Jannatul jami Period 1 and 2 
import random
score = 0
number_rolls = int(input("How many rolls do you want to play: "))

def game():
number = random.randint(1,6)
user_guess = int(input("Guess a number bewteen 1-6: "))
print(number)
attempts += 1 
    if user_guess == number:
        print("That's correct you earn +1 point")
        score += 1
    else:
        print("Incorrect! That's one less point
              score += 1
game()

