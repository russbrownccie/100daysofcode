from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed("fastest")
        random.x = random.randint(-280, 280)
        random.y = random.randint(-280, 280)
        self.goto(random.x, random.y)
        self.refresh()

    def refresh(self):
        random.x = random.randint(-280, 280)
        random.y = random.randint(-280, 280)
        self.goto(random.x, random.y)
