from turtle import Turtle
from player import Player

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class SidePlayer(Player):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("pink")
        self.shield_direction = 0
