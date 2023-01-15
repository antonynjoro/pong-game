from turtle import Turtle, Screen


# TODO create ball class
class Ball(Turtle):
    def __init__(self,height, width):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(1, 1)
        self.color('white')
        self.x_move = 10
        self.y_move = 10



    def move(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.setposition(new_x_cor, new_y_cor)

