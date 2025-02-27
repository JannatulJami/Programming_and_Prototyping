#Jannatul jami
#Period 1 and 2
#2/26/2024

#function for question 1
import math # To be able to use pi
def sphere_volume(radius):
    volume = (4/3) * math.pi *(radius **3)
    return volume
volume_reset = sphere_volume(5)
print(f"The volume of a sphere of radius 5 is {volume_reset:2F}")

    
#function for question 2
def w_cost(copies):
    cover_price = 24.95
    discount = 0.40
    ship_first = 3
    ship_after = 0.75
    discount_price = cover_price* (1- discount)
    total_book_cost = discount_price * copies
    ship_cost = ship_first + (ship_after * (copies - 1))
    total = ship_cost + total_book_cost 
    print(f"Your total is ${total :2f}") # To print the final sentence with the total cost
w_cost(60) #To play the function






# Function for question 3
def running_time(start_hour, start_minutes):
    easy_pace = 8*60 +15
    temp_pace = 7*60+12
    
    
    total_time_seconds = easy_pace * 2 + (temp_pace *3)
    total_minutes = total_time_seconds // 60
    total_seconds = total_time_seconds % 60
    
    end_minutes = total_minutes + start_minutes
    end_hour = start_hour
    
    if end_minutes >= 60:
        end_hour += end_minutes // 60
        end_minutes = end_minutes % 60
    return end_hour, end_minutes
end_hour, end_minutes = running_time(6, 52)
print(f"You will arrive home for breakfast at {end_hour}:{end_minutes} AM.")
    
    
