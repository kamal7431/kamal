from turtle import *

bgcolor("green")
speed(0)
pensize(2)
hideturtle()

for i in range(90):
    color("olive")
    circle(i)
    color("cyan")
    circle(i * 1.5)

done()