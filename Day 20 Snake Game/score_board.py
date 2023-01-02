from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align = 'center', font=('Arial', 10) )
        self.hideturtle()

    def updatescore(self):
        self.write(f"Score: {self.score}", align='center', font=('Arial', 10))

    def increasescore(self):
        self.clear()
        self.score += 1
        self.clear()
        self.updatescore()
