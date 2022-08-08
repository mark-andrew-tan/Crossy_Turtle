from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 240
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.position = self.pos()
        self.position_x = self.position[0]
        self.position_y = self.position[1]
        self.valid_up = True
        self.valid_down = True
        self.valid_right = True
        self.valid_left = True
        self.time_out = False
        self.crushed = False

    def go_up(self):
        if self.valid_up:
            self.setheading(UP)
            self.forward(MOVE_DISTANCE)

    def go_down(self):
        if self.valid_down:
            self.setheading(DOWN)
            self.forward(MOVE_DISTANCE)

    def go_left(self):
        if self.valid_left:
            self.setheading(LEFT)
            self.forward(MOVE_DISTANCE)

    def go_right(self):
        if self.valid_right:
            self.setheading(RIGHT)
            self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if round(self.ycor()) >= FINISH_LINE_Y:
            return True
        else:
            return False
