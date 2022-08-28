from turtle import *
import turtle
 
tur = turtle.Turtle()
 
def eyes(color, radius):
    tur.down()
    tur.fillcolor(color)
    tur.begin_fill()
    tur.circle(radius)
    tur.end_fill()
    tur.up()
 
 
tur.fillcolor('cyan')
tur.begin_fill()
tur.circle(100)
tur.end_fill()
tur.up()
 
tur.goto(-40, 120)
eyes('white', 15)
tur.goto(-37, 125)
eyes('blue', 5)
tur.goto(40, 120)
eyes('white', 15)
tur.goto(40, 125)
eyes('blue', 5)
 
tur.goto(0, 75)
eyes('red', 8)
 
tur.goto(-40, 85)
tur.down()
tur.right(90)
tur.circle(40, 180)
tur.up()
 

tur.goto(-10, 45)
tur.down()
tur.right(180)
tur.fillcolor('red')
tur.begin_fill()
tur.circle(10, 180)
tur.end_fill()
tur.hideturtle()
turtle.done()