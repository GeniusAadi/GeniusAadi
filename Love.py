import turtle
#background colour
x=turtle.Screen()
x.bgcolor("black")
#variable
x = turtle.Turtle()
#speed
x.speed(0)
#pensize
x.pensize(15)
#coloring
x.color("red")
x.begin_fill()
#making heart
x.left(140)
x.forward(200)
for i in range(200):
    x.right(1)
    x.forward(2)
x.left(118)
for i in range(200):
    x.right(1)
    x.forward(2)
x.right(5)
x.forward(215)
#ending color fill
x.end_fill()
# making I
x.penup()
x.goto(-300,300)
x.pendown()
x.right(35)
x.forward(150)
x.forward(-75)
x.left(90)
x.forward(300)
x.right(90)
x.forward(75)
x.forward(-150)
#making U
x.penup()
x.goto(300,300)
x.pendown()
x.left(90)
x.forward(250)
for i in range(170):
    x.left(1)
    x.forward(1)
x.left(10)
x.forward(260)
#command to hold turtle page
turtle.done()