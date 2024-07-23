from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

# set up screen
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# set up objects
paddle = Paddle()
ball = Ball()
score = Scoreboard()

# get player input
screen.listen()
screen.onkey(paddle.move_up, "w")
screen.onkey(paddle.move_down, "s")
screen.onkey(paddle.move_up, "W")
screen.onkey(paddle.move_down, "S")

screen.onkey(paddle.move_up2, "Up")
screen.onkey(paddle.move_down2, "Down")

screen.onkeypress(paddle.move_up, "w")
screen.onkeypress(paddle.move_down, "s")
screen.onkeypress(paddle.move_up, "W")
screen.onkeypress(paddle.move_down, "S")

screen.onkeypress(paddle.move_up2, "Up")
screen.onkeypress(paddle.move_down2, "Down")

# is game on?
game_is_on = True
while game_is_on:
    # move ball
    ball.ball_move()

    # detect collisions of ball
    # detect collision top and bottom
    if ball.ball.ycor() > 290 or ball.ball.ycor() < -290:
        ball.bounce_y()

    # detect collision with paddles
    if ball.ball.distance(paddle.ai_paddle) < 30 and ball.ball.xcor() > 360:
        ball.bounce_x()
        ball.x_move -= 0.1

    if ball.ball.distance(paddle.player_paddle) < 30 and ball.ball.xcor() < -360:
        ball.bounce_x()
        ball.x_move += 0.1

    # detect collision left and right
    if ball.ball.xcor() < -420:
        score.add_ai_score()
        score.update_scoreboard()
        ball.x_move = -2.5
        ball.center()

    if ball.ball.xcor() > 420:
        score.add_player_score()
        score.update_scoreboard()
        ball.x_move = 2.5
        ball.center()







screen.exitonclick()