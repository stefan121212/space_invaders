from turtle import Screen
from player import Player
from invaders import InvaderManager
from bullet import Bullet
from scoreboard import ScoreBoard
from collsion import is_collision
from scoreboard2 import ScoreBoard2
import time
# from playsound import playsound

# screen set up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.bgpic("assets/space_invaders_background.gif")
screen.tracer(0)

player = Player()
invader_manager = InvaderManager()
scoreboard = ScoreBoard()
scoreboard2 = ScoreBoard2()
bullet = Bullet(player)

screen.listen()
screen.onkeypress(player.left, "Left")
screen.onkeypress(player.right, "Right")
screen.onkeypress(bullet.fire_bullet, "space")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    invader_manager.create_invader()
    invader_manager.move_invader()
    if bullet.bullet_state == "fire":
        y = bullet.ycor()
        y += 20
        bullet.sety(y)
    if bullet.ycor() > 275:
        bullet.ht()
        bullet.clear()
        bullet.bullet_state = "ready"
    for invader in invader_manager.all_invaders:
        # destroying enemy ship if bullet hits them
        if is_collision(bullet, invader):
            # playsound("assets/Space Invaders_explosion.wav") Freezing game easily
            scoreboard2.increase_score()
            invader.goto(-1000, 1000)
            invader.ht()
            bullet.goto(1000, 1000)
            bullet.ht()
            bullet.bullet_state = "ready"
        # Game over if player collides with invader
        if is_collision(player, invader):
            scoreboard.game_over()
            game_is_on = False
        # Game over if invaders reach bottom
        if invader.ycor() < -300:
            scoreboard.game_over()
            game_is_on = False
    # mechanic for changing levels, adding more enemies and increasing speed of enemies
    if scoreboard2.score / 50 == scoreboard.level * (scoreboard.level + 1 ) / 2:
        invader_manager.level_up()
        scoreboard.increase_level()
screen.exitonclick()

















