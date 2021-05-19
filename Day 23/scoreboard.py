from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

    def write_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write (f"Level {self.level}:", align="left", font = (FONT))

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.write_scoreboard()

    def gameover(self):

        self.hideturtle()
        self.goto (0,0)
        self.write (f"GAME OVER", align="center", font = (FONT))
