import turtle
from turtle import Turtle, Screen
import random
race_on = False
my_screen = Screen()
my_screen.setup(width=500, height= 400)
user_bet = my_screen.textinput(title='Make your bet', prompt="Which turtles will win the race?"
"(red, orange, yellow, green, blue, purple) \n Enter the color:")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_position = [-100, -50, 0, 50 , 100, 150]
turtle_list = []

for i in range(len(color)):
    turtles = Turtle(shape="turtle")
    turtles.color(color[i])
    turtles.penup()
    turtles.goto(x=-230, y=starting_position[i] )
    turtle_list.append(turtles)

if user_bet:
    race_on = True

while race_on:
    for turtles in turtle_list:
        if turtles.xcor() > 230:
            race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                turtle.clearscreen()
                turtle.hideturtle()
                turtle.color("Green")
                turtle.penup()
                turtle.write(f"You won bet. The {winning_color} turtle win the race.", move = True, align= 'center', font=("Arial", 10, "bold"))
                turtle.done()
            else:
                turtle.clearscreen()
                turtle.hideturtle()
                turtle.color("red")
                turtle.penup()
                turtle.write(f"You lose bet. The {winning_color} turtle win the race.", move = True, align= 'center', font=("Arial", 10, "bold"))
                turtle.done()
        distance = random.randint(0, 10)
        turtles.forward(distance)
my_screen.exitonclick()
