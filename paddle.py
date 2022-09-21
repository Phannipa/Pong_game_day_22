# Create left and right paddles that respond to key press.
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position): #Pass position as argument because we identified the position of objects
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) #We set our paddle width =20, height =100. All turtle start off as 20 by 20.
        # So that means in the width, we have to stretch it by 5, and in the length
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor()+20 # we move up on vertical at 20. We cannot use self.heading(90), it changes the paddle to be horizonal.
        self.goto(self.xcor(), new_y) # xcor() is the same position.

    def go_down(self):
        new_y = self.ycor() - 20  # we move up on vertical at 20
        self.goto(self.xcor(), new_y)  # xcor() is the same postion
