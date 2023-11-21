import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Score

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Score()
cars = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move_turtle)

playing = True
while playing:
    time.sleep(0.1)
    screen.update()

    cars.generate_cars()
    cars.move_cars()

    if player.finish_line():
        score.show_level()
        player.restart()
        cars.increase_speed()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.game_end()
            playing = False

screen.exitonclick()
