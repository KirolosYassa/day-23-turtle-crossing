from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.setheading(to_angle=90)
        self.goto(STARTING_POSITION)

    def up(self, move_distance=MOVE_DISTANCE):
        self.forward(move_distance)