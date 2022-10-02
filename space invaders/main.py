import random
import winsound
from turtle import Turtle, Screen

# Setting up the screen and its functionality.
screen = Screen()
screen.bgpic("background.gif")
screen.title("SPACE INVADERS")
screen.setup(width=1.0, height=1.0)
screen.tracer(0)

player_image = "player.gif"
screen.register_shape(player_image)
screen.register_shape("space-invaders.gif")


# Creating the scoreboard and all its functionality.
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 330)
        self.write(self.score, align="center", font=("Courier", 20, "normal"))

    def scored(self):
        self.score += 3
        self.update_scoreboard()


# Creating the player
class PlayerManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("player.gif")
        self.penup()
        self.goto(0, -260)
        self.speed("fastest")

    def get_position(self):
        return self.pos()

    def go_left(self):
        self.setheading(0)
        self.forward(30)
        screen.update()

    def go_right(self):
        self.setheading(180)
        self.forward(30)
        screen.update()


# creating the list of enemies, creating them and setting them to their positions.
enemies = []


class EnemyManager:

    def __init__(self):
        self.each_enemy = None
        self.pack_enemies()
        self.x_move = 1

    def pack_enemies(self):
        for x_position in range(0, 680, 120):
            for y_position in range(120, 300, 120):
                self.enemy = Turtle()
                self.enemy.shape("space-invaders.gif")
                self.enemy.penup()
                self.enemy.shapesize(stretch_wid=1, stretch_len=5)
                self.enemy.goto(x_position, y_position)
                self.enemy.speed("fastest")
                enemies.append(self.enemy)

    def move_enemies(self):
        screen.update()
        for self.each_enemy in enemies:
            new_x = self.each_enemy.xcor() - self.x_move
            new_y = self.each_enemy.ycor()
            self.each_enemy.goto(new_x, new_y)
            if self.each_enemy.xcor() < -680:
                self.x_move += -2
            if self.each_enemy.xcor() > 680:
                self.x_move -= -2


# This is the bullet manager of the player, responsible for the shoot.
class BulletManager(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("triangle")
        self.color("yellow")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=1.3, stretch_wid=0.3)
        self.hideturtle()

    def move_bullet(self):
        global bullet_condition
        if bullet_condition == "ready_fire":
            bullet_condition = "fire"
            winsound.PlaySound('sound/player_shoot.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

            global player
            self.setpos(player.get_position()[0], player.get_position()[1])

            self.showturtle()


# Manages the bullets of the enemies.
class EnemyBullet(Turtle):

    def __init__(self):

        super().__init__()
        self.shape("triangle")
        self.color("red")
        self.penup()
        self.setheading(270)
        self.shapesize(stretch_len=1.3, stretch_wid=0.3)
        self.hideturtle()

    def move_bullet(self):
        global i_condition
        if i_condition == "ready_fire":
            i_condition = "fire"

            e = random.choice(enemies)
            self.setpos(e.pos()[0], e.pos()[1])

            self.showturtle()


# Creating the objects of each class and initialising.
score_board = Scoreboard()
enemy_object = EnemyManager()
player = PlayerManager()
bullet = BulletManager()

bullet_condition = "ready_fire"
i_condition = "ready_fire"
mb = EnemyBullet()

screen.listen()
screen.onkeypress(player.go_left, "Right")
screen.onkeypress(player.go_right, "Left")
screen.onkeypress(bullet.move_bullet, "space")

# Getting the game to run.
game_is_on = True
while game_is_on:
    screen.update()
    enemy_object.move_enemies()
    mb.move_bullet()
    if i_condition == "fire":
        new_y = mb.ycor()
        new_y -= 3
        mb.sety(new_y)

    if mb.ycor() < -250:
        mb.hideturtle()
        i_condition = "ready_fire"

    if bullet_condition == "fire":
        new_y = bullet.ycor()
        new_y += 2
        bullet.sety(new_y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_condition = "ready_fire"

    # If an enemy is shot
    for any_enemy in enemies:
        if bullet.distance(any_enemy) < 30:
            winsound.PlaySound('sound/villain_shoot.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            any_enemy.hideturtle()
            score_board.scored()
            score_board.update_scoreboard()
            enemies.remove(any_enemy)

    if player.distance(mb) < 30:
        winsound.PlaySound('sound/player_killed.wav', winsound.SND_ASYNC | winsound.SND_FILENAME )
        player.hideturtle()

screen.exitonclick()
