from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level:{self.score}", align='left', font=("Arial", 15))

    def level_up(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write("Game Over", font=("Arial", 15), align='center')

    def show_score(self):
        self.goto(0, -100)
        self.color('green')
        self.write(f"Your turtle succeed {self.score} time in the game.", font=("Arial", 15), align='center')
