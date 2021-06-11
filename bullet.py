from turtle import Turtle
# from playsound import playsound
BULLET_SPEED = 20


class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(0.3, 0.8)
        self.ht()
        self.player = player
        self.bullet_state = "ready"

    def fire_bullet(self):
        if self.bullet_state == "ready":
            # playsound("assets/Space Invaders_laser.wav") this way of playing audio file causes major screen freeze
            self.bullet_state = "fire"
            # Move the bullet to the just above the player
            x = self.player.xcor()
            y = self.player.ycor() + 10
            self.setposition(x, y)
            self.showturtle()