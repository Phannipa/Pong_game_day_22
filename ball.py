#Make a ball to move from the center of screen to the right top of screen
from turtle import Turtle



class Ball (Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10 #Make attribute that every time when the ball move, it's going to increase in the x cooridate by 10 pixels.
        self.y_move = 10
        self.move_speed = 0.1 # set the speed at 0.1 because we will increase speed every time when the ball hit the paddle.

    def move(self): #Ball moves increase 10 pixels
        new_x = self.xcor() + self.x_move # self.xcor() means from current position and then move 10 pixels
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self): #Ball move decrease 10 pixels to bounce
        self.y_move = self.y_move * -1 # Move means it increases 10 pixels, bouncing decrease 10 pixels
        # and then it will ove to the opposite direction. This bounce move vertical direction
        # because it moves from center of screen to the right top of screen.

    def bounce_x(self): #bounce_x means the paddle hit the ball.
        self.x_move = self.x_move * -1
        self.move_speed = self.move_speed * 0.9 #It means every time when the paddle hit the ball, the speed will decrese (such as speed is 5--> 5x0.9 = 4.5)


    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1 #When we reset, reset to the same speed at 0.1
        self.bounce_x() # After they hit the wall (move in vertical direction), it will bounce in the horizontal direction to the other side of the screen.


