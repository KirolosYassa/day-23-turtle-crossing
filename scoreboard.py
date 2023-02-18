from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-200, 250)
        self.display_level()

    def display_level(self):
        self.write(f"Level: {self.level}", True, align="center", font=FONT)

    def next_round(self):
        self.level += 1
        self.clear()
        self.goto(-200, 250)
        self.display_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", True, align="center", font=FONT)

    def winner(self):
        self.goto(0, 0)
        self.write("You Won!", True, align="center", font=FONT)
