import turtle
import math

def triangleLength(t, r, angle):
  y = r * math.sin(math.radians(angle))
  t.rt(angle)
  t.fd(r)
  t.lt(90+angle)
  t.fd(y*2)
  t.lt(90 + angle)
  t.fd(r)
  t.lt(180-angle)
 
def pie(t, r, n):
  angle = 360/n
  for i in range(n):
    triangleLength(t, r, angle/2)
    t.rt(angle)
def move(t,length):
  t.pu()
  t.fd(length)
  t.pd()
pepito = turtle.Turtle()
pepito.speed(3)


pie(pepito, 30, 5)
