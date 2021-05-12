import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

def move_forward():
    tim.forward(15)
def move_backward():
    tim.backward(15)
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right,"d")
screen.onkey(turtle.resetscreen, "c")

screen.exitonclick()
