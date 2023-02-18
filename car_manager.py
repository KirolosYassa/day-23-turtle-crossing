from turtle import Turtle
import random
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 6:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(1.3, 2.5)
            new_car.setheading(to_angle=180)
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
