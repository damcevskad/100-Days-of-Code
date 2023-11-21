from turtle import Turtle


class Players(Turtle):
    def __init__(self, a, b):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(a, b)

    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
