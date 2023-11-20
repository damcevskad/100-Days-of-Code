from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        self.goto(x, y)

    def new_food(self):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        self.goto(x, y)


