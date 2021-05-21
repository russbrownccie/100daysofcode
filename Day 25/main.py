import turtle
import pandas
ALL_STATES = 50
FONT = ("Ariel", 8, "normal")

# read the CSV file and make a list of states to search through
data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
]

# setup the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# set variables for number of states gotten right
current_states = 0
# set up list for correct guesses to be compared to
list_of_current_states = []
# set up turtle object to move and write the text
turtle_pen = turtle.Turtle()
# set up initial box prompts
title_input = "Guess The State"
prompt_input = "What's another state's name?"



while current_states != 50:
    turtle_pen.hideturtle()
    # make your guess
    answer_state = screen.textinput(title=f"{title_input}", prompt=f"{prompt_input}")
    answer_state = answer_state.title()
    # Provide an exit out that prints a list of missed states
    if answer_state == "Exit":
    # Provide an exit out that prints a list of missed states
    if answer_state == "Exit":
        missed_states = [guesses for guesses in states_list if guesses not in list_of_current_states]

        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missed_states.csv")
        break
    # if guess is right but already chosen
    if answer_state in list_of_current_states:
        prompt_input = "Already guessed - try another"
    # if guess is right ant not chosen yet
    elif answer_state in states_list and answer_state not in list_of_current_states:
        current_states += 1
        title_input = f"{current_states}/50 correct"
        prompt_input = "Correct, guess another state"
        list_of_current_states.append(answer_state)
        output = (data[data.state == answer_state])
        turtle_pen.speed(0)
        turtle_pen.penup()
        turtle_pen.goto(int(output.x - 15), int(output.y))
        turtle_pen.write(f"{answer_state}", font=FONT)
    # if guess is wrong
    else:
        prompt_input = "Not a state - Guess Again"

if current_states == 50:
    screen.title("Congratulations! - You won the U.S. States Game")
    screen.exitonclick()
