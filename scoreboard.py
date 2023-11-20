from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt") as hs:
            self.high_score = hs.read()
        self.hideturtle()
        self.penup()
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"SCORE: {self.score}    HIGH SCORE: {self.high_score}", align="center", font=("Courier", 20, "normal"))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as hs:
                hs.write(str(self.high_score))
        self.score = 0

    # def game_end(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=("Courier", 20, "normal"))


