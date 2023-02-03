from turtle import Turtle


ALIGNMENT = "center"
SCORE_FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 30, "normal")
NEW_HIGHSCORE_FONT = ("Courier", 18, "normal")


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
        """Clears all scoreboard objects and reprints main scoreboard with updated score.
        Called after collision with food to update scoreboard or called after Play Again.
        Called by reset, add_point, and play_again methods"""
        self.clear()
        self.write(arg=f"Score: {self.score}  |  High Score: {self.highscore}", align=ALIGNMENT, font=SCORE_FONT)

    def game_over(self):
        """Resets scoreboard and track High Score. Called after collision with tail or screen boundary"""
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
            self.goto(0, 80)
            self.write(arg="NEW HIGH SCORE!", align=ALIGNMENT, font=NEW_HIGHSCORE_FONT)

    def reset(self):
        """Resets scoreboard. Called after play_again"""
        self.goto(x=0, y=280)
        self.score = 0
        self.update_scoreboard()

    def add_point(self):
        """Adds point to scoreboard"""
        self.score += 1
        self.update_scoreboard()

    def play_again(self):
        """Displays option to play again"""
        self.goto(0, -60)
        self.write(arg="Press [ENTER] to play again!", align=ALIGNMENT, font=SCORE_FONT)
