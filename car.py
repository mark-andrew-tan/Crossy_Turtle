from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "pink", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POS_X = -340
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Car(Turtle):
    def __init__(self):
        super().__init__()  # need this to intialize from turtle class
        self.shape("square")
        self.speed = random.randint(5, 20)  # change left bound depending on level
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.colorlabel = random.choice(COLORS)
        self.color(self.colorlabel)

        self.direction = 0  # default is right

    def reset_car(self):
        # print("in reset car def")
        self.reset()
