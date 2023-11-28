from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.dx = 5
        self.dy = 5

    def move_r(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    #adjusts the balls movement towards left
    def reset_pos(self):
        self.hideturtle()
        self.goto(0, 0)  # Move the ball to the center
        self.showturtle()

    def move_l(self):
        self.bounce_x()
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)


    def bounce_y(self):
        self.dy *= -1  # Reverse the vertical direction to bounce off

    def bounce_x(self):
        self.dx *= -1
















