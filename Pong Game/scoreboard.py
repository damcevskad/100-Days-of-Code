from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(0, 230)
        self.write(f"{self.left_score} : {self.right_score}", align="center", font=("Courier", 50, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 50, "bold"))

