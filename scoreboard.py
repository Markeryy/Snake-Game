from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=250)
        self.draw_score(self.score)  # draw initial score
        
    def draw_score(self, new_score):
        self.clear()
        self.write(
            align="center",
            arg=f"Score: {new_score}",
            font=("Arial", 24, "normal")
        )

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(
            align="center",
            arg=f"Game over!\nScore: {self.score}",
            font=("Arial", 24, "normal")
        )
        
    def increase_score(self):
        self.score += 1
        self.draw_score(self.score)