#Jannnatul Jami
#Period 1 and 2 
#12/12/2024


import simplegui
import random
#Variables

snow_y = []
width = 600
height = 400
snow_flakes = 5
snowfall_speed= 1
x1 = -20
x2 = -20

# the for loop that creates the 
for i in range(snow_flakes):
    snow_y.append(random.randint(0, height))
   

def draw_handler(canvas):
    global snow_y
    #Draw the bakground
    canvas.draw_polygon([(0, 0), (width, 0), 
                        (width, height), (0, height)], 1, "white", "LightBlue")
    for i in range(snow_flakes):
        snowflake_x = random.randint(0, width)
        snowflake_y = random.randint(0, height)
        canvas.draw_circle((snowflake_x, snow_y[i]), 10, 1, "white", "white")
        
    # the code for the snowman
    #Its body's code
    canvas.draw_circle((100, 300), 35, 1, "white", "white")
    canvas.draw_circle((100, 260), 25, 1, "white", "white")
    canvas.draw_circle((100, 300), 2, 1, "black", "black")
    canvas.draw_circle((100, 290), 2, 1, "black", "black")
    canvas.draw_circle((100, 260), 2, 1, "black", "black")
    canvas.draw_circle((100, 230), 20, 1, "white", "white")
    canvas.draw_line((100, 235), (105, 235), 3, "orange")
    canvas.draw_circle((90, 230), 1, 1, "black", "black")
    canvas.draw_circle((110, 230), 1, 1, "black", "black")
    #The snowman's arms
    canvas.draw_line((124, 260), (137, 280), 3, "brown")
    canvas.draw_line((76, 260), (63, 280), 3, "brown")
    #The ground's code
    canvas.draw_polygon([(0, height),(0, 320), (width, 320), (width, height)], 1, "white", "white")
    canvas.draw_line((80, 210), (125, 210), 5, "black")
    canvas.draw_line((90, 210), (115, 210), 4, "green")
    #The snowman's hat
    canvas.draw_polygon([(90, 210), (90, 180), (115, 180), (115, 210)], 5, "black", "black")
    canvas.draw_line((88, 205), (117, 205), 4, "green")  
    canvas.draw_line((440, 320), (440, 270), 7, "brown")
    #Th tree's code
    canvas.draw_polygon([(420, 270), (470, 270), (445, 180)], 40, "green")
    canvas.draw_circle((418, 250), 2, 10, "red", "red")
    canvas.draw_circle((436, 250), 2, 10, "blue", "blue")
    canvas.draw_circle((454, 250), 2, 10, "yellow", "yellow")
    canvas.draw_circle((471, 250), 2, 10, "red", "red")
    
    global x1 
    global x2
    x1 = x1 + 5
    canvas.draw_circle((x1, 100), 15, 1, "white", "yellow")
    canvas.draw_circle((x2, 100), 15, 1, "white", "gray")
    if x1 > 650:
        x2 = x2 + 5
        if x2 > 630: 
            x1 = -10
            x2 = x2 + 5
            


frame = simplegui.create_frame('Winter animation', width, height)
frame.set_draw_handler(draw_handler)

frame.start()

