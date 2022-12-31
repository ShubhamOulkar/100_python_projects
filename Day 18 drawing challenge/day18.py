import turtle
from turtle import Turtle, Screen

# square_turtle = Turtle()
# square_turtle.shape("square")
# square_turtle.shapesize(100,100)

# tur = Turtle()
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

# # challenge 1
# import random
# challenge = Turtle()
# color_choice = ['magenta', 'red', 'black', 'blue','green','brown', 'pink', 'yellow']
# for i in range(3, 11):
#     angle = 360/i
#     challenge.color(random.choice(color_choice))
#     for _ in range(i):
#         challenge.shape()
#         challenge.forward(100)
#         challenge.right(angle)



# # challenge 2
# import random
# random_path =Turtle()
# color_choice = ['magenta', 'red', 'black', 'blue','green','brown', 'pink', 'yellow']
# stop = True
# for i in range(100):
#     random_path.speed('fastest')
#     direction_choice = random.randint(1,4)
#     if direction_choice == 1 :
#         random_path.shape()
#         random_path.pensize(6)
#         random_path.setheading(0)
#         random_path.color(random.choice(color_choice))
#         random_path.forward(20)
#     elif direction_choice == 2:
#         random_path.shape()
#         random_path.pensize(6)
#         random_path.setheading(90)
#         random_path.color(random.choice(color_choice))
#         random_path.forward(20)
#     elif direction_choice == 3:
#         random_path.shape()
#         random_path.pensize(6)
#         random_path.setheading(180)
#         random_path.color(random.choice(color_choice))
#         random_path.forward(20)
#     else:
#         random_path.shape()
#         random_path.pensize(6)
#         random_path.setheading(270)
#         random_path.color(random.choice(color_choice))
#         random_path.forward(20)


# # Make Spirograph
# import random
# spirograph = Turtle()
# spirograph.speed("fastest")
# turtle.colormode(255)
#
# def rgb_color():
#     global rgb
#     rgb = ()
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     rgb = (r, g, b)
#     return rgb
#
# for i in range(100):
#     spirograph.circle(100)
#     spirograph.color(rgb_color())
#     position = spirograph.heading()
#     spirograph.setheading(position + i)

my_screen = Screen()
stop = my_screen.exitonclick()













