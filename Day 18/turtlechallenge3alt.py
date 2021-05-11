from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("turtle")
no_of_sides = 3

def draw_shape(num_sides):
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    for sides in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


while no_of_sides < 11:
    draw_shape(no_of_sides)
    no_of_sides +=1
