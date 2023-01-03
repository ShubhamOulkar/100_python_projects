from turtle import  Turtle
import random
colors = ["red","blue","green","orange","purple","pink"]

class Car:

    def __init__(self):
        super().__init__()
        self.all_car = []
        self.car_speed = 10

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_car.append(new_car)

    def move_car(self):
        for car in self.all_car:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed *= 0.9



