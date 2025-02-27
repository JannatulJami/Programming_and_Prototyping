#Jannatul jami
#Period 1 and 2
#2/26/2024

#function for question 1
import math # To be able to use pi
def sphere_volume(radius): #writing the beginning of the function
    volume = (4/3) * math.pi *(radius **3) #Forula of the volume of a sphere
    return volume #Return the volume of the sphere
volume_reset = sphere_volume(5)#Making the radius equal to 5 and trying to run it
print(f"The volume of a sphere of radius 5 is {volume_reset:.2F}") #Writing the volume output for a radius of 5

    
#function for question 2
def w_cost(copies): #For users to put whatever number of copies they want
    cover_price = 24.95 #The cover price for one book
    discount = 0.40 #The discount amount
    ship_first = 3 #The shipping value cost of the first copy
    ship_after = 0.75 ##The shipping cost value of everyother copy after the forst one
    discount_price = cover_price* (1- discount) #Finding the cost after the dscount price was added
    total_book_cost = discount_price * copies #finding the cost of all the copies
    ship_cost = ship_first + (ship_after * (copies - 1)) #finding the total shipping cost
    total = ship_cost + total_book_cost #Findging the total of the shipping cost and the discounted book cost
    print(f"Your total is ${total :.2f}") # To print the final sentence with the total cost
w_cost(60) #To play the function






# Function for question 3
def running_time(start_hour, start_minutes): #Writing teh start of teh function
    easy_pace = 8*60 +15 #How long it takes in seconds to run one mile in easy pace
    temp_pace = 7*60+12 #How long it takes in seconds to run one mile in tempo pace
    
    
    total_time_seconds = easy_pace * 2 + (temp_pace *3) #Total time in seconds to run 2 miles in easy pace and 3 miles in tempo pace
    total_minutes = total_time_seconds // 60 #The number of minutes of the total running time
    total_seconds = total_time_seconds % 60 #The number of seconds remaining after calculating the seconds
    
    end_minutes = total_minutes + start_minutes #Finding the number of minutes that passed after 6:52 am
    end_hour = start_hour #To make the new hour
    
    if end_minutes >= 60: #A ocnditional to make the minutes not go over 60 and move on to the next hour
        end_hour += end_minutes // 60 #To add a another hour after 60 minutes
        end_minutes = end_minutes % 60 #To find the amount of minutes
    return end_hour, end_minutes #retruning both final values of the new hour and minutes
end_hour, end_minutes = running_time(6, 52) #To un the function
print(f"You will arrive home for breakfast at {end_hour}:{end_minutes} AM.") #To print the snetence
    
    
    
    
