from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

turtle = Turtle()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0) #Turn the animation function off because the paddle create at the center
# and then it moves to the location where we need to on right side of screen.
# So we use screen.tracy(0) to get rid off that animation
# and show paddle on the position that we need without move from the center.


# Create left and right paddles that respond to key press.
r_paddle = Paddle((350, 0)) # right side of screen
l_paddle = Paddle((-350, 0)) # left side if screen

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up") #Do not have parenthesis after paddle.move_up when we call function.
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Create dash line middle the screen.
turtle.hideturtle()
screen.title("Pong Game")
# turtle.color("white")
# turtle.penup()
# turtle.sety(-300)


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed) # we will stop time 0.1 second every each of update. It means ball will move slowly

    screen.update() #every time when we change we have to update screen after turn off the animation. After we update the screen, ball moves

    # Ball moves from center to the right top of screen.
    ball.move()


    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280: #The ball will hit the wall when y coordinate is 300 and -300
        ball.bounce_y() #Need to bounce.

    # Detect collision with paddle # Move in horizontal direction.
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
    #Size of ball and paddle are 20x20. If ball hot the edge of paddle, so it means the distance are more than 20. We have to use x coordinate to help this logic.
        ball.bounce_x()

# Detect r_paddle miss the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


# Detect l_paddle miss the ball.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()











screen.exitonclick()
