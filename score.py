from turtle import Turtle

# TODO create score card
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0


    def draw_divider(self):
        self.sety(-280)
        self.setx(0)
        self.pensize(5)
        self.setheading(90)
        self.pendown()
        self.color('white')
        for i in range(15):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()



