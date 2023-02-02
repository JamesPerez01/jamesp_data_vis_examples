from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Adds points to scoreboard. Called after collision with food"""
        self.clear()
        self.write(arg=f"Score: {self.score} High Score :{self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Resets scoreboard. Called after collision with tail or screen boundary"""
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def add_point(self):
        self.score += 1
        self.update_scoreboard()
