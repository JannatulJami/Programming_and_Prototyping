#Jannatul Jami
#Period 1 and 2
#Amrch18;2025
import turtle
import math

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.forward(length * n)
    t.left(angle)
    draw(t, length, n-1)
    t.right(2 * angle)
    draw(t, length, n-1)
    t.left(angle)
    t.backward(length * n)

def polygon(t, length, n):
  if n == 0:
      return
  angle = 360 / n
  for i in range(n):
        t.forward(length)
        t.left(angle)
        

def square(t, length):
  angle = 90
  for i in range(4):
        t.forward(length)
        t.left(angle)
bob = turtle.Turtle()

def circle(t, r, length):
  n = int(r * 2 * math.pi)
  angle = 360 / n
  for i in range(n):
        t.forward(length)
        t.left(angle)
draw(bob, 10, 4)  

#no overlapping
bob.penup()
bob.goto(-50, -50) #diff pos
bob.pendown()


polygon(bob, 10, 5)
square(bob, 90)
circle(bob, 5, 3)

turtle.done()

