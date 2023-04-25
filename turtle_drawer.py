import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()


def forwards():
    timmy.forward(10)


def backwards():
    timmy.backward(10)


def left():
    timmy.left(10)


def right():
    timmy.right(10)


def clear():
    timmy.setposition(0, 0)
    timmy.clear()
    timmy.setheading(0)


screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
