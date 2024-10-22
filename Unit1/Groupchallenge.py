#Wendy/Jannatul
#10/22/24
#Period 1 and 2

import random
import time 

round_num = 1
response_time = 0 
total_attempts = 0

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

def play_round(round_num, total_attempts, response_time):
    if round_num > num_user:
        average_attempts = total_attempts / num_user
        average_response_time = response_time / total_attempts
        print(f"\nGame over! You played {num_user} rounds.")
        print(f"Total attempts: {total_attempts}")
        print(f"Average attempts per round: {average_attempts:.2f}")
        print(f"Average response time: {average_response_time:.2f} seconds per attempt")
    else:
        print(f"\nRound {round_num}")
        
        ran_num = random.randint(1, limit)
       
        attempts, response_time = guess_number(0, ran_num)

        total_attempts += attempts
        response_time += response_time

        play_round(round_num + 1, total_attempts, response_time)

play_round(round_num, total_attempts, response_time)
user_score(0)       
difficulty = input("How would you define the difficulty from 1-10: ")
print("You rated the difficulty as: " + difficulty)
