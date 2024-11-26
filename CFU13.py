#Jannatul Jami Period 1 and 2 
#11/26/2024
#CFU 13

import simplegui

def draw_handler(canvas):
    #Where the drawing happens
    canvas.draw_point([55, 70], "white")
    canvas.draw_point([145, 70], "white")
    canvas.draw_point([52, 145], "white")
    canvas.draw_point([59, 147], "white")
    canvas.draw_point([66, 149], "white")
    canvas.draw_point([73, 151], "white")
    canvas.draw_point([80, 153], "white")
    canvas.draw_point([87, 155], "white")
    canvas.draw_point([94, 157], "white")
    canvas.draw_point([101, 159], "white")
    canvas.draw_point([108, 162], "white")
    canvas.draw_point([113, 159], "white")
    canvas.draw_point([120, 157], "white")
    canvas.draw_point([127, 155], "white")
    canvas.draw_point([134, 153], "white")
    canvas.draw_point([141, 151], "white")
    canvas.draw_point([148, 149], "white")
frame = simplegui.create_frame("Python Drawing", 200, 200)
frame.set_draw_handler(draw_handler)
frame.start()
