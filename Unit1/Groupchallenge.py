#Wendy/Jannatul
#10/22/24

import random


def user_score (attempts):
    random_num = random.randint(1, 10)
    guess = int(input("Guess a number from 1-10: " ))
    attempts +=1
    if random_num == guess:
        print("Thats correct. It took " + str(attempts) + " try")
    elif random_num > guess:
        print("Too High")
        user_score(attempts)
    else:
        print("Too Low")
        user_score(attempts)

user_score(0)       
difficulty = input("How would you define the difficulty from 1-10: ")
print("You rated the difficulty as: " + difficulty)
