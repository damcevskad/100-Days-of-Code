import random
import turtle

turtle_colors = ["maroon", "light salmon", "dark cyan", "olive", "indigo"]
turtles = []

screen = turtle.Screen()
screen.setup(height=400, width=500)
bet = screen.textinput(title="Make Your Bet", prompt="Who are you betting on? ")

x = 100
for index in range(5):
    t = turtle.Turtle("turtle")
    t.penup()
    t.color(turtle_colors[index])
    t.goto(-230, x)
    x -= 50
    turtles.append(t)

race = True
while race:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            winner_turtle = turtle.pencolor()
            if winner_turtle == bet:
                print("Congrats! You won the bet!")
                race = False
            else:
                print("Better luck next time. You lost the bet.")
                race = False

screen.exitonclick()
