from turtle import Turtle

STARTING_X_P_1 = 350
STARTING_X_P_TWO = -350
STARTING_Y = 0
PADDLE_WID = 5.0
PADDLE_LEN = 1
PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"
PADDLE_MOV = 20
PADDLE_DIR = 90

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.seth(90)
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=PADDLE_LEN, stretch_len=PADDLE_WID)

    def move_up(self):
        self.forward(PADDLE_MOV)

    def move_back(self):
        self.back(PADDLE_MOV)