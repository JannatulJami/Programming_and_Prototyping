import simplegui


frame = simplegui.create_frame("Thanksgiving Drawing", 600, 400)

# Draw handler function
def draw(canvas):
    # Example: Drawing a circle
    canvas.draw_polygon([(130, 50), (120, 400), (420, 400), (420, 50)], 300, "Brown")
    canvas.draw_circle((300, 200), 50, 5, "Brown", "Orange")
    # Example: Drawing a line
    #canvas.draw_line((100, 200), (500, 200), 3, "Black")
    # Example: Drawing a polygon
    canvas.draw_polygon([(250, 250), (350, 250), (300, 300)], 5, "Red", "Yellow")
    # Example: Drawing a point
    canvas.draw_point((300, 200), "Blue")
    canvas.draw_polygon([(200, 80), (175, 115), (225, 115)], 5, "Orange", "Yellow")
    canvas.draw_line((200, 95), (219, 105), 3, "Orange")
    canvas.draw_line((200, 95), (181, 105), 3, "Orange")
    canvas.draw_line((200, 105), (222, 115), 3, "Orange")
    canvas.draw_line((200, 105), (178, 115), 3, "Orange")
    canvas.draw_line((200, 115), (200, 125), 3, "Red")
    canvas.draw_line((200,80), (200, 115), 3, "Orange")
    canvas.draw_circle((440, 150), 60, 30, "#C0C0C0")
    canvas.draw_circle((440, 150), 30, 60, "#D3B683")
    canvas.draw_line((440, 165), (440, 170), 3, "#7B3F00")
    canvas.draw_line((430, 150), (420, 150), 3, "#7B3F00")
    canvas.draw_line((450, 150), (465, 150), 3, "#7B3F00")
    canvas.draw_circle((440, 150), 3, 6, "#7B3F00")
    canvas.draw_circle((440, 150), 30, 8, "#7B3F00")
    canvas.draw_polygon([(300, 90), (275, 115), (325, 115)], 5, "Orange", "Yellow")
    canvas.draw_line((300, 88), (300, 113), 3, "Orange")
    canvas.draw_line((300, 100), (317, 105), 3, "Orange")
    canvas.draw_line((300, 100), (283, 105), 3, "Orange")
    canvas.draw_line((300, 118), (300, 128), 5, "Red")
    canvas.draw_line((300, 107), (282, 112), 3, "Orange")
    canvas.draw_line((300, 107), (318, 112), 3, "Orange")
    canvas.draw_polygon([(135, 300), (115, 325), (155, 325)], 5, "Red", "Orange")
  

# Assign draw handler to the frame
frame.set_draw_handler(draw)

# Start the frame
frame.start()
