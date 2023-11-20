from turtle import Turtle


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.start = self.snakes[0]

    def create_snake(self):
        x = 0
        for index in range(0, 3):
            snake = Turtle("square")
            snake.color("green")
            snake.penup()
            snake.goto(x, 0)
            x += 20
            self.snakes.append(snake)

    def move_snake(self):
        for s in range(len(self.snakes) - 1, 0, -1):
            x = self.snakes[s - 1].xcor()
            y = self.snakes[s - 1].ycor()

            self.snakes[s].goto(x, y)
        self.start.forward(20)

    def up(self):
        if self.start.heading() != 270:
            self.start.setheading(90)

    def down(self):
        if self.start.heading() != 90:
            self.start.setheading(270)

    def left(self):
        if self.start.heading() != 0:
            self.start.setheading(180)

    def right(self):
        if self.start.heading() != 180:
            self.start.setheading(0)

    def grow_snake(self):
        snake = Turtle("square")
        snake.color("green")
        snake.penup()
        x = self.snakes[-1].xcor()
        y = self.snakes[-1].ycor()
        snake.goto(x, y)
        self.snakes.append(snake)

    def reset(self):
        for s in self.snakes:
            s.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.start = self.snakes[0]


