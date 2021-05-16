from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Russpong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.tracer(0)
ball = Ball((0,0))
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(r_paddle.paddleup, "Up")
screen.onkeypress(r_paddle.paddledown, "Down")
screen.onkeypress(l_paddle.paddleup, "w")
screen.onkeypress(l_paddle.paddledown, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with r_paddle

    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(l_paddle) < 55 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.l_point()





screen.exitonclick()
