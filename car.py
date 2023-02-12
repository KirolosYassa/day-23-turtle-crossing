from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    def __init__(self):
        super().__init__(shape="square")
        self.penup()
        self.shapesize(1.3, 2.5)
        self.setheading(to_angle=180)
        self.color(random.choice(COLORS))
        self.goto(x=300, y=random.randint(-300, 300))
        self.move_incremental = MOVE_INCREMENT
        # self.start()

        # while True:
        #     # dis = STARTING_MOVE_DISTANCE
        #     dis = STARTING_MOVE_DISTANCE + self.move_incremental
        #     self.forward(distance=dis)
        # self.forward(100)
        # self.goto(STARTING_MOVE_DISTANCE)

    def start(self):
        pass
