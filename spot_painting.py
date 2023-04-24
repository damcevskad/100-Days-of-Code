# Day 18

import random
import turtle

# import colorgram
# colors = colorgram.extract("palette.jpg", 30)
# rgb_colors = []
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

turtle.colormode(255)

colors = [(208, 160, 101), (150, 75, 37), (231, 213, 97), (132, 34, 21), (191, 156, 15), (87, 33, 21), (238, 174, 153),
          (21, 57, 80), (41, 117, 63), (31, 93, 135), (196, 98, 88), (2, 81, 115), (10, 99, 77), (194, 163, 165),
          (109, 159, 185), (73, 76, 40), (179, 209, 168), (106, 140, 129), (37, 27, 35), (78, 153, 168), (46, 50, 47),
          (134, 163, 150), (234, 178, 180), (2, 72, 136), (125, 64, 66), (118, 36, 39)]

t = turtle.Turtle()
screen = turtle.Screen()
t.hideturtle()
t.speed(0)
t.setheading(222)
t.penup()
t.forward(300)
t.setheading(0)

for _ in range(10):
    for _ in range(10):
        t.shape("classic")
        t.penup()
        t.dot(20, random.choice(colors))
        t.forward(50)

    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(360)

screen.exitonclick()


