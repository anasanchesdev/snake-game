from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, shape):
        super().__init__()
        self.shape(shape)
        self.shapesize(10, 10)
        self.color('yellow')
        self.penup()
        self.speed('fastest')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))

