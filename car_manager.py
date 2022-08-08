from turtle import Turtle
from car import Car
import random

COLORS = ["red", "orange", "yellow", "pink", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POS_X = -340
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class CarManager(Car):
    def __init__(self):
        super().__init__()  # need this to intialize from turtle class
        # self.test = barrier_ypos
        self.all_cars = []  # holds CAR objects
        self.hideturtle()

    def create_car(self, barrier_ypos):
        new_car = Car()
        # need to initialize the invalid_ypos
        not_valid_position = True
        random_y = 0

        while not_valid_position:
            random_y = (20 * random.randint(-12, 12))  # RANGE: -240:240 STEP = 20
            # print("random_y: ", random_y)
            for barrier in barrier_ypos:
                # print("barrier ycor: ",barrier)
                if barrier != random_y:
                    not_valid_position = False  # is a valid position
                else:
                    # print("-- barrier hit")
                    not_valid_position = True
                    break

        # print(random_y)
        new_car.direction = RIGHT  # initial starting pos = LEFT
        start_on_right = False
        x_pos = STARTING_POS_X
        if random.randint(0, 1) == 0:
            start_on_right = True
        if start_on_right:
            x_pos *= -1
            new_car.direction = LEFT

        new_car.goto(x_pos, random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.setheading(car.direction)
            car.forward(car.speed)

    def reset_cars(self):
        for remaining_cars in self.all_cars:
            remaining_cars.reset()


