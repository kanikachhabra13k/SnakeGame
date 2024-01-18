from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score1 = int (data.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def game_over(self):
        self.hideturtle()
        self.goto(0,0)
        self.write("Game Over. You lost:(", align="center", font=("Arial", 24, "normal"))

    def high_score(self):
        if self.score > self.high_score1:
            self.high_score1 = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.high_score1}")
        self.score = 0
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"SCOREBOARD: {self.score}  HIGH SCORE: {self.high_score1}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()