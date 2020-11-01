import turtle
import tkinter
import random
import math
import time

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("RPG Battle")
wn.setup(width = 700, height = 700)
wn.tracer(10)

icons = ["Player.gif", "Chimera.gif"]
for icon in icons:
    turtle.register_shape(icon)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        #self.shape("circle")
        self.color("black")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.name = "Ace"
        self.shape("Player.gif")
        self.penup()
        self.speed(0)
        self.health = 1000
        self.magic = 100
        self.limit = 0
        self.goto(x, y)

    def use_attack(self):
        if not cannot_attack:
            damage = random.randrange(100, 150)
            message.clear()
            message.write("{} attacks! {} takes {} damage!".format(self.name, enemy.name, damage), align = "center", font = ("Arial", 24, "normal"))
            enemy.health -= damage
            enemy.limit += random.randrange(5, 10)
            enemy_health.clear()
            enemy_health.write("{}'s Health: {}".format(enemy.name, enemy.health), font = ("Arial", 12, "normal"))
            enemy_limit.clear()
            enemy_limit.write("{}'s Limit: {}".format(enemy.name, enemy.limit), font = ("Arial", 12, "normal"))

    def use_magic_1(self):
        if not cannot_attack and self.magic > 0:
            magic = "Heal"
            heal = random.randrange(20, 40)
            message.clear()
            message.write("{} uses {}! {} restores {} HP!".format(self.name, magic, self.name, heal), align = "center", font = ("Arial", 24, "normal"))
            self.health += heal
            self.magic -= 10
            player_health.clear()
            player_health.write("Player Health: {}".format(self.health), font = ("Arial", 12, "normal"))
            player_magic.clear()
            player_magic.write("Player Mana: {}".format(self.magic), font = ("Arial", 12, "normal"))
        elif self.magic <= 0:
            message.clear()
            message.write("Out of Mana!", align = "center", font = ("Arial", 24, "normal"))

        
    def use_magic_2(self):
        if not cannot_attack and self.magic > 0:
            magic = "Fire"
            damage = random.randrange(150, 300)
            message.clear()
            message.write("{} uses {}! {} takes {} damage!".format(self.name, magic, enemy.name, damage), align = "center", font = ("Arial", 24, "normal"))
            enemy.health -= damage
            enemy.limit += random.randrange(10, 15)
            self.magic -= 5
            player_magic.clear()
            player_magic.write("Player Mana: {}".format(self.magic), font = ("Arial", 12, "normal"))
            enemy_health.clear()
            enemy_health.write("{}'s Health: {}".format(enemy.name, enemy.health), font = ("Arial", 12, "normal"))
            enemy_limit.clear()
            enemy_limit.write("{}'s Limit: {}".format(enemy.name, enemy.limit), font = ("Arial", 12, "normal"))
        elif self.magic <= 0:
            message.clear()
            message.write("Out of Mana!", align = "center", font = ("Arial", 24, "normal"))

    def use_limit(self):
        if not cannot_attack and self.limit >= 100:
            damage = random.randrange(900, 1000)
            message.clear()
            message.write("{}'s limit break, Sun Strike! {} takes {} damage!".format(self.name, enemy.name, damage), align = "center", font = ("Arial", 24, "normal"))
            enemy.health -= damage
            enemy.limit += 30
            self.limit = 0
            enemy_health.clear()
            enemy_health.write("{}'s Health: {}".format(enemy.name, enemy.health), font = ("Arial", 12, "normal"))
            enemy_limit.clear()
            enemy_limit.write("{}'s Limit: {}".format(enemy.name, enemy.limit), font = ("Arial", 12, "normal"))
            player_limit.clear()
            player_limit.write("Limit: {}".format(player.limit), font = ("Arial", 12, "normal"))
            
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.name = "Chimera"
        self.shape("Chimera.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.health = 10000
        self.limit = 0

    def regular_attack(self):
        if enemy_turn:
            damage = random.randrange(5, 10)
            message.clear()
            message.write("The {} attacks! {} takes {} damage!".format(self.name, player.name, damage), align = "center", font = ("Arial", 24, "normal"))
            player.health -= damage
            player.limit += damage
            player_health.clear()
            player_health.write("Player Health: {}".format(player.health), font = ("Arial", 12, "normal"))
            player_magic.clear()
            player_magic.write("Player Mana: {}".format(player.magic), font = ("Arial", 12, "normal"))
            player_limit.clear()
            player_limit.write("Limit: {}".format(player.limit), font = ("Arial", 12, "normal"))

    def strong_attack(self):
        if enemy_turn and self.limit >= 100:
            damage = random.randrange(40, 60)
            message.clear()
            message.write("{}'s powerful attack! {} takes {} damage!".format(self.name, player.name, damage), align = "center", font = ("Arial", 24, "normal"))
            player.health -= damage
            player.limit += random.randrange(damage // 2)
            self.limit = 0
            player_health.clear()
            player_health.write("Player Health: {}".format(player.health), font = ("Arial", 12, "normal"))
            player_magic.clear()
            player_magic.write("Player Mana: {}".format(player.magic), font = ("Arial", 12, "normal"))
            player_limit.clear()
            player_limit.write("Limit: {}".format(player.limit), font = ("Arial", 12, "normal"))
            enemy_limit.clear()
            enemy_limit.write("{}'s Limit: {}".format(enemy.name, enemy.limit), font = ("Arial", 12, "normal"))

    def defeated(self):
        self.hideturtle()

player = Player(-200, 0)
enemy = Enemy(200, 0)
cannot_attack = False
has_not_attacked = True
enemy_turn = False
time_passed_player = 0
time_passed_enemy = 0

player_health = Pen()
player_health.hideturtle()
player_health.goto(-300, 200)
player_health.write("Player Health: {}".format(player.health), font = ("Arial", 12, "normal"))

player_magic = Pen()
player_magic.hideturtle()
player_magic.goto(-300, 150)
player_magic.write("Player Mana: {}".format(player.magic), font = ("Arial", 12, "normal"))

player_limit = Pen()
player_limit.hideturtle()
player_limit.goto(-300, 100)
player_limit.write("Limit: {}".format(player.limit), font = ("Arial", 12, "normal"))

enemy_health = Pen()
enemy_health.hideturtle()
enemy_health.goto(100, 200)
enemy_health.write("{}'s Health: {}".format(enemy.name, enemy.health), font = ("Arial", 12, "normal"))

enemy_limit = Pen()
enemy_limit.hideturtle()
enemy_limit.goto(100, 100)
enemy_limit.write("{}'s Limit: {}".format(enemy.name, enemy.limit), font = ("Arial", 12, "normal"))

message = Pen()
message.hideturtle()
message.goto(0, -100)
message.write("A wild {} attacks!".format(enemy.name), align = "center", font = ("Arial", 24, "normal"))

options = Pen()
options.hideturtle()
options.goto(0, -200)
options.write("What will {} do?\n1. Attack\t2. Heal\n3. Fire\t4. Limit".format(player.name), align = "center", font = ("Arial", 24, "normal"))

turtle.listen()
turtle.onkeypress(player.use_attack, "1")
turtle.onkeypress(player.use_magic_1, "2")
turtle.onkeypress(player.use_magic_2, "3")
turtle.onkeypress(player.use_limit, "4")

game_loop = True
while game_loop:

    if time_passed_enemy < 400:
        time_passed_enemy += 1
    else:
        enemy_turn = True
        time_passed_enemy = 0

##    if time_passed_player < 400 and not has_not_attacked:
##        cannot_attack = True
##        time_passed_player += 1
##
##    elif time_passed_player > 400 and has_not_attacked:
##        cannot_attack = False
##        time_passed_player += 1
##
##    else:
##        cannot_attack = True
##        time_passed_player = 0

    if enemy.limit > 100:
        enemy.limit = 100
        enemy_limit.clear()
        enemy_limit.write("{}'s Limit: {}".format(enemy.name, enemy.limit), font = ("Arial", 12, "normal"))

    if player.limit > 100:
        player.limit = 100
        player_limit.clear()
        player_limit.write("Limit: {}".format(player.limit), font = ("Arial", 12, "normal"))


    if not enemy_turn:
        options.clear()
        options.write("What will {} do?\n1. Attack\t2. Heal\n3. Fire\t4. Limit".format(player.name), align = "center", font = ("Arial", 24, "normal"))
                        
    else:
        if enemy.limit < 100:
            enemy.regular_attack()
        else:
            enemy.strong_attack()
        enemy_turn = False
    
    if player.health <= 0:
        player.health = 0
        message.clear()
        message.write("Game Over!", align = "center", font = ("Arial", 24, "normal"))
        options.clear()
        player_health.clear()
        player_health.write("Player Health: {}".format(player.health), font = ("Arial", 12, "normal"))
        game_loop = False
        
    if enemy.health <= 0:
        enemy.health = 0
        enemy.defeated()
        message.clear()
        message.write("You Win!", align = "center", font = ("Arial", 24, "normal"))
        options.clear()
        enemy_health.clear()
        enemy_health.write("{}'s Health: {}".format(enemy.name, enemy.health), font = ("Arial", 12, "normal"))
        game_loop = False

    wn.update()

turtle.onkeypress(None, "1")
turtle.onkeypress(None, "2")
turtle.onkeypress(None, "3")
turtle.onkeypress(None, "4")
turtle.done()



    
