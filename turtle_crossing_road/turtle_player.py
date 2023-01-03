from turtle import  Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move_up(self):
        self.forward(10)

    def finish_line(self):
        if self.ycor() >= 280:
            return True
        else:
            return False
    def goto_start(self):
        self.goto(0, -280)

