#Wendy/Jannatul
#10/22/24
#Period 1 and 2

import random
import time 
num_user = int(input("How many rounds do you want to play? "))


response_time = 0 
total_attempts = 0
round_num = 1

def difficulty():
    print("\nSelect difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-1000)")
    
    difficulty = int(input("Choose 1, 2, or 3: "))
    
    if difficulty == 1:
        return 10
    elif difficulty == 2:
        return 50
    elif difficulty == 3:
        return 1000
    else:
        print("Invalid choice. Defaulting to Easy.")
        return 10

limit = difficulty()

def user_score (initial_attempt, random_num):
    random_num = random.randint(1, 10)
    start_time = time.time()
    initial_attempt +=1
    guess = int(input(f"Enter a random number between 1 and {limit}: "))
    end_time = time.time()
    response_time = end_time - start_time
    print(f"It took you {response_time:.2f} seconds to respond.")
    if random_num == guess:
        print("Thats correct. It took " + str(initial_attempt) + " try")
        return initial_attempt, response_time
    elif random_num > guess:
        print("Too High")
        return user_score(initial_attempt, random_num)
    else:
        print("Too Low")
        return user_score(initial_attempt, random_num)

def play_round(round_num, total_attempts, response_time):
    if round_num > num_user:
        average_attempts = total_attempts / num_user
        average_response_time = response_time / total_attempts
        print(f"\nGame over! You played {num_user} rounds.")
        print(f"Total attempts:  {total_attempts}")
        print(f"Average attempts per round: + {average_attempts:.2f}")
        print(f"Average response time: {average_response_time:.2f} seconds per attempt")
    else:
        print(f"\nRound {round_num}")
        
        random_num = random.randint(1, 10)
        attempts, response_time = user_score(0, random_num)

        total_attempts += attempts
        response_time += response_time

        play_round(round_num + 1, total_attempts, response_time)

play_round(round_num, total_attempts, response_time)
#user_score(0)       
difficulty = input("How would you define the difficulty from 1-10: ")
print("You rated the difficulty as: " + difficulty)
