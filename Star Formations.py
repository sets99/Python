from turtle import *
from shapes import *
Saksham = turtle
Saksham.shape("turtle")
Saksham.speed(10)

draw_star(Saksham, "red", 50, 25, 0)
draw_star(Saksham, "blue", 50, 0, 0)
draw_star(Saksham, "yellow", 50, -25, 0)

Saksham.penup()
Saksham.goto(0,-50)
Saksham.color("black")
Saksham.write("Coding Rocks!", None, "center", "32pt bold")
Saksham.goto(0,-80)
