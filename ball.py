from turtle import Turtle

START_X = 0
START_Y = 0
WIDTH = 20
HEIGHT = 20
SHAPE = "circle"
COLOR = "white"
MOVEMENT = 2

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(START_X, START_Y)
        self.shape(SHAPE)
        self.color(COLOR)
        self.seth(65)
        self.y_move = MOVEMENT
        self.x_move = MOVEMENT

    def onward(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def refresh_self(self):
        self.ht()
        self.goto(START_X, START_Y)
        self.y_move = MOVEMENT
        self.x_move = MOVEMENT
        self.st()

    def onward_plus(self):
        self.x_move *= 1.1
        self.y_move *= 1.1



