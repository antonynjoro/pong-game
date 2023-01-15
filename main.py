from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from player import Player
from score import Score
from random import randint

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title("Pong")
screen.listen()
screen.tracer(0)

right_edge = (SCREEN_WIDTH / 2) - 50
left_edge = (SCREEN_WIDTH / -2) + 50

l_paddle = Paddle((left_edge, 0))
r_paddle = Paddle((right_edge, 0))

score = Score()

ball = Ball(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
score.draw_divider()
player_r = Player(50)
player_l = Player(-50)

game_is_on = True

while game_is_on:

    screen.update()
    ball.move()
    time.sleep(0.1)
    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, "Down")
    screen.onkey(l_paddle.move_up, "w")
    screen.onkey(l_paddle.move_down, "s")

    #   if ball hits top walls, bounce back
    if ball.ycor() > (SCREEN_HEIGHT / 2 - 20) or ball.ycor() < (SCREEN_HEIGHT / -2 + 20):
        ball.y_move *= -1

    # if the paddle hits the ball, bounce back
    if r_paddle.xcor() - 20 < ball.xcor() and r_paddle.distance(ball.position()) < 50 or l_paddle.xcor() + 20 > ball.xcor() and l_paddle.distance(ball.position()) < 50:
        ball.x_move *= -1

    if ball.xcor() > SCREEN_WIDTH / 2:
        player_l.score += 1
        player_l.show_score()
        ball.goto(0, 0)

    elif ball.xcor() < SCREEN_WIDTH / -2:
        player_r.score += 1
        player_r.show_score()

        ball.goto(0, 0)

screen.exitonclick()
