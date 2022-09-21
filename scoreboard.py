from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle() #Hide the arrow
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard() #call thos metod because it's initiallize evry time when we set the scoreboard

    def update_scoreboard(self):
        self.goto(-100, 200) # Move scoreboard to the top of screen
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)  # Move scoreboard to the top of screen
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score = self.l_score+1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score = self.r_score+1
        self.clear()
        self.update_scoreboard()

