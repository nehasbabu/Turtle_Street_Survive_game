import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
cars=CarManager()
score=Scoreboard()
screen.listen()
screen.onkey(player.mov,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.car()
    cars.movement()
    for cr in cars.care:
        if cr.distance(player)<30:
            game_is_on=False
            score.gme()
    if player.ycor() > 280:
        score.levelup()
        player.starting()
        cars.speedup()
screen.exitonclick()
