import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from car import Car
from scoreboard import Scoreboard
from boarder import Boarder
from barrier import Barrier
from walls import Walls
from side_player import SidePlayer
from shield import Shield

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

NUM_WALLS = 30

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.tracer(0)

boarder = Boarder("square")
finish_line = Boarder("classic")
boarder.draw_boarder()
finish_line.draw_finish_line()
scoreboard = Scoreboard()

shield = Shield()
player = Player()

walls = Walls(NUM_WALLS)
barrier_positions = walls.get_all_barriers_ypos()
# print(barrier_positions)
car_manager = CarManager()

screen.listen()


# screen.onkey(player.go_up, "Up")
# screen.onkey(player.go_down, "Down")
# screen.onkey(player.go_left, "Left")
# screen.onkey(player.go_right, "Right")


# screen.onkey(shield.go_up_s, "w")
# screen.onkey(shield.go_down_s, "s")
# screen.onkey(shield.go_left_s, "d")
# screen.onkey(shield.go_right_s, "a")


def up_pls():
    player.go_up()
    if player.valid_up:
        shield.go_up_s()


def down_pls():
    player.go_down()
    if player.valid_down:
        shield.go_down_s()


def right_pls():
    player.go_right()
    if player.valid_right:
        shield.go_right_s()


def left_pls():
    player.go_left()
    if player.valid_left:
        shield.go_left_s()


screen.onkey(up_pls, "Up")
screen.onkey(down_pls, "Down")
screen.onkey(left_pls, "Left")
screen.onkey(right_pls, "Right")

spawn_rate = 10
counter = 0
game_is_on = True
while game_is_on:
    # generating cars // spawn_rate DOWN = HIGHER DIFFICULTY
    counter += 1
    time.sleep(0.1)
    screen.update()
    if counter % spawn_rate == 0:
        car_manager.create_car(barrier_positions)
    # car movement
    car_manager.move_cars()

    # removing cars out of bounds
    for car in car_manager.all_cars:
        print(f"Direction ({car.colorlabel}) {car.direction}:")
        if car.direction == LEFT and car.xcor() < -340:
            car.reset_car()
        elif car.direction == RIGHT and car.xcor() > 340:
            car.reset_car()

    # detect collision with car
    for car in car_manager.all_cars:
        if round(car.distance(player)) < 20:
            # scoreboard.player_lose()
            # scoreboard.update_scoreboard()
            player.crushed = True
            game_is_on = False

    # detect crossing finish line
    # print("player ycor:", player.ycor())
    if player.is_at_finish_line():
        print("AT FINISH LINE")
        scoreboard.increase_level()
        spawn_rate -= 2
        scoreboard.update_scoreboard()
        walls.reset_walls(NUM_WALLS)
        car_manager.reset_cars()
        shield.reset_shield_pos()
        player.go_to_start()

    scoreboard.decrement_time()
    scoreboard.update_scoreboard()
    if scoreboard.time_per_level <= 0:
        game_is_on = False
        player.time_out = True

    beside = False

    for barrier in walls.all_barriers:

        # NOTE FOR NEW DETECTION:
        # CHANGE ORDER OF SHIELD initialization.
        # Each shield piece acts as up, down, etc.
        # to determine valid up/down etc
        for side_shield in shield.all_side_players:

            if round(barrier.distance(side_shield)) < 20:
                # print("in first if dist: ", round(barrier.distance(side_shield)))
                beside = True
                if side_shield.shield_direction == UP:
                    player.valid_up = False
                    # print("NOT IN VAILD (UP)")
                elif side_shield.shield_direction == DOWN:
                    player.valid_down = False
                    # print("NOT IN VAILD (DOWN)")
                elif side_shield.shield_direction == RIGHT:
                    player.valid_right = False
                    # print("NOT IN VAILD (RIGHT)")
                elif side_shield.shield_direction == LEFT:
                    player.valid_left = False
                    # print("NOT IN VAILD (LEFT)")
            if not beside:  # allow any movement
                # print("outside if dist", round(barrier.distance(side_shield)))
                # print("NOT BESIDE ")
                player.valid_up = True
                player.valid_down = True
                player.valid_right = True
                player.valid_left = True
                # print("player valid_up:", player.valid_up)
    if spawn_rate < 0:
        game_is_on = False
        scoreboard.player_win()

if player.crushed:
    scoreboard.player_lose_crushed()
if player.time_out:
    scoreboard.player_lose_time()

screen.exitonclick()
