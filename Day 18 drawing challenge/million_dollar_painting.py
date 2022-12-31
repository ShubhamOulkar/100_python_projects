import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
import colorgram

color_from_image = colorgram.extract('Damien_Hirst_painting.jpg', 30)

rgb_colors = []
for color in color_from_image:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_colors.append(rgb)


#rgb_colors = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61)]

import random
painting = Turtle()
painting.speed('fastest')
painting.hideturtle()
painting.penup()
painting.setheading(180)
painting.forward(200)
painting.right(90)
painting.forward(250)
painting.right(90)
def drawdot(space, x):
    for i in range(x):
        for j in range(x):
           # painting.pensize(10)
            painting.dot(20, random.choice(rgb_colors))
            #painting.color(random.choice(rgb_colors))
            painting.forward(space)
        painting.backward(space * x)
        painting.right(90)
        painting.forward(space)
        painting.left(90)

drawdot(50, 10)

my_screen = Screen()
stop = my_screen.exitonclick()