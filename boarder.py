from turtle import Turtle
import random

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# we want this food class to inherit from turtle class
# ---------||||||
class Boarder(Turtle):

    def __init__(self, shape):
        super().__init__()  # need this to intialize from turtle class
        self.shape(shape)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.width(5)
        self.penup()
        self.hideturtle()

    def draw_boarder(self):
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0,300)
        self.pendown()
        self.setheading(RIGHT)
        self.forward(300)
        self.setheading(DOWN)
        self.forward(600)
        self.setheading(LEFT)
        self.forward(600)
        self.setheading(UP)
        self.forward(600)
        self.setheading(RIGHT)
        self.forward(600)


    def draw_finish_line(self):
        self.penup()
        self.color("cyan")
        self.speed("fastest")
        self.goto(-300,240)
        self.pendown()
        self.setheading(RIGHT)
        self.forward(600)

