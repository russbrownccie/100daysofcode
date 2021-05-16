from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.speed(0)
        self.goto(position)

    def paddleup(self):
        if self.ycor() < 260:
            self.goto(self.xcor(), self.ycor() + 20)


    def paddledown(self):
        if self.ycor() > -260:
            self.goto(self.xcor(), self.ycor() - 20)
