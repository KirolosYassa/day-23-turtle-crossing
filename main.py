import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.up)


# def create_car():
#     return car


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # screen.tracer(100, 10)
    # dist = 2
    car = CarManager()
    for i in range(10):
        car.fd(car.dis)
        # rt(90)
        # dist += 2
    time.sleep(random.randint(0, 2))
    # car.forward(car_manager.dis)

screen.exitonclick()