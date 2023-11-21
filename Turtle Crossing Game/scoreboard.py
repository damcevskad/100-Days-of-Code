from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-235, 260)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "bold"))

    def show_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "bold"))

    def game_end(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 20, "bold"))
