from turtle import Turtle
from barrier import Barrier
import random


class Walls(Barrier):
    def __init__(self, num_walls):
        super().__init__()  # need this to intialize from turtle class

        self.all_barriers = []  # holds Barrier objects
        self.create_walls(num_walls)
        self.all_barriers_ypos = []
        self.initialize_all_barriers_ypos()

    def create_walls(self, num_walls):
        for i in range(1, num_walls):
            new_barrier = Barrier()
            new_barrier.color("green")
            self.all_barriers.append(new_barrier)

    def clear_walls(self):
        print("REMOVING WALLS")
        for remaining_walls in self.all_barriers:
            remaining_walls.reset()
        self.all_barriers_ypos.clear()
        print("Cleared walls list:", self.all_barriers_ypos)



    def reset_walls(self, num_walls):
        self.clear_walls()

        self.all_barriers.clear()
        self.all_barriers_ypos.clear()
        self.create_walls(num_walls)
        self.initialize_all_barriers_ypos()

    def initialize_all_barriers_ypos(self):
        for barrier in self.all_barriers:
            self.all_barriers_ypos.append(barrier.ypos)

    def get_all_barriers_ypos(self):
        return self.all_barriers_ypos


