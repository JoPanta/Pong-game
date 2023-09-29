from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.setposition(350, 0)
        self.showturtle()

    def move_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)


