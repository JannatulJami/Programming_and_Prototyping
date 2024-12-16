#Jannnatul Jami
#Period 1 and 2 
#12/12/2024


import simplegui
import random
snow_y = []

width = 600
height = 400
snow_flakes = 5
snowfall_speed= 1

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
    canvas.draw_circle((100, 300), 35, 1, "white", "white")
    canvas.draw_circle((100, 260), 25, 1, "white", "white")
    canvas.draw_circle((100, 300), 2, 1, "black", "black")
    canvas.draw_circle((100, 290), 2, 1, "black", "black")
    canvas.draw_circle((100, 260), 2, 1, "black", "black")
    canvas.draw_circle((100, 230), 20, 1, "white", "white")
    canvas.draw_circle((90, 230), 1, 1, "black", "black")
    canvas.draw_circle((110, 230), 1, 1, "black", "black")
    canvas.draw_line((124, 260), (137, 280), 3, "brown")
    canvas.draw_polygon([(0, height),(0, 320), (width, 320), (width, height)], 1, "white", "white")
   
                           
frame = simplegui.create_frame('Winter animation', width, height)
frame.set_draw_handler(draw_handler)

frame.start()
