from turtle import Turtle

class Scoreboard():

    def __init__(self):
        self.player_score_value = 0

        self.ai_score_value = 0

        self.player_score = Turtle()
        self.player_score.hideturtle()
        self.player_score.color("white")
        self.player_score.penup()
        self.player_score.goto(-200, 250)
        self.player_score.write(f"{self.player_score_value}", True, "center", font=('Courier', 30, 'normal'))

        self.ai_score = Turtle()
        self.ai_score.hideturtle()
        self.ai_score.color("white")
        self.ai_score.penup()
        self.ai_score.goto(200, 250)
        self.ai_score.write(f"{self.player_score_value}", True, "center", font=('Courier', 30, 'normal'))

    def update_scoreboard(self):
        self.ai_score.clear()
        self.player_score.clear()

        self.player_score.color("white")
        self.player_score.penup()
        self.player_score.goto(-200, 250)
        self.player_score.write(f"{self.player_score_value}", True, "center", font=('Courier', 30, 'normal'))

        self.ai_score.color("white")
        self.ai_score.penup()
        self.ai_score.goto(200, 250)
        self.ai_score.write(f"{self.ai_score_value}", True, "center", font=('Courier', 30, 'normal'))

    def add_player_score(self):
        self.player_score_value += 1

    def add_ai_score(self):
        self.ai_score_value += 1
