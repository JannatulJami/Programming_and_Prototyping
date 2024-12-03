import simplegui


frame = simplegui.create_frame("Thanksgiving Drawing", 600, 400)
#background color for the image
frame.set_canvas_background("#p")

# Draw handler function
def draw(canvas):
    #Drawing the brown table the food is set on using the polygon function
    canvas.draw_polygon([(200, 50), (200, 400), (420, 400), (420, 50)], 300, "Brown")
    # Drawing a Cherry pie
    canvas.draw_circle((300, 200), 50, 5, "Brown", "Orange")
    #Drawing the silver plate
    canvas.draw_circle((300, 200), 60, 18, "Silver")
    #The red filling in a circle in the middle
    canvas.draw_circle((300, 200), 5, 10, "Red")
    #Drawing liness that go vertical n the pie
    canvas.draw_line((311, 153), (311, 250), 2, "Brown")
    canvas.draw_line((289, 153), (289, 250), 2, "Brown")
    canvas.draw_line((335, 165), (335, 237), 2, "Brown")
    canvas.draw_line((265, 165), (265, 237), 2, "Brown")
    # Example: Drawing a leaf with the polygon function
    canvas.draw_polygon([(200, 80), (175, 115), (225, 115)], 5, "Orange", "Yellow")
    #Drawing lines for the leaves
    canvas.draw_line((200, 95), (219, 105), 3, "Orange")
    canvas.draw_line((200, 95), (181, 105), 3, "Orange")
    canvas.draw_line((200, 105), (222, 115), 3, "Orange")
    canvas.draw_line((200, 105), (178, 115), 3, "Orange")
    canvas.draw_line((200, 115), (200, 125), 3, "Red")
    canvas.draw_line((200,80), (200, 115), 3, "Orange")
    #Drawing a choclate pie
    #Using circle function to draw the cholcate pie with brown, and light brown colors
    canvas.draw_circle((440, 150), 60, 30, "#C0C0C0")
    canvas.draw_circle((440, 150), 30, 60, "#D3B683")
    #Drawing lines on the choclate pie
    canvas.draw_line((440, 165), (440, 170), 3, "#7B3F00")
    canvas.draw_line((430, 150), (420, 150), 3, "#7B3F00")
    canvas.draw_line((450, 150), (465, 150), 3, "#7B3F00")
    canvas.draw_line((440, 130), (440, 140), 3, "#7B3F00")
    #Draw the filling of the cake using dark brown
    canvas.draw_circle((440, 150), 3, 6, "#7B3F00")
    canvas.draw_circle((440, 150), 30, 8, "#7B3F00")
    canvas.draw_circle((440, 150), 50, 8, "#7B3F00")
    #Drawing a nother leaf but smaller
    #Using the polygon function for the leaf
    canvas.draw_polygon([(300, 90), (275, 115), (325, 115)], 5, "Orange", "Yellow")
    # The lines for the smaller leaf
    canvas.draw_line((300, 88), (300, 113), 3, "Orange")
    canvas.draw_line((300, 100), (317, 105), 3, "Orange")
    canvas.draw_line((300, 100), (283, 105), 3, "Orange")
    canvas.draw_line((300, 118), (300, 128), 5, "Red")
    canvas.draw_line((300, 107), (282, 112), 3, "Orange")
    canvas.draw_line((300, 107), (318, 112), 3, "Orange")
    # Creating another smaller leaf but red
    canvas.draw_polygon([(135, 300), (115, 325), (155, 325)], 5, "Red", "Orange")
    #Using line function for the lines on the leaf
    canvas.draw_line((135, 300), (135, 325), 3, "Red")
    canvas.draw_line((135, 310), (153, 320), 3, "Red")
    canvas.draw_line((135, 310), (117, 320), 3, "Red")
    canvas.draw_line((135, 325), (135, 335), 3, "Red")
    #Creating a pumpkin
    #Using the polygon feature to create a pumpkin
    canvas.draw_polygon([(90, 50), (90, 100), (145, 100), (145, 50)], 50, "Orange")
    #Using the lines features to create the pumpkin grooves
    canvas.draw_line((105, 25), (105, 125), 3, "#FFB66B")
    canvas.draw_line((130, 25), (130, 125), 3, "#FFB66B")
    canvas.draw_line((140, 25), (140, 125), 3, "#FFB66B")
    canvas.draw_line((95, 25), (95, 125), 3, "#FFB66B")
    canvas.draw_line((105, 25), (105, 125), 3, "#FFB66B")
    canvas.draw_line((155, 25), (155, 125), 3, "#FFB66B")
    canvas.draw_line((80, 25), (80, 125), 3, "#FFB66B")
    #Pumpkin stem created using the polygpn funct
    canvas.draw_polygon([(105, 20), (100, 20), (110,32), (110, 30)], 5, "Green")

# Assign draw handler to the frame
frame.set_draw_handler(draw)

# Start the frame
frame.start()
# Assign draw handler to the frame
frame.set_draw_handler(draw)

# Start the frame
frame.start()
