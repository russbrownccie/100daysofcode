from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
x_axis = 0

snake = Snake()
food = Food()
screen.listen()
gamescore = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        gamescore.scoreupdate()
    #Detect collision with wall

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        gamescore.gameover()

    #Detect collision with tale
    # if head collides with any segment in tail, game over
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            gamescore.gameover()

screen.exitonclick()
