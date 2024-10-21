from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score =0
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"score = {self.score}", False, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()