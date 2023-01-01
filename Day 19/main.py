import turtle
from turtle import Turtle, Screen

sketch = Turtle()

def forward():
    sketch.forward(10)

def backward():
    sketch.backward(10)

def counter_clockwise():
    sketch.left(10)

def clockwise():
    sketch.right(10)

def clear():
    sketch.clear()
    sketch.penup()
    sketch.home()
    sketch.pendown()

turtle.onkey(key='w', fun= forward)
turtle.onkey(key='s', fun= backward)
turtle.onkey(key='a', fun= counter_clockwise)
turtle.onkey(key='d', fun= clockwise)
turtle.onkey(key='c', fun= clear)
turtle.listen()


my_screen = Screen()
my_screen.exitonclick()