import turtle as turtle_module
import random
color_list = [(43, 1, 177), (78, 253, 172), (226, 149, 109), (230, 224, 253), (160, 3, 83), (3, 212, 100), (3, 139, 64), (246, 41, 128), (109, 108, 248), (252, 253, 53), (184, 184, 251), (211, 106, 4), (35, 35, 252), (176, 112, 248), (139, 0, 0), (252, 36, 35), (215, 114, 174), (50, 240, 56), (85, 248, 252), (17, 126, 144), (188, 40, 109), (9, 208, 216), (22, 5, 108), (97, 8, 53), (230, 163, 206), (205, 119, 34), (113, 7, 3), (239, 165, 161), (8, 114, 16), (244, 14, 16), (6, 111, 114)]

screen = turtle_module.Screen()
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
next_line = -250

tim.speed(0)

for y in range (10):
   tim.setpos(-300, next_line)
   next_line += 50
   for x in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

