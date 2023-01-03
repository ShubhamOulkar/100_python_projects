from turtle import Turtle

class Ball(Turtle):

    def  __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.shapesize(1.5)
        self.sleep_time = 0.1
        self.x_move = 10
        self.y_move = 10

    def  move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() +self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1
        self.sleep_time *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.sleep_time *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()
        self.sleep_time = 0.1

