import turtle as t
from time import sleep


t.speed(0)
t.bgcolor("black")

colours = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(360):
    t.pencolor(colours[i%6])
    t.width(i/250 + 1)
    t.forward(i)
    t.left(59)




sleep(5)
t.hideturtle()