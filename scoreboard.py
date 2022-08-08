from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # need this to intialize from turtle class
        self.level = 1
        self.time_per_level = 200
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 320)
        self.write(f"Level: {self.level}     Time left: {self.time_per_level}", align=ALIGN, font=FONT)

    def increase_level(self):
        self.level += 1
        self.time_per_level = 200 + self.level*10

    def decrement_time(self):
        self.time_per_level -= 1

    def player_win(self):
        self.clear()
        self.goto(0, 0)
        self.write("-- SURVIVED --", align=ALIGN, font=FONT)

    def player_lose_crushed(self):
        self.clear()
        self.goto(0, 0)
        self.write("-- CRUSHED --", align=ALIGN, font=FONT)

    def player_lose_time(self):
        self.clear()
        self.goto(0, 0)
        self.write("-- TIME OUT --", align=ALIGN, font=FONT)

