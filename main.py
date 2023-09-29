from turtle import Turtle, Screen
from paddle1 import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

right_paddel = Paddle()


screen.listen()
screen.onkeypress(right_paddel.move_up, "Up")
screen.onkeypress(right_paddel.move_down, "Down")






























screen.exitonclick()