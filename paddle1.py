from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.setposition(xcor, ycor)

    def move_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)


