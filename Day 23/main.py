import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
turtle = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkeypress(turtle.jump, "Up")


game_is_on = True
while game_is_on:
    time.sleep(turtle.car_speed)
    screen.update()
    score.write_scoreboard()
    car_manager.create_car()
    car_manager.move_cars()


    if turtle.ycor() >= 300:
        turtle.playerreset()
        score.update_scoreboard()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            score.gameover()
            game_is_on = False

screen.exitonclick()
