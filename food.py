import random
from turtle import Turtle
import time

# poisonous food reminder


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.random_x = 0
        self.random_y = 0

    def normal_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.random_x = random.randint(-280,280)
        self.random_y = random.randint(-280, 280)
        self.goto(self.random_x, self.random_y)

    def poison(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.random_x = random.randint(-280, 280)
        self.random_y = random.randint(-280, 280)
        self.goto(self.random_x, self.random_y)
# CREDITS: a.shahmir
