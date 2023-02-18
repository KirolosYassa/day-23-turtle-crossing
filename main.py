import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SPEED = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.up)

game_is_on = True

while game_is_on:
    time.sleep(SPEED)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if player.distance(car) <= 20:
            game_is_on = False
            score.game_over()
            break

    if player.ycor() >= 290:
        player.next_round()
        car_manager.next_round()
        score.next_round()
        SPEED *= 0.9
        if score.level == 8:
            score.winner()
            game_is_on = False

screen.exitonclick()