#Jannnatul Jami
#Period 1 and 2 
#12/12/2024


import simplegui
import random
snow_y = []
snow_x = []

width = 600
height = 400
snow_flakes = 5
snowfall_speed= 1

for i in range(snow_flakes):
    snow_y.append(random.randint(0, height))
    snow_x.append(random.randint(width, 0))

def draw_handler(canvas):
    global snow_y
    global snow_x
    #Draw the bakground
    canvas.draw_polygon([(0, 0), (width, 0), 
                        (width, height), (0, height)], 1, "white", "LightBlue")
    for i in range(snow_flakes):
        snowflake_x = random.randint(0, width)
        snowflake_y = random.randint(0, height)
        canvas.draw_circle((snowflake_x, snow_y[i]), 10, 1, "white", "white")
                           
frame = simplegui.create_frame('TWinter animation', width, height)
frame.set_draw_handler(draw_handler)

frame.start()
