from turtle import Turtle


class Hashmarks(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.ht()
        self.pensize(5)
        self.goto(0, -310)
        self.seth(90)
        self.pencolor("white")
        for x in range(200):
            self.fd(15)
            self.pd()
            self.fd(15)
            self.pu()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.goto(0, -310)
        self.pencolor("white")
        self.goto(x=0, y=220)
        self.player_score = 0
        self.player_two_score = 0
        self.write(arg=f"{self.player_two_score}            {self.player_score}", align="center",
                   font=("courier", 40, "normal"))

    def player_scores(self):
        self.player_score += 1
        self.write(arg=f"{self.player_two_score}            {self.player_score}", align="center",
                   font=("courier", 40, "normal"))

    def player_two_scores(self):
        self.clear()
        self.player_two_score += 1
        self.write(arg=f"{self.player_two_score}            {self.player_score}", align="center",
                   font=("courier", 40, "normal"))
