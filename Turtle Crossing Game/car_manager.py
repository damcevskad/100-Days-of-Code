from turtle import Turtle
import random

COLORS = ["brown4", "salmon4", "Slateblue4", "dark slate gray", "dark olive green", "DarkGoldenrod4", "MediumPurple4",
          "PeachPuff4", "maroon", "snow4"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()

    def generate_cars(self):
        chance = random.randint(1, 5)
        if chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            y = random.randrange(-250, 250)
            car.setposition(300, y)
            x = car.xcor() + 1
            y = car.ycor() + 1
            car.goto(x, y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        for car in self.all_cars:
            speed = STARTING_MOVE_DISTANCE
            speed += MOVE_INCREMENT
            car.forward(speed)
