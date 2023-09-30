from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 220)

    def update_scoreboard(self):
        self.write(f"{self.score_left}   {self.score_right}", False, "center", ("Verdana", 50, "normal"))

    def left_player_score(self):
        self.score_left += 1
        self.clear()
        self.update_scoreboard()

    def right_player_score(self):
        self.score_right += 1
        self.clear()
        self.update_scoreboard()