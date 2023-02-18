from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
MOVE_INCREMENT = 10


class Player(Turtle):

    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.setheading(to_angle=90)
        self.goto(STARTING_POSITION)
        self.speed_player = MOVE_DISTANCE

    def up(self):
        self.forward(self.speed_player)

    def next_round(self):
        self.speed_player += MOVE_INCREMENT
        self.goto(STARTING_POSITION)
