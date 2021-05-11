from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("turtle")
no_of_sides = 3

while no_of_sides < 11:

    tim.color(random.randint(0,255), random.randint(0,255), random.randint(0, 255))

    for sides in range(no_of_sides):
        angle = 360/no_of_sides
        tim.forward(100)
        tim.right(angle)
    no_of_sides += 1
