import turtle
from turtle import Turtle
from player import Player
from side_player import SidePlayer

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
NUMSHIELDS = 4

# side_player1 = SidePlayer(0,-260)
# side_player2 = SidePlayer(0,-300)
# side_player3 = SidePlayer(-20,-280)
# side_player4 = SidePlayer(20,-280)
# COLORS = ["red", "orange", "yellow", "pink"]

X_START_POS = [0, 20, 0, -20]
Y_START_POS = [-260, -280, -300, -280]


class Shield(SidePlayer):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.all_side_players = []  # holds Barrier objects
        self.starting_shield_positions = [UP, RIGHT, DOWN, LEFT]
        self.create_side_players(NUMSHIELDS)
        # self.all_barriers_ypos = []
        # self.initialize_all_barriers_ypos()

    def reset_shield_pos(self):
        i = 0
        for side_player in self.all_side_players:
            side_player.goto(X_START_POS[i], Y_START_POS[i])
            i += 1

    def create_side_players(self, amount):
        for i in range(0, amount):
            new_side_player = SidePlayer()
            new_side_player.color("pink")
            new_side_player.hideturtle()
            new_side_player.shape("square")
            new_side_player.shield_direction = self.starting_shield_positions[i]
            new_side_player.goto(X_START_POS[i], Y_START_POS[i])
            self.all_side_players.append(new_side_player)

    def go_up_s(self):
        for side_player in self.all_side_players:
            side_player.setheading(UP)
            side_player.forward(MOVE_DISTANCE)

    def go_down_s(self):
        for side_player in self.all_side_players:
            side_player.setheading(DOWN)
            side_player.forward(MOVE_DISTANCE)

    def go_left_s(self):
        for side_player in self.all_side_players:
            side_player.setheading(LEFT)
            side_player.forward(MOVE_DISTANCE)

    def go_right_s(self):
        for side_player in self.all_side_players:
            side_player.setheading(RIGHT)
            side_player.forward(MOVE_DISTANCE)
