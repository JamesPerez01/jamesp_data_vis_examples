from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        """Manages 'food' properties. Spawns initial food in random position"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)

    def refresh(self):
        """Moves 'food' to a random position in screen"""
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(x=random_x, y=random_y)
        