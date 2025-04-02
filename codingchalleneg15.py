#Jannatul Jami
#Period 1 and 2
import turtle

def koch(t, length):
  if length < 3:
    t.forward(length)
  else:
    koch(t, length / 3)    
    t.left(60)
    koch(t, length / 3)
    t.right(120)
    koch(t, length / 3)
    t.left(60)
    koch(t, length / 3)
   
def snowflake(t, length):
  for i in range(3):
    koch(t, length)
    t.right(120)

pepito = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")
pepito.speed(0)
pepito.penup()
pepito.goto(-150, 100) 
pepito.pendown()
snowflake(pepito, 300)
turtle.done()
