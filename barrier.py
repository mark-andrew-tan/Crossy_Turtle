from turtle import Turtle
import random


# we want this food class to inherit from turtle class
# ---------||||||
class Barrier(Turtle):

    def __init__(self):
        super().__init__()  # need this to intialize from turtle class
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)  # stretching by factor of half
        self.color("")
        self.speed("fastest")
        self.xpos = round((20 * random.randint(-14, 12)))
        self.ypos = round((20 * random.randint(-14, 12)))
        self.goto(self.xpos, self.ypos)

    def refresh(self):
        randx = random.randint(-240, 240)  # 300 - 20. Range accounting for food size and dimensions
        randy = random.randint(-240, 240)
        self.goto(randx, randy)

    def get_ypos(self):
        return self.ypos

