from turtle import Screen
from pong import Paddle
from ball import Ball
import  time
from score import Score

my_screen = Screen()
my_screen.setup(800, 600)
my_screen.title("My Pong game")
my_screen.bgcolor('black')
my_screen.tracer(0)

paddle0 = Paddle((350,0))
paddle1 = Paddle((-350, 0))
ball = Ball()
score = Score()


my_screen.listen()
my_screen.onkeypress(paddle0.go_up, "Up")
my_screen.onkeypress(paddle0.go_down, 'Down')
my_screen.onkeypress(paddle1.go_up, "w")
my_screen.onkeypress(paddle1.go_down, 's')

ok = True
while ok:
    time.sleep(ball.sleep_time)
    my_screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    # collision with right paddle
    if ball.distance(paddle0) < 50 and ball.xcor() > 320 or ball.distance(paddle1) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_point()

#detect left paddle position
    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_point()





my_screen.exitonclick()