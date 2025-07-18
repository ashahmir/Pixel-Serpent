from turtle import Turtle
from snake import Snake

with open("score.txt", mode="r") as file:
    score = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.highScore = int(score)
        self.goto(0,280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}           Highscore: {self.highScore}", align="center",
                   font=("Arial", 14, "normal"))

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("score.txt", mode="w") as f:
                f.write(str(self.highScore))

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def decrease_score(self):
        self.score -= 1
        self.update_score()

    def exit_game(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Arial", 14, "normal"))

# CREDITS: a.shahmir
