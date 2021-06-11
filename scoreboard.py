from turtle import Turtle
import time

FONT = ("Comic-san", 18, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.color("white")

        self.update()

    def update(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.goto(0, 0)
        self.write(f"level: {self.level} incoming!!!", align="center", font=FONT)
        time.sleep(3)
        self.update()

    def game_over(self):
        self.goto(-70, 0)
        self.write("GAME OVER", font=FONT)