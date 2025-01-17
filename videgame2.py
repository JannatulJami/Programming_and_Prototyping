import simplegui
import random

width = 600
height= 700
room1 = True 
room2 = False
room3 = False
frame = None
char_inventory = []
#character Variables
char_x = width // 2 
char_y = height - 100
char_health = 100
char_score = 0
twinkle_frame = 0 
victory = False
items = []
char_inventory = []

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
    global twinkle_frame
    global victory
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
     # Draw items
    generate_objects()
    for item in items:
        canvas.draw_circle((item["x"], item["y"]), 10, 2, "gold", "yellow")
    #stats
    canvas.draw_text("Health: " + str(char_health), (10, 20), 20, "white")
    canvas.draw_text("Score: " + str(char_score), (10, 50), 20, "white")
    
    
#Twinkling stars
    for i in range(12):
        x = i * 50 + 20
        y = 50 + (i % 2) * 40
        size = 4 if (twinkle_frame // 10) % 2 == 0 else 6
        canvas.draw_circle((x, y), size, 1, "White", "White")

    twinkle_frame += 1  # Update counter
#Draw a charcter
    canvas.draw_circle((char_x, char_y), 15, 2, "#da9cb6", "#d8a9de")
#Drawing the inventory
    canvas.draw_text("Inventory:", (10, 80), 20, "white")
    y_offset = 100
    for item in char_inventory:
        canvas.draw_text("- " + item, (10, y_offset), 20, "white")
        y_offset += 20

if char_health <= 0:
    canvas.draw_text("You Win!", (100, height //2), 30, "green")
    victory = True
def keydown(key):
    global char_x, char_y, char_health, char_score
    if victory:
        return
    if key == simplegui.KEY_MAP["up"] and char_y > 15:
        char_y -= 10
    elif key == simplegui.KEY_MAP["down"] and char_y <  height - 15:
        char_y += 10
    elif key == simplegui.KEY_MAP["left"] and char_x > 15:
        char_x -= 10
    elif key == simplegui.KEY_MAP["right"] and char_x <  width - 15:
        char_x += 10

# Generate items and threats
def generate_objects():
    global items
    if random.random() < 0.2:
        new_item = {"x": random.randint(20, width - 20), "y": 0}
        items.append(new_item)
def add_item(item):
    if item not in char_inventory:
        char_inventory.append(item)
def increase_score(amount):
    global char_score
    char_score += amount

def use_item(item):
    global char_health
    if item == "Health Potion!":
        if item in char_inventory:
            char_health += 20
            char_inventory.remove(item)
            print("You used a Health Potion and restored 20 health!")
        else:
            print("you don't have a health potion")
                  

def explore_room():
    global char_health, char_score, char_inventory, victory
    if victory:
        return
    event = random.randint(1, 6)
    if event == 1:
        add_item("Health Potion!")
        print(add_item)
    elif event == 2:
        add_item("You get a sword")
        print(add_item)
        increase_score(15)
    elif event == 3:
        add_item("You get a shield")
        print(add_item)
        increase_score(10)
    elif event == 4:
        char_inventory.remove("You get a shield")
        increase_score(-10)
    elif event == 5:
        char_inventory.remove("You get a sword")
        increase_score(-15)
def toggle_room1():
    global room1, room2, room3
    room1 = True
    room2 = False
    room3 = False

def toggle_room3():
    global room1, room2, room3
    room3 = True
    room2 = False
    room1 = False
def toggle_room2():
    global room2, room1, room3
    room2 = True
    room1 = False
    room3 = False
        
def create_frame():
    global frame
    frame = simplegui.create_frame("Final project", width, height)
    frame.set_draw_handler(draw)
    frame.set_keydown_handler(keydown)
    frame.add_button("1st room", toggle_room1, 150)
    frame.add_button("2nd room", toggle_room2, 150)
    frame.add_button("3rd room", toggle_room3, 150)
    frame.add_button("Explore Room", explore_room, 150)
    frame.start()
    
    
create_frame()
