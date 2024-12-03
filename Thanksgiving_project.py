import simplegui


frame = simplegui.create_frame("Thanksgiving Drawing", 600, 400)
frame.set_canvas_background("#p")

# Draw handler function
def draw(canvas):
    # Example: Drawing a circle
    canvas.draw_polygon([(130, 50), (120, 400), (420, 400), (420, 50)], 300, "Brown")
    canvas.draw_circle((300, 200), 50, 5, "Brown", "Orange")
    canvas.draw_circle((300, 200), 60, 18, "Silver")
    canvas.draw_circle((300, 200), 5, 10, "Red")
    canvas.draw_line((311, 153), (311, 250), 2, "Brown")
    canvas.draw_line((289, 153), (289, 250), 2, "Brown")
    canvas.draw_line((335, 165), (335, 237), 2, "Brown")
    canvas.draw_line((265, 165), (265, 237), 2, "Brown")
    # Example: Drawing a line
    #canvas.draw_line((100, 200), (500, 200), 3, "Black")
    # Example: Drawing a polygon
    # Example: Drawing a point
    #canvas.draw_point((300, 200), "Blue")
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
    canvas.draw_line((440, 130), (440, 140), 3, "#7B3F00")
    canvas.draw_circle((440, 150), 3, 6, "#7B3F00")
    canvas.draw_circle((440, 150), 30, 8, "#7B3F00")
    canvas.draw_circle((440, 150), 50, 8, "#7B3F00")
    canvas.draw_polygon([(300, 90), (275, 115), (325, 115)], 5, "Orange", "Yellow")
    canvas.draw_line((300, 88), (300, 113), 3, "Orange")
    canvas.draw_line((300, 100), (317, 105), 3, "Orange")
    canvas.draw_line((300, 100), (283, 105), 3, "Orange")
    canvas.draw_line((300, 118), (300, 128), 5, "Red")
    canvas.draw_line((300, 107), (282, 112), 3, "Orange")
    canvas.draw_line((300, 107), (318, 112), 3, "Orange")
    canvas.draw_polygon([(135, 300), (115, 325), (155, 325)], 5, "Red", "Orange")
    canvas.draw_line((135, 300), (135, 325), 3, "Red")
    canvas.draw_line((135, 310), (153, 320), 3, "Red")
    canvas.draw_line((135, 310), (117, 320), 3, "Red")
    canvas.draw_line((135, 325), (135, 335), 3, "Red")

# Assign draw handler to the frame
frame.set_draw_handler(draw)

# Start the frame
frame.start()
