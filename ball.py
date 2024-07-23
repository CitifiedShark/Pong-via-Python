from turtle import Turtle

class Ball():

    def __init__(self):
        super().__init__()

        self.ball = Turtle(shape="circle")
        self.ball.penup()
        self.ball.color("orange")
        self.x_move = 2.5
        self.y_move = 2.5

    def ball_move(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def center(self):
        self.ball.teleport(0, 0)
        self.bounce_x()
