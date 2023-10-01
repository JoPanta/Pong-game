from turtle import Turtle, Screen
from paddle1 import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

game_is_on = True
score_right = 0
score_left = 0

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    scoreboard.update_scoreboard()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 327 or ball.distance(left_paddle) < 50 and ball.xcor() < -327:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.refresh_position()
        scoreboard.left_player_score()
    if ball.xcor() < -380:
        ball.refresh_position()
        scoreboard.right_player_score()

screen.exitonclick()