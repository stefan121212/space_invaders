from turtle import register_shape, Turtle
import random

STARTING_MOVING_SPEED = 3
MOVING_INCREMENT = 1
STARTING_LEVEL_DIFF = 5
register_shape("assets/invader.gif")


class InvaderManager():
    def __init__(self):
        self.all_invaders = []
        self.invader_speed = STARTING_MOVING_SPEED
        self.starting_spawn = STARTING_LEVEL_DIFF

    def create_invader(self):
        if len(self.all_invaders) < self.starting_spawn:
            new_invader = Turtle("assets/invader.gif")
            new_invader.penup()
            random_x = random.randint(-270, 270)
            random_y = random.randint(350, 650)
            new_invader.goto(random_x, random_y)
            self.all_invaders.append(new_invader)

    def move_invader(self):
        for enemy in self.all_invaders:
            if enemy.ycor() < -300:
                enemy.ht()
            else:
                enemy.setheading(90)
                enemy.backward(self.invader_speed)

    def level_up(self):
        self.all_invaders.clear()
        self.invader_speed += MOVING_INCREMENT
        self.starting_spawn += STARTING_LEVEL_DIFF

