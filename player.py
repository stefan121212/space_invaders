from turtle import register_shape, Turtle

MOVE_DISTANCE = 10
register_shape("assets/player.gif")
bulletstate = "ready"

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("assets/player.gif")
        self.penup()
        self.goto(0, -270)
        self.color("white")
        self.setheading(90)


    def right(self):
        if self.xcor() < 280:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def left(self):
        if self.xcor() > -280:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())

