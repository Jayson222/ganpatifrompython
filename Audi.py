import turtle
vr = turtle.Turtle()

vr.pensize(7)
turtle.Screen().bgcolor("black")
#Bg color is use to set the background color
vr.pencolor("#D0CFCF")
#pencolor() is use to set the Pen color
vr.speed(10)
for i in range(4):
  vr.penup()
#Penup() ensures that the moving object you've created does not draw anything on the window.
  vr.goto(i*70, 0)
#goto() : can be used to set a position for turtle.
  vr.pendown()
#pendown() tell the turtle to leave ink on the screen as it moves or not to leave ink.
  vr.circle(50)
#circle() : use for to draw a circle
vr.color("white")
vr.penup()
vr.goto(77, -40)
vr.pendown()
#creating a label
vr.write("Audi",font=("Arial", 16, "bold","italic"))