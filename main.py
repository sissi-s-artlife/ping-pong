from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
scoreboard= Scoreboard()


r_paddle=Paddle((350,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


l_paddle=Paddle((-350,0))

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



# Create a ball instance
ball = Ball()
game_is_on=True
while game_is_on:
    ball.move_r()
    screen.update()
    if ball.ycor() > 290 or ball.ycor() < -280:  # Adjust this value based on your screen dimensions
        ball.bounce_y()
    if ball.xcor() > 330 and ball.distance(r_paddle)<=50 or ball.xcor()<-330 and ball.distance(l_paddle)<50:
        ball.bounce_x()
        # Ball goes past right paddle
    if ball.xcor() > 400:
        ball.reset_pos()  # Reset ball position
        ball.move_l()
        scoreboard.l_point()
    if ball.xcor() < -400:
        ball.reset_pos()
        ball.bounce_x()
        scoreboard.r_point()










































screen.exitonclick()