from turtle import Turtle
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.write(f"Score = {self.score}", True, align="center", font= FONT)


    def scoreupdate(self):
        self.score += 1
        self.clear()
        self.goto(0, 280)
        self.write(f"Score = {self.score}", True, align="center", font= FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", True, align="center", font= FONT)


