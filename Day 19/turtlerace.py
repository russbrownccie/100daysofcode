

import random
is_race_on = False
from turtle import Turtle, Screen
colors = ["red", "orange", "yellow", "green", "blue", "purple" ]
y_axis = [-70, -40, -10, 20, 50, 80]
screen = Screen()
screen.setup(width=500, height=400)
all_turtles= []
for item in range (6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[item])
    new_turtle.goto(-230, y_axis[item])
    all_turtles.append(new_turtle)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?  Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > +230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print (f"You won! - the {winning_color} turtle is the winner!")
            else:
                print (f"You lost - the {winning_color} turtle is the winner!")
                print(all_turtles)
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()
