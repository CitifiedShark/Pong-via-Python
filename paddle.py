from turtle import Turtle
PLAYER_STARTING_X = -380
AI_STARTING_X = 380
CENTER_STARTING_Y = 600

class Paddle():

    def __init__(self):
        super().__init__()

        self.player_paddle = Turtle(shape="square")
        self.player_paddle.penup()
        self.player_paddle.shapesize(stretch_wid=2, stretch_len=0.1)
        self.player_paddle.teleport(PLAYER_STARTING_X, 0)
        self.player_paddle.color("white")

        self.ai_paddle = Turtle(shape="square")
        self.ai_paddle.penup()
        self.ai_paddle.shapesize(stretch_wid=2, stretch_len=0.1)
        self.ai_paddle.teleport(AI_STARTING_X, 0)
        self.ai_paddle.color("white")

        self.center = Turtle(shape="square")
        self.center.teleport(0, CENTER_STARTING_Y)
        self.center.pencolor("white")
        for lines in range(12):
            self.center.penup()
            self.center.goto(0, CENTER_STARTING_Y - (lines * 100))
            self.center.pendown()
            self.center.goto(0, CENTER_STARTING_Y - (lines * 100) - 100)


    def move_up(self):
        if self.player_paddle.ycor() < 290:
            self.player_paddle.teleport(self.player_paddle.xcor(), self.player_paddle.ycor() + 20)

    def move_down(self):
        if self.player_paddle.ycor() > -290:
            self.player_paddle.teleport(self.player_paddle.xcor(), self.player_paddle.ycor() - 20)

    def move_up2(self):
        if self.ai_paddle.ycor() < 290:
            self.ai_paddle.teleport(self.ai_paddle.xcor(), self.ai_paddle.ycor() + 20)

    def move_down2(self):
        if self.ai_paddle.ycor() > -290:
            self.ai_paddle.teleport(self.ai_paddle.xcor(), self.ai_paddle.ycor() - 20)

