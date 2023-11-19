import random
import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.shape("classic")
colors = ["light steel blue", "dark khaki", "burlywood", "thistle", "dark sea green", "navajo white", "tan",
          "light sea green", "pale goldenrod", "blanched almond", "lavender", "bisque", "light cyan"]

directions = [0, 90, 180, 270]

for _ in range(200):
    t.speed(0)
    t.width(15)
    t.color(random.choice(colors))
    t.setheading(random.choice(directions))
    t.forward(30)


screen.exitonclick()
