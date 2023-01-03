from turtle import Screen
from turtle_player import Player
import time
from cars import Car
from score import Score

my_screen = Screen()
my_screen.setup(600,600)
my_screen.title("My turtle crossing road")
my_screen.tracer(0)

player = Player()
car = Car()
score = Score()
my_screen.listen()
my_screen.onkeypress(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()

    car.create_car()
    car.move_car()

    # detect collision
    for c in car.all_car:
        if c.distance(player) < 20:
            game_is_on = False
            my_screen.clear()
            score.game_over()
            score.show_score()

    # detect crossing
    if  player.finish_line() :
        player.goto_start()
        car.level_up()
        score.level_up()


my_screen.exitonclick()
