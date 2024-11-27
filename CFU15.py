#Jannatul Jami
#Period 1 and 2
#CFU 15

import simplegui

def draw_handler(canvas):
    canvas.draw_point([100,100], "red")
    canvas.draw_polygon([(30, 45), (30, 75), (45, 45)], 15, "#F1D3E3")
    canvas.draw_polygon([(100, 45), (100, 75), (115, 45)], 15, "#F1D3E3")
    canvas.draw_polygon([(80, 120), (110, 140), (140, 120)], 16, "#F1D3E3")
    #canvas.draw_circle((150, 135), 5, 5, "purple")
#create the frame
frame = simplegui.create_frame("CFU 15 Happy Shapes", 200, 200)
frame.set_canvas_background("white")
frame.set_draw_handler(draw_handler)
frame.start()
