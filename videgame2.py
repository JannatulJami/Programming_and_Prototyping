import simplegui
import random

width = 600
height= 700
room1 = True 
room2 = True
room3 = True
frame = None
def room1_drawing(canvas):
    canvas.draw_polygon([(0, 0), (width, 0), 
                        (width, height), (0, height)], 1, "white", "#AF958F")
    canvas.draw_polygon([(0, height), (0, 530), (width, 530), (width, height)], 1, "black", "#725E59")
    canvas.draw_polygon([(400, 200), (510, 200), (510, 530), (400, 530)], 1, "black", "#725E59")

    #Code starts and a moon and maybe clouds
def room2_drawing(canvas):
    canvas.draw_polygon([(0, 0), (width, 0), 
                        (width, height), (0, height)], 1, "white", "#ebc4f0")
    canvas.draw_polygon([(0, height), (0, 530), (width, 530), (width, height)], 1, "black", "#735e50")
    canvas.draw_polygon([(300, 200), (510, 200), (510, 530), (300, 530)], 1, "black", "#dad2e3")
    for i in range(0, 200, 25):
        canvas.draw_polygon([(i + 305, 235), (i + 315, 235), (i + 315,  255), (i + 305,  255)], 1, "black", "#fffbd9")
    for i in range(0, 200, 25):
        canvas.draw_polygon([(i + 305, 285), (i + 315, 285), (i + 315,  305), (i + 305,  305)], 1, "black", "#fffbd9")
    for i in range(0, 200, 25):
        canvas.draw_polygon([(i + 305, 335), (i + 315, 335), (i + 315,  355), (i + 305,  355)], 1, "black", "#fffbd9")
    for i in range(0, 200, 25):
        canvas.draw_polygon([(i + 305, 385), (i + 315, 385), (i + 315,  405), (i + 305,  405)], 1, "black", "#fffbd9")
    for i in range(0, 200, 25):
        canvas.draw_polygon([(i + 305, 435), (i + 315, 435), (i + 315,  455), (i + 305,  455)], 1, "black", "#fffbd9")
    for i in range(0, 200, 25):
        canvas.draw_polygon([(i + 305, 485), (i + 315, 485), (i + 315,  505), (i + 305,  505)], 1, "black", "#fffbd9")

        #Make astroids fall here
def room3_drawing(canvas):
    canvas.draw_polygon([(0, 0), (width, 0), 
                        (width, height), (0, height)], 1, "white", "#ffcde2")
    canvas.draw_polygon([(0, height), (0, 530), (width, 530), (width, height)], 1, "black", "#FFF5F3")
    canvas.draw_polygon([(300, 250), (510, 250), (510, 530), (300, 530)], 1, "black", "#c496a9")
    canvas.draw_circle((470, 100), 40, 1, "black", "#ff60a2")                                                                                                                                                                                                                                                                                                                                                                                                                                             
def draw(canvas):
    quadrant_width = width / 2
    quadrant_height = height / 2
    
    # Only draw if show_faces is True
    if room1:
        # Top-left face (happy)
        room1_drawing(canvas)
    if room2:
        room2_drawing(canvas)
    if room3:
        room3_drawing(canvas)
def toggle_room1():
    global room1
    room1 = not room1

def toggle_room3():
    global room3
    room3 = not room3
def toggle_room2():
    global room2
    room2 = not room2
        
def create_frame():
    global frame
    frame = simplegui.create_frame("Emoji project", width, height)
    frame.set_draw_handler(draw)
    
    frame.add_button("1st room", toggle_room1, 150)
    frame.add_button("2nd room", toggle_room2, 150)
    frame.add_button("3rd room", toggle_room3, 150)
    frame.start()
    
    
create_frame()