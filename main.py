from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scorekeeper import Scoreboard, Hashmarks

# initial constants for players, goal boundary, walls

STARTING_X_ONE = 350
STARTING_X_TWO = -350

GOAL_LEFT = -390
GOAL_RIGHT = 390

UPPER_LIM = 300
LOWER_LIM = -300

# initialize screen

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("jope's wicked pong")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
hash = Hashmarks()


# initialize paddles

player_one = Paddle()
player_one.setx(STARTING_X_ONE)

player_two = Paddle()
player_two.setx(STARTING_X_TWO)

# initialize ball

pong_ball = Ball()

# paddle movement

screen.onkey(fun=player_one.move_up, key="Up")
screen.onkey(fun=player_one.move_back, key="Down")

screen.onkey(fun=player_two.move_up, key="w")
screen.onkey(fun=player_two.move_back, key="s")

game_on = True

while game_on:
    pong_ball.onward()
    screen.update()

    # detect collision with players

    if pong_ball.distance(player_one) < 30 and pong_ball.xcor() > 340:
        pong_ball.paddle_bounce()
        pong_ball.onward_plus()

    if pong_ball.distance(player_two) < 30 and pong_ball.xcor() < -340:
        pong_ball.paddle_bounce()
        pong_ball.onward_plus()

    # detect collision with walls

    if pong_ball.ycor() > UPPER_LIM:
        pong_ball.bounce()

    if pong_ball.ycor() < LOWER_LIM:
        pong_ball.bounce()

    # detect goal state

    if pong_ball.xcor() > GOAL_RIGHT:
        scoreboard.player_two_scores()
        pong_ball.refresh_self()

    if pong_ball.xcor() < GOAL_LEFT:
        scoreboard.player_scores()
        pong_ball.refresh_self()

    if scoreboard.player_score > 2 or scoreboard.player_two_score > 2:
        game_on = False




screen.exitonclick()
