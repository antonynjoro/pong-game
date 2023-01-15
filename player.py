# TODO create player class

from score import Score
from paddle import Paddle


class Player(Score):
    def __init__(self, x_pos):
        super().__init__()
        self.sety(250)
        self.xposition = x_pos
        self.setx(self.xposition)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(self.score , False, align="center", font=("ariel", 35, 'normal'))



