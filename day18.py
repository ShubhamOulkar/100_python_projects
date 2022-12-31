from turtle import Turtle, Screen

# square_turtle = Turtle()
# square_turtle.shape("square")
# square_turtle.shapesize(100,100)

tur = Turtle()


# def drawdot(space, x):
#     for i in range(x):
#         for j in range(x):
#             tur.dot()
#             tur.forward(space)
#         tur.backward(space * x)
#         tur.right(90)
#         tur.forward(space)
#         tur.left(90)
# 
# 
# tur.penup()
# drawdot(10, 8)
# 
# tur.hideturtle()


# for _ in range(15):
#     tur.pencolor("black")
#     tur.pensize(1)
#     tur.forward(5)
#     tur.penup()
#     tur.forward(5)
#     tur.pendown()

# challenge
import random
challenge = Turtle()
color_choice = ['magenta', 'red', 'black', 'blue','green','brown', 'pink', 'yellow']
for i in range(3, 11):
    angle = 360/i
    challenge.color(random.choice(color_choice))
    for _ in range(i):
        challenge.shape()
        challenge.forward(100)
        challenge.right(angle)


















my_screen = Screen()
my_screen.exitonclick()