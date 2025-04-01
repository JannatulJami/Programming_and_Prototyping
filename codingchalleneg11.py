#Jannatul Jami
#Period 1 and 2


import turtle
angle = 0.0
def draw_spiral(t, n, length, a, b):
  for i in range(n):
    t.forward(length)
    thetha = 1 / (angle * a + b)
    t.left(thetha)
    thetha += 0.1

pepito = turtle.Turtle()
pepito.speed(0)
screen = turtle.Screen()

draw_spiral(pepito, 1000, 5, 0.5, 0.2)
