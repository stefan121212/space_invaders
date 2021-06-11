from turtle import Turtle
FONT = ("Comic-san", 18, "bold")


class ScoreBoard2(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(280, 260)
        self.color("white")

        self.update()

    def update(self):
        self.clear()
        self.write(f"score: {self.score}", align="right", font=FONT)

    def increase_score(self):
        self.score += 10
        self.update()
