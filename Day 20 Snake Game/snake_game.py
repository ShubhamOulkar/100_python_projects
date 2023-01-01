from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width= 600, height=600)
my_screen.bgcolor('black')
my_screen.title("Snake Game")

starting_positions = [(0,0),(-20,0),(-40,0)]

for position in starting_positions:
    snake = Turtle('square')
    snake.color("white")
    snake.goto(position)







my_screen.exitonclick()