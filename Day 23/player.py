from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.speed(0)
        self.goto((STARTING_POSITION))
        self.color("black")
        self.car_speed = 0.1

    def jump(self):
        self.forward(MOVE_DISTANCE)

    def playerreset(self):
        self.clear()
        self.car_speed *= .9
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto((STARTING_POSITION))
        self.color("black")
