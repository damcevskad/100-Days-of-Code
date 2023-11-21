from turtle import Screen
from players import Players
from scoreboard import Score
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

left_player = Players(-350, 0)
right_player = Players(350, 0)
scoreboard = Score()
ball = Ball()

screen.listen()
screen.onkey(key="Up", fun=right_player.up)
screen.onkey(key="Down", fun=right_player.down)
screen.onkey(key="w", fun=left_player.up)
screen.onkey(key="s", fun=left_player.down)

playing = True
while playing:
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_player) < 50 and ball.xcor() > 320 or ball.distance(left_player) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restart()
        ball.bounce_x()
        scoreboard.left_score += 1
        scoreboard.show_score()

    if ball.xcor() < -380:
        ball.restart()
        ball.bounce_x()
        scoreboard.right_score += 1
        scoreboard.show_score()

    if scoreboard.right_score == 30 or scoreboard.left_score == 30:
        scoreboard.game_over()
        playing = False

screen.exitonclick()
