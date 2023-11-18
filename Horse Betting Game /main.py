import random
from turtle import Turtle, Screen

horse_colors = {"red.gif": "red",
                "orange.gif": "orange",
                "pink.gif": "pink",
                "green.gif": "green",
                "blue.gif": "blue"}

screen = Screen()
screen.setup(height=600, width=800)
screen.title("Horse Betting")
bet = screen.textinput(title="Make Your Bet", prompt="Who are you betting on? ")

for key in horse_colors:
    screen.addshape(key)

horses = []
x = 200
for key in horse_colors.keys():
    horse = Turtle(key)
    horse.penup()
    horse.goto(-330, x)
    x -= 100
    horses.append(horse)

score = Turtle()
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 0)

race = True
while race:
    for horse in horses:
        horse.forward(random.randint(0, 30))
        if horse.xcor() > 335:
            winner = horse_colors[horse.shape()]
            if winner == bet:
                score.write("Congrats! You won the bet!", font=("Times", 35, "bold"), align="center")
                race = False
            else:
                score.write("Better luck next time! You lost the bet.", font=("Times", 35, "bold"), align="center")
                race = False

screen.exitonclick()
