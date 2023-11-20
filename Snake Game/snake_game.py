from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

playing = True
while playing:
    screen.update()
    time.sleep(0.1)
    screen.listen()

    snake.move_snake()
    if snake.start.distance(food) < 15:
        food.hideturtle()
        food.new_food()
        food.showturtle()
        snake.grow_snake()
        score.score += 1
        score.show_score()

    if snake.start.xcor() > 280 or snake.start.ycor() > 280 or snake.start.xcor() < -280 or snake.start.ycor() < -280:
        score.reset()
        score.show_score()
        snake.reset()

    for s in snake.snakes[1:-1]:
        if snake.start.distance(s) < 10:
            score.reset()
            score.show_score()
            snake.reset()

    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

