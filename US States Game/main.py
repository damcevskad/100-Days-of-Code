import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess The States Game")
screen.addshape("blank_states_img.gif")
screen.setup(width=725, height=490)
turtle.shape("blank_states_img.gif")

states_data = pandas.read_csv("50_states.csv")
states_list = list(states_data.state)
guessed_states = []
states_to_learn = []

while len(guessed_states) < 50:
    state = screen.textinput(prompt="Enter state: ", title=f"{len(guessed_states)}/50 States").title()

    if state == "Exit":
        states_to_learn = [state for state in states_list if state not in guessed_states]
        not_guessed_states = pandas.DataFrame(states_to_learn)
        not_guessed_states.to_csv("states_to_learn.csv")
        break

    if state in states_list:
        guessed_states.append(state)
        x = int(states_data[states_data.state == state].x)
        y = int(states_data[states_data.state == state].y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(state, font=('Arial', 8, 'bold'))



