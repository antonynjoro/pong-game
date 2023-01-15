from turtle import Turtle
from ball import Ball

# TODO create paddle class
class Paddle(Turtle):
    def __init__(self, position: tuple):
        super().__init__()
        self.shapesize(1, 5)
        self.penup()
        self.color('white')
        self.shape('square')
        self.setposition(position)
        self.left(90)

    def move_up(self):
        self.forward(20)
        print("UUUUP")

    def move_down(self):
        self.back(20)
        print("DOWWWWWN")


