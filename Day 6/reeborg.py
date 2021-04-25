def turn_right():
    turn_left()
    turn_left()
    turn_left()    

def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
def hurdle():
    move()
    jump()


while not at_goal():
    if right_is_clear():
            turn_right()
            move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        


